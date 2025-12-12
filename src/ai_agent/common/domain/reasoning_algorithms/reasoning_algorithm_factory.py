from ai_agent.common.domain.reasoning_algorithms.value_objects.reasoning_algorithm_config import ReasoningAlgorithmConfig
from ai_agent.common.domain.reasoning_algorithms.normal_reasoning_algorithm import NormalReasoningAlgorithm
from ai_agent.common.domain.reasoning_algorithms.reasoning_algorithm_protocol import ReasoningAlgorithmProtocol
from ai_agent.common.domain.sampling.sampling_protocol import SamplingMethodProtocol
from ai_agent.common.domain.aggregation.aggregation_protocol import AggregationMethodProtocol
from ai_agent.common.domain.task.task_protocol import TaskProtocol


def create_reasoning_algorithm(
    reasoning_algorithm_config: ReasoningAlgorithmConfig,
    sampling_method: SamplingMethodProtocol,
    aggregation_method: AggregationMethodProtocol,
    task_protocol: TaskProtocol
) -> ReasoningAlgorithmProtocol:
    if reasoning_algorithm_config.reasoning_algorithm_name == "normal_reasoning_algorithm":
        return NormalReasoningAlgorithm(
            sampling_method=sampling_method,
            aggregation_method=aggregation_method,
            task_protocol=task_protocol
        )
    else:
        raise ValueError(f"Invalid reasoning algorithm: {reasoning_algorithm_config.name}")