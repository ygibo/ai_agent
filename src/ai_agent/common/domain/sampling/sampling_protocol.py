from typing import Protocol, Optional
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage


class SamplingMethodProtocol(Protocol):
    def sample(
        self,
        system_prompt: Optional[str],
        messages: list[ChatMessage]
    ) -> list[ChatMessage]: ...