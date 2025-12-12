from typing import Protocol
from ai_agent.common.domain.reasoning_algorithms.value_objects.reasoning_result import ReasoningResult

class ReasoningAlgorithmProtocol(Protocol):
    def infer_answer(
        self,
        prompt: str
    ) -> ReasoningResult: ...

    