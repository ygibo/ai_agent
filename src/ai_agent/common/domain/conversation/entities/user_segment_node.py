from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from ai_agent.common.domain.conversation.entities.segment import Segment
from ai_agent.common.domain.conversation.entities.user_segment_history import UserSegmentHistory
from datetime import datetime


@dataclass
class UserSegmentNode:
    index: int
    segment: Segment
    user_segment_history: Optional[UserSegmentHistory] = None

    @property
    def last_viewed_at(self) -> datetime:
        if self.user_segment_history is None:
            return self.segment.created_at
        return self.user_segment_history.last_viewed_at
