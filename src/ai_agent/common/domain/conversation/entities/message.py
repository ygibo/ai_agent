from __future__ import annotations
from datetime import datetime
from uuid6 import uuid7
from typing import Optional
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.services.datetime_service import utc_now


"""
    メッセージはセグメント内のメッセージを表す。
    メッセージはチャットメッセージと作成日時から構成される。
"""
class Message:
    def __init__(
        self,
        message_id: str,
        segment_id: str,
        chat_message: ChatMessage,
        created_at: Optional[datetime] = None
    ):
        self.__message_id = message_id
        self.__segment_id = segment_id
        self.__chat_message = chat_message
        self.__created_at = created_at or utc_now()

    @classmethod
    def new(cls, segment_id: str, chat_message: ChatMessage) -> "Message":
        return cls(
            message_id=str(uuid7()),
            segment_id=segment_id,
            chat_message=chat_message
        )

    @property
    def message_id(self) -> str:
        return self.__message_id
    
    @property
    def segment_id(self) -> str:
        return self.__segment_id
    
    @property
    def chat_message(self) -> ChatMessage:
        return self.__chat_message
    
    @property
    def created_at(self) -> datetime:
        return self.__created_at