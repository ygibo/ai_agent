from enum import Enum


class UserSegmentHistoryOrderBy(str, Enum):
    CREATED_AT = "created_at"
    LAST_VIEWED_AT = "last_viewed_at"