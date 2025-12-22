from __future__ import annotations
from typing import Protocol
from ai_agent.common.domain.conversation.entities.user_conversation_state import UserConversationState


class UserConversationStateRepository(Protocol):
    def get_user_conversation_state(self, user_id: str, conversation_id: str) -> UserConversationState: ...
