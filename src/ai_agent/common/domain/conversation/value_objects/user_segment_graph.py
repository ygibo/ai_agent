from __future__ import annotations
from ai_agent.common.domain.conversation.entities.segment import Segment
from ai_agent.common.domain.conversation.entities.user_segment_node import UserSegmentNode
from ai_agent.common.domain.conversation.entities.user_segment_history import UserSegmentHistory
from ai_agent.common.domain.conversation.errors import SegmentConflictError


class SegmentGraph:
    def __init__(
        self,
        conversation_id: str
    ) -> None:
        self.__conversation_id = conversation_id
        self.__root_segment_id = None
        self.__segment_id_to_node = {} # {segment_id: UserSegmentNode}
        self.__segment_id_to_children_nodes = {} # {segment_id: [UserSegmentNode, ...]}

    def __add_segment(self, segment: Segment) -> None:
        if segment.parent_segment_id is None:
            self.__root_segment_id = segment.segment_id

        node = UserSegmentNode(
            index=len(self.__segment_id_to_node),
            segment=segment
        )
        self.__segment_id_to_node[segment.segment_id] = node
        self.__segment_id_to_children_nodes[segment.segment_id] = []

    def __set_user_segment_history(self, user_segment_history: UserSegmentHistory) -> None:
        node = self.__segment_id_to_node[user_segment_history.segment_id]
        node.user_segment_history = user_segment_history

    def add_segments(self, segments: list[Segment], user_segment_histories: list[UserSegmentHistory]) -> None:
        for segment in segments:
            self.__add_segment(segment)
        for user_segment_history in user_segment_histories:
            self.__set_user_segment_history(user_segment_history)

        # 親から子にたどれるようにセグメントの親から子への参照を設定する
        for node in self.__segment_id_to_node.values():
            if node.segment.parent_segment_id is not None:
                self.__segment_id_to_children_nodes[node.segment.parent_segment_id].append(node)
    
    """
        指定したセグメントから最後に見た HEAD ノードを取得する。
    """
    def get_head_user_segment_node(
        self, from_segment_id: str, from_message_id: str
    ) -> UserSegmentNode:
        if from_segment_id not in self.__segment_id_to_node:
            raise SegmentConflictError()

        from_node = self.__segment_id_to_node[from_segment_id]
        stack = [from_node]
        visited_segment_ids = set()
        most_recent_viewed_node = None

        while stack:
            current_node: UserSegmentNode = stack.pop()
            # 開始 segment の開始メッセージより前のメッセージから分岐した場合はスキップする
            if current_node.segment.segment_id == from_node.segment.segment_id:
                if current_node.segment.start_from_message_id is not None and from_message_id is not None:
                    if current_node.segment.start_from_message_id >= from_message_id:
                        continue
            if most_recent_viewed_node is None:
                most_recent_viewed_node = current_node
            else:
                if current_node.last_viewed_at > most_recent_viewed_node.last_viewed_at:
                    most_recent_viewed_node = current_node
            childrens = self.__segment_id_to_children_nodes[current_node.segment.segment_id]
            stack.extend(
                filter(lambda x: x.segment.segment_id not in visited_segment_ids, childrens)
            )

        return most_recent_viewed_node

    """
        HEAD ノードからルートノードまでのセグメントパスを取得する。
    """
    def get_segment_path_to_head(
        self,
    ) -> list[Segment]:
        if self.__root_segment_id is None:
            raise SegmentConflictError()

        head_node = self.get_head_user_segment_node(
            from_segment_id=self.__root_segment_id,
            from_message_id=None
        )