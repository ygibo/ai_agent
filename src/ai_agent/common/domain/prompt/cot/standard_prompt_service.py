from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol
from ai_agent.common.domain.datasets.value_objects.dataset_types import DatasetType
from ai_agent.common.domain.prompt.cot.prompts_gsm8k import STANDARD_PROMPT_TEMPLATE_FOR_GSM8K


class StandardPromptService(PromptServiceProtocol):
    def __init__(self, dataset_type: DatasetType):
        self.dataset_type = dataset_type

    def get_prompt(self, question: str) -> str:
        if self.dataset_type == DatasetType.GSM8K:
            return STANDARD_PROMPT_TEMPLATE_FOR_GSM8K.format(question=question)
        else:
            raise ValueError(f"Invalid dataset type: {self.dataset_type}")

