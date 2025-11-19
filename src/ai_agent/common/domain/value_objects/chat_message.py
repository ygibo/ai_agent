from pydantic import BaseModel, Field
from typing import Any
from ai_agent.common.domain.value_objects.chat_role import ChatRole


class ChatMessage(BaseModel):
    role: ChatRole = Field(..., description="メッセージの役割")
    content: str = Field(..., description="メッセージの内容")
