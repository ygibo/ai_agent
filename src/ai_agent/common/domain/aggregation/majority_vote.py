from typing import Counter
from ai_agent.common.domain.aggregation.aggregation_protocol import AggregationMethodProtocol


class MajorityVoteAggregationMethod(AggregationMethodProtocol):
    def __init__(self):
        pass

    def aggregate(
        self,
        samples: list[str]
    ) -> str:
        return Counter[str](samples).most_common(1)[0][0]