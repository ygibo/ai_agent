from __future__ import annotations
from typing import Protocol, Optional
from ai_agent.common.domain.conversation.entities.conversation import Conversation
from ai_agent.common.domain.value_objects.page import Page
from ai_agent.common.domain.conversation.value_objects.conversation_order_by import ConversationOrderBy
from ai_agent.common.domain.value_objects.sort_order import SortOrder


class ConversationSearchService(Protocol):
    def list_conversations(
        self,
        user_id: str,
        order_by: ConversationOrderBy = ConversationOrderBy.CREATED_AT,
        order: SortOrder = SortOrder.DESC,
        limit: int = 10,
        next_page_token: Optional[str] = None
    ) -> Page[Conversation]: ...