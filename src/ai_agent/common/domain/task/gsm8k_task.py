import re
from decimal import Decimal
from ai_agent.common.domain.task.task_protocol import TaskProtocol
from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol


class GSM8KTask(TaskProtocol):
    def __init__(
        self,
        prompt_service: PromptServiceProtocol
    ):
        self.__prompt_service = prompt_service
    
    def build_prompt(self, question: str) -> str:
        return self.__prompt_service.get_prompt(question)
    
    def extract_answer(self, response: str) -> str:
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

    def extract_answer_from_ground_truth(self, ground_truth: str) -> str:
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

    def is_correct(self, answer: str, ground_truth: str) -> bool:
        number1 = GSM8KTask.__normalize_number(answer)
        number2 = GSM8KTask.__normalize_number(ground_truth)
        if number1 is None or number2 is None:
            return False
        return number1 == number2