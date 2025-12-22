from typing import Protocol, Optional
from ai_agent.common.domain.reasoning_algorithms.value_objects.reasoning_result import ReasoningResult


class ReasoningAlgorithmProtocol(Protocol):
    def infer_answer(
        self,
        system_prompt: Optional[str],
        question: str
    ) -> ReasoningResult: ...

    