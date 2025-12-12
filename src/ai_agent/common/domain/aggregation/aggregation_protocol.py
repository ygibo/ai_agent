from typing import Protocol


class AggregationMethodProtocol(Protocol):
    def aggregate(
        self,
        samples: list[str]
    ) -> str: ...