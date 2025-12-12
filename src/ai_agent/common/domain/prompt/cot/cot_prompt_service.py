from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol
from ai_agent.common.domain.datasets.value_objects.dataset_types import DatasetType
from ai_agent.common.domain.prompt.cot.prompts_gsm8k import CHAIN_OF_THOUGHT_PROMPT_TEMPLATE_FOR_GSM8K


class CotPromptService(PromptServiceProtocol):
    def __init__(self, dataset_type: DatasetType):
        self.dataset_type = dataset_type

    def get_prompt(self, question: str) -> str:
        if self.dataset_type == DatasetType.GSM8K:
            return CHAIN_OF_THOUGHT_PROMPT_TEMPLATE_FOR_GSM8K.format(question=question)
        else:
            raise ValueError(f"Invalid prompt type: {self.prompt_type}")

