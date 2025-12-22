from datetime import datetime, timedelta, timezone

from ai_agent.common.domain.conversation.entities.segment import Segment
from ai_agent.common.domain.conversation.entities.user_segment_history import UserSegmentHistory
from ai_agent.common.domain.conversation.value_objects.user_segment_graph import SegmentGraph

def make_segment(segment_id, conversation_id, parent_segment_id=None, start_from_message_id=None):
    return Segment(
        segment_id=segment_id,
        conversation_id=conversation_id,
        parent_segment_id=parent_segment_id,
        start_from_message_id=start_from_message_id,
    )

def test_get_head_user_segment_node_returns_most_recent_descendant():
    conv_id = "conv-1"
    user_id = "user-1"
    now = datetime(2025, 1, 1, tzinfo=timezone.utc)

    root = make_segment("seg-root", conv_id, parent_segment_id=None, start_from_message_id=None)
    child1 = make_segment("seg-1", conv_id, parent_segment_id="seg-root", start_from_message_id="msg-1")
    child2 = make_segment("seg-2", conv_id, parent_segment_id="seg-1", start_from_message_id="msg-2")

    segments = [root, child1, child2]

    histories = [
        UserSegmentHistory(user_id, conv_id, "seg-root", last_viewed_at=now),
        UserSegmentHistory(user_id, conv_id, "seg-2",   last_viewed_at=now + timedelta(minutes=15)),
        UserSegmentHistory(user_id, conv_id, "seg-1",   last_viewed_at=now + timedelta(minutes=10)),
    ]

    graph = SegmentGraph(conversation_id=conv_id)
    graph.add_segments(segments, histories)

    head = graph.get_head_user_segment_node(
        from_segment_id="seg-root",
        from_message_id="msg-0",  # root からすべての分岐を対象とする想定
    )

    assert head.segment.segment_id == "seg-2"

def test_get_head_user_segment_node_returns_most_recent_descendant_when_from_message_id_is_none():
    conv_id = "conv-1"
    user_id = "user-1"
    now = datetime(2025, 1, 1, tzinfo=timezone.utc)

    root = make_segment("seg-root", conv_id, parent_segment_id=None, start_from_message_id=None)
    child1 = make_segment("seg-1", conv_id, parent_segment_id="seg-root", start_from_message_id="msg-1")
    child2 = make_segment("seg-2", conv_id, parent_segment_id="seg-1", start_from_message_id="msg-2")

    segments = [root, child1, child2]

    histories = [
        UserSegmentHistory(user_id, conv_id, "seg-root", last_viewed_at=now),
        UserSegmentHistory(user_id, conv_id, "seg-2",   last_viewed_at=now + timedelta(minutes=15)),
        UserSegmentHistory(user_id, conv_id, "seg-1",   last_viewed_at=now + timedelta(minutes=10)),
    ]

    graph = SegmentGraph(conversation_id=conv_id)
    graph.add_segments(segments, histories)

    head = graph.get_head_user_segment_node(
        from_segment_id="seg-root",
        from_message_id=None,  # root からすべての分岐を対象とする想定
    )

    assert head.segment.segment_id == "seg-2"