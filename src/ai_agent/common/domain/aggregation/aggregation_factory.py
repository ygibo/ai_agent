from ai_agent.common.domain.aggregation.value_objects.aggregation_config import AggregationConfig
from ai_agent.common.domain.aggregation.aggregation_protocol import AggregationMethodProtocol
from ai_agent.common.domain.aggregation.one_sample import OneSampleAggregationMethod
from ai_agent.common.domain.aggregation.majority_vote import MajorityVoteAggregationMethod

def create_aggregation_method(
    aggregation_config: AggregationConfig
) -> AggregationMethodProtocol:
    if aggregation_config.aggregation_method_name == "one_sample":
        return OneSampleAggregationMethod()
    elif aggregation_config.aggregation_method_name == "majority_vote":
        return MajorityVoteAggregationMethod()
    else:
        raise ValueError(f"Invalid aggregation method: {aggregation_config.aggregation_method_name}")
    