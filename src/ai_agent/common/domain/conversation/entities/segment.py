from __future__ import annotations
from datetime import datetime
from uuid6 import uuid7
from typing import Optional
from ai_agent.common.domain.services.datetime_service import utc_now


"""
    セグメントは分岐を含まない会話の連続した部分を表す。
    分岐を作成した際に新しいセグメントが作成され、親セグメントの最後のメッセージを起点とする。
"""
class Segment:
    def __init__(
        self,
        segment_id: str,
        conversation_id: str, # セグメントが属する会話の ID
        parent_segment_id: Optional[str] = None, # 分岐元の親セグメントの ID
        start_from_message_id: Optional[str] = None, # セグメントの起点となる親セグメントのメッセージの ID
        created_at: Optional[datetime] = None
    ):
        self.__segment_id = segment_id
        self.__conversation_id = conversation_id
        self.__parent_segment_id = parent_segment_id
        self.__start_from_message_id = start_from_message_id
        self.__created_at = created_at or utc_now()


    """
        新しく会話が開始された際の起点となるセグメントのルートを作成する。
        ルートセグメントは親セグメントがない。
    """
    @classmethod
    def new_root(cls, conversation_id: str) -> "Segment":
        return cls(
            segment_id=str(uuid7()), 
            conversation_id=conversation_id
        )

    """
        分岐を作成した際の新しいセグメントを作成する。
        分岐セグメントは親セグメントがあり、親セグメントの最後のメッセージを起点とする。
    """
    @classmethod
    def new_branch(
        cls,
        conversation_id: str,
        parent_segment_id: str,
        start_from_message_id: str
    ) -> "Segment":
        return cls(
            segment_id=str(uuid7()), 
            conversation_id=conversation_id,
            parent_segment_id=parent_segment_id,
            start_from_message_id=start_from_message_id
        )

    @property
    def segment_id(self) -> str:
        return self.__segment_id

    @property
    def conversation_id(self) -> str:
        return self.__conversation_id

    @property
    def parent_segment_id(self) -> Optional[str]:
        return self.__parent_segment_id

    @property
    def start_from_message_id(self) -> Optional[str]:
        return self.__start_from_message_id

    @property
    def created_at(self) -> datetime:
        return self.__created_at