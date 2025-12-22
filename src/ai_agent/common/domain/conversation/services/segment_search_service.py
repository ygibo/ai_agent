from __future__ import annotations
from typing import Protocol, Optional
from ai_agent.common.domain.conversation.entities.segment import Segment
from ai_agent.common.domain.value_objects.page import Page
from ai_agent.common.domain.conversation.value_objects.segment_order_by import SegmentOrderBy
from ai_agent.common.domain.value_objects.sort_order import SortOrder


class SegmentSearchService(Protocol):
    def list_segments(
        self,
        conversation_id: str,
        order_by: SegmentOrderBy = SegmentOrderBy.CREATED_AT,
        order: SortOrder = SortOrder.DESC,
        limit: int = 10,
        next_page_token: Optional[str] = None
    ) -> Page[Segment]: ...