from dataclasses import dataclass
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage

@dataclass
class ReasoningResult:
    final_answer: str
    messages: list[ChatMessage]