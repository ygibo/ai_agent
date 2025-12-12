from ai_agent.common.domain.sampling.value_objects.sampling_config import SamplingConfig
from ai_agent.common.domain.sampling.sampling_protocol import SamplingMethodProtocol
from ai_agent.common.domain.sampling.greedy import GreedySamplingMethod
from ai_agent.common.domain.sampling.top_p_sampling import TopPSamplingMethod
from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol


def create_sampling_method(
    sampling_config: SamplingConfig,
    llm_client: LLMClientProtocol
) -> SamplingMethodProtocol:
    if sampling_config.sampling_method_name == "greedy":
        return GreedySamplingMethod(
            temperature=sampling_config.temperature,
            llm_client=llm_client
        )
    elif sampling_config.sampling_method_name == "top_p":
        return TopPSamplingMethod(
            top_p=sampling_config.top_p,
            temperature=sampling_config.temperature,
            num_samples_per_query=sampling_config.num_samples_per_query,
            llm_client=llm_client
        )
    else:
        raise ValueError(f"Invalid sampling method: {sampling_config.method}")
