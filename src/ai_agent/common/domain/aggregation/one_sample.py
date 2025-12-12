from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.aggregation.aggregation_protocol import AggregationMethodProtocol


class OneSampleAggregationMethod(AggregationMethodProtocol):
    def __init__(self):
        pass

    def aggregate(
        self,
        samples: list[str]
    ) -> str:
        if len(samples) != 1:
            raise ValueError("One sample aggregation method requires exactly one sample")
        return samples[0]