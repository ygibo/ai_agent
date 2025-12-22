from ai_agent.common.domain.reasoning_algorithms.reasoning_algorithm_protocol import ReasoningAlgorithmProtocol
from ai_agent.common.domain.sampling.sampling_protocol import SamplingMethodProtocol
from ai_agent.common.domain.task.task_protocol import TaskProtocol
from ai_agent.common.domain.aggregation.aggregation_protocol import AggregationMethodProtocol
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.chat.value_objects.chat_role import ChatRole
from ai_agent.common.domain.reasoning_algorithms.value_objects.reasoning_result import ReasoningResult
from typing import Optional


class NormalReasoningAlgorithm(ReasoningAlgorithmProtocol):
    def __init__(
        self,
        sampling_method: SamplingMethodProtocol,
        aggregation_method: AggregationMethodProtocol,
        task_protocol: TaskProtocol
    ):
        self.__sampling_method: SamplingMethodProtocol = sampling_method
        self.__aggregation_method: AggregationMethodProtocol = aggregation_method
        self.__task_protocol: TaskProtocol = task_protocol

    def infer_answer(
        self,
        system_prompt: Optional[str],
        question: str
    ) -> str:
        samples: list[ChatMessage] = self.__sampling_method.sample(
            system_prompt=system_prompt,
            messages=[ChatMessage(role=ChatRole.USER, content=question)]
        )
        if samples is None or len(samples) == 0:
            raise ValueError("No samples found")
        answers = []
        for sample in samples:
            answer = self.__task_protocol.extract_answer(sample.content)
            answers.append(answer)
        final_answer = self.__aggregation_method.aggregate(answers)
        return ReasoningResult(final_answer=final_answer, messages=samples)
