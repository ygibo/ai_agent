from __future__ import annotations
from datetime import datetime
from typing import Optional
from ai_agent.common.domain.services.datetime_service import utc_now


"""
    UserSegmentHistory はユーザーがセグメントを最後に見た日時を表す。
    セグメントの履歴を保持することで、ユーザーがセグメントを過去に見たことを再現することができる。
"""
class UserSegmentHistory:
    def __init__(
        self,
        user_id: str,
        conversation_id: str,
        segment_id: str,
        last_viewed_at: Optional[datetime] = None
    ):
        self.__user_id = user_id
        self.__conversation_id = conversation_id
        self.__segment_id = segment_id
        self.__last_viewed_at = last_viewed_at or utc_now()

    @classmethod
    def new(cls, user_id: str, conversation_id: str, segment_id: str) -> "UserSegmentHistory":
        return cls(
            user_id=user_id,
            conversation_id=conversation_id,
            segment_id=segment_id
        )

    @property
    def user_id(self) -> str:
        return self.__user_id
    
    @property
    def conversation_id(self) -> str:
        return self.__conversation_id
    
    @property
    def segment_id(self) -> str:
        return self.__segment_id
    
    @property
    def last_viewed_at(self) -> datetime:
        return self.__last_viewed_at

    def update_last_viewed_at(self) -> None:
        self.__last_viewed_at = utc_now()