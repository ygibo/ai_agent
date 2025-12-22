from ai_agent.common.domain.reasoning_algorithms.reasoning_algorithm_protocol import ReasoningAlgorithmProtocol
from ai_agent.common.domain.task.task_protocol import TaskProtocol
from ai_agent.common.domain.reasoning_algorithms.value_objects.reasoning_result import ReasoningResult
from ai_agent.common.domain.sampling.sampling_protocol import SamplingMethodProtocol
from typing import Optional


class ReactReasoningAlgorithm(ReasoningAlgorithmProtocol):
    def __init__(
        self,
        sampling_method: SamplingMethodProtocol,
        task_protocol: TaskProtocol
    ):
        self.__sampling_method: SamplingMethodProtocol = sampling_method
        self.__task_protocol: TaskProtocol = task_protocol

    def infer_answer(
        self,
        system_prompt: Optional[str],
        question: str
    ) -> ReasoningResult:
        return ReasoningResult(final_answer=final_answer, messages=messages)