import random
import re
from ai_agent.common.application.services.llm_client_protocol import LLMClientProtocol
from ai_agent.chain_of_thought.domain.services.prompt_service import PromptService
from ai_agent.common.domain.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.value_objects.chat_role import ChatRole
from decimal import Decimal
from ai_agent.common.application.services.experiment_callback import ExperimentCallback


class ExperimentExecutionService:
    def __init__(self, llm_client: LLMClientProtocol):
        self.__llm_client = llm_client
    
    @staticmethod
    def __extract_answer(response: str) -> str:
        lines = response.splitlines()
        answer_line = None
        for line in lines[::-1]:
            if "ANSWER:" in line.upper():
                answer_line = line
                break
        target = answer_line if answer_line is not None else response
        m = re.search(r"-?\d+(?:\.\d+)?", target)
        if m:
            return m.group(0)
        return None

    @staticmethod
    def __extract_answer_from_ground_truth(ground_truth: str) -> str:
        if "####" in ground_truth:
            tail = ground_truth.split("####")[-1]
        else:
            tail = ground_truth
        m = re.search(r"-?\d+(\.\d+)?", tail)
        if not m:
            return None
        return m.group(0)

    @staticmethod
    def __normalize_number(number: str) -> str:
        m = re.search(r"-?\d+(?:\.\d+)?", number)
        if not m:
            return None
        try:
            return Decimal(m.group(0))
        except Exception as e:
            return None

    def __equal_numbers(number1: str, number2: str) -> bool:
        number1 = ExperimentExecutionService.__normalize_number(number1)
        number2 = ExperimentExecutionService.__normalize_number(number2)
        if number1 is None or number2 is None:
            return False
        return number1 == number2

    def run_experiment(
        self,
        dataset: list[dict],
        prompt_service: PromptService,
        experiment_callback: ExperimentCallback
    ) -> None:
        results = []

        for idx, item in enumerate(dataset):
            experiment_callback.on_iteration_start(idx, item)
            q = item["question"]
            gt = ExperimentExecutionService.__extract_answer_from_ground_truth(item["answer"])

            prompt = prompt_service.get_prompt(q)
            experiment_callback.on_llm_request(idx, prompt)
            chat_message = ChatMessage(role=ChatRole.USER, content=prompt)
            response = self.__llm_client.generate_text(None, [chat_message])
            experiment_callback.on_llm_response(idx, response)
            answer = ExperimentExecutionService.__extract_answer(response.content)
            if ExperimentExecutionService.__equal_numbers(answer, gt):
                results.append(True)
            else:
                results.append(False)
            experiment_callback.on_iteration_end(idx, {
                "answer": answer,
                "ground_truth": gt,
                "result": results[idx]
            })
        
        return {
            "accuracy": sum(results) / len(results)
        }

