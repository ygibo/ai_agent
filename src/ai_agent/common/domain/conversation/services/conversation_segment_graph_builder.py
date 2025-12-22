from __future__ import annotations
from typing import Protocol
from ai_agent.common.domain.conversation.services.conversation_search_service import ConversationSearchService
from ai_agent.common.domain.conversation.services.segment_search_service import SegmentSearchService
from ai_agent.common.domain.conversation.services.user_segment_history_search_service import UserSegmentHistorySearchService


class ConversationSegmentGraphService:
    def __init__(
        self,
        conversation_search_service: ConversationSearchService,
        segment_search_service: SegmentSearchService,
        user_segment_history_search_service: UserSegmentHistorySearchService
    ) -> None:
        self.__conversation_search_service: ConversationSearchService = conversation_search_service
        self.__segment_search_service: SegmentSearchService = segment_search_service
        self.__user_segment_history_search_service: UserSegmentHistorySearchService = user_segment_history_search_service

