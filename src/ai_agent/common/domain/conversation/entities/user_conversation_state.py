from __future__ import annotations
from datetime import datetime
from typing import Optional
from ai_agent.common.domain.services.datetime_service import utc_now


"""
    UserConversationState はユーザーが会話のどのセグメントを見ているかを表す。
    current_segment_id の Segment から親セグメントを辿ることで、会話の履歴を再現することができる。
"""
class UserConversationState:
    def __init__(
        self,
        user_id: str,
        conversation_id: str,
        current_segment_id: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.__user_id = user_id
        self.__conversation_id = conversation_id
        self.__current_segment_id = current_segment_id
        self.__created_at = created_at or utc_now()
    
    @classmethod
    def new(cls, user_id: str, conversation_id: str, current_segment_id: str) -> "UserConversationState":
        return cls(
            user_id=user_id,
            conversation_id=conversation_id,
            current_segment_id=current_segment_id
        )
    
    @property
    def user_id(self) -> str:
        return self.__user_id
    
    @property
    def conversation_id(self) -> str:
        return self.__conversation_id
    
    @property
    def current_segment_id(self) -> str:
        return self.__current_segment_id
    
    @property
    def created_at(self) -> datetime:
        return self.__created_at

    def set_head_segment(self, segment_id: str) -> None:
        self.__current_segment_id = segment_id
        self.__updated_at = utc_now()