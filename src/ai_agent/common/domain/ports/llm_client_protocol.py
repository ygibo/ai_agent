from typing import Protocol, Optional
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage


class LLMClientProtocol(Protocol):
    def change_parameters(
        self,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
        num_samples_per_query: Optional[int] = None
    ) -> None:
        ...

    def generate_text(
        self,
        system_prompt: Optional[str],
        messages: list[ChatMessage]
    ) -> list[ChatMessage]:
        ...