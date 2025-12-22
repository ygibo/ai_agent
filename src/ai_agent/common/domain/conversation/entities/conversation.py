from __future__ import annotations
from typing import Optional
from uuid6 import uuid7
from datetime import datetime
from ai_agent.common.domain.conversation.errors import *
from ai_agent.common.domain.services.datetime_service import utc_now

"""
    Conversation は 1 つの会話を表す。会話は複数のセグメントとメッセージから構成される
"""
class Conversation:
    def __init__(
        self,
        conversation_id: str,
        user_id: str,
        title: Optional[str] = None, # 会話のタイトル、ない場合は最初のメッセージの内容をタイトルとする
        created_at: Optional[datetime] = None
    ):
        self.__conversation_id = conversation_id
        self.__user_id = user_id
        self.__title = title
        self.__created_at = created_at or utc_now()


    @classmethod
    def new(cls, user_id: str) -> "Conversation":
        return cls(
            conversation_id=str(uuid7()),
            user_id=user_id
        )

    @property
    def conversation_id(self) -> str:
        return self.__conversation_id
    
    @property
    def user_id(self) -> str:
        return self.__user_id
    
    @property
    def title(self) -> Optional[str]:
        return self.__title
    
    @property
    def created_at(self) -> datetime:
        return self.__created_at

    def valid_access(self, user_id: str) -> None:
        if self.__user_id != user_id:
            raise ConversationPermissionDeniedError()
        
    def set_title(self, title: str) -> None:
        if self.__title is None:
            self.__title = title
        else:
            raise ConversationConflictError()