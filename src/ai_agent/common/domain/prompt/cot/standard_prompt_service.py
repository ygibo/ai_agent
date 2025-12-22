from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol
from ai_agent.common.domain.datasets.value_objects.dataset_types import DatasetType
from ai_agent.common.domain.prompt.cot.standard_prompts_gsm8k import STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V1, STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V2, STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V3, STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V4
from typing import Optional


class StandardPromptService(PromptServiceProtocol):
    def __init__(self, dataset_type: DatasetType, version: str):
        self.dataset_type = dataset_type
        self.version = version

    def __get_system_prompt_for_gsm8k(self, question: str) -> str:
        if self.version == "v1":
            return None
        elif self.version == "v2":
            return None
        elif self.version == "v3":
            return STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V3
        elif self.version == "v4":
            return STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V4
        else:
            raise ValueError(f"Invalid version: {self.version}")

    def get_system_prompt(self, question: str, context: Optional[dict]) -> str:
        if self.dataset_type == DatasetType.GSM8K:
            return self.__get_system_prompt_for_gsm8k(question)
        else:
            raise ValueError(f"Invalid dataset type: {self.dataset_type}")

    def get_user_prompt(self, question: str, context: Optional[dict]) -> str:
        if self.version == "v1":
            return STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V1.format(question=question)
        elif self.version == "v2":
            return STANDARD_PROMPT_TEMPLATE_FOR_GSM8K_V2.format(question=question)
        elif self.version == "v3" or self.version == "v4":
            return f"Q: {question}\nA: "
        else:
            raise ValueError(f"Invalid version: {self.version}")
