from typing import Protocol, Optional
from ai_agent.common.domain.value_objects.chat_message import ChatMessage

class LLMClientProtocol(Protocol):
    def generate_text(
        self,
        system_prompt: Optional[str],
        messages: list[ChatMessage]
    ) -> ChatMessage:
        pass