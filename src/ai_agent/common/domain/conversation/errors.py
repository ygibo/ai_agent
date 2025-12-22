from ai_agent.common.domain.errors import *


class ConversationError(DomainError):
    code = "conversation.error"

class ConversationNotFoundError(ConversationError, NotFoundError):
    code = "conversation.not_found"

class ConversationConflictError(ConversationError, ConflictError):
    code = "conversation.conflict"

class ConversationPermissionDeniedError(ConversationError, PermissionDeniedError):
    code = "conversation.permission_denied"

class SegmentConflictError(ConversationError, ConflictError):
    code = "segment.conflict"