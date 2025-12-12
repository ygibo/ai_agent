from ai_agent.common.domain.prompt.value_objects.prompt_config import PromptConfig
from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol
from ai_agent.common.domain.prompt.cot.cot_prompt_service import CotPromptService
from ai_agent.common.domain.prompt.cot.standard_prompt_service import StandardPromptService
from ai_agent.common.domain.datasets.value_objects.dataset_config import DatasetConfig


def create_prompt_service(
    prompt_config: PromptConfig,
    dataset_config: DatasetConfig
) -> PromptServiceProtocol:
    if prompt_config.prompt_name == "few_shot_cot":
        return CotPromptService(dataset_type=dataset_config.get_dataset_type())
    elif prompt_config.prompt_name == "standard":
        return StandardPromptService(dataset_type=dataset_config.get_dataset_type())
    else:
        raise ValueError(f"Invalid prompt service: {prompt_config.prompt_name}")