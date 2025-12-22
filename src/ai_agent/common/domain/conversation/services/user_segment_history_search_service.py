from __future__ import annotations
from typing import Protocol, Optional
from ai_agent.common.domain.conversation.entities.user_segment_history import UserSegmentHistory
from ai_agent.common.domain.value_objects.page import Page
from ai_agent.common.domain.conversation.value_objects.user_segment_history_order_by import UserSegmentHistoryOrderBy
from ai_agent.common.domain.value_objects.sort_order import SortOrder


class UserSegmentHistorySearchService(Protocol):
    def list_user_segment_histories(
        self,
        user_id: str,
        conversation_id: str,
        order_by: UserSegmentHistoryOrderBy = UserSegmentHistoryOrderBy.LAST_VIEWED_AT,
        order: SortOrder = SortOrder.DESC,
        limit: int = 10,
        next_page_token: Optional[str] = None
    ) -> Page[UserSegmentHistory]: ...