from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol
from ai_agent.common.domain.datasets.value_objects.dataset_types import DatasetType
from ai_agent.common.domain.prompt.cot.cot_prompts_gsm8k import CHAIN_OF_THOUGHT_PROMPT_TEMPLATE_FOR_GSM8K_V1, CHAIN_OF_THOUGHT_PROMPT_TEMPLATE_FOR_GSM8K_V2
from typing import Optional


class CotPromptService(PromptServiceProtocol):
    def __init__(self, dataset_type: DatasetType, version: str):
        self.dataset_type = dataset_type
        self.version = version

    def __get_system_prompt_for_gsm8k(self, question: str) -> str:
        if self.version == "v1":
            # v1 の場合は user_message に CoT のプロンプトを追加する
            return None
        elif self.version == "v2":
            # v2 の場合は system_prompt に CoT のプロンプトを追加する
            return CHAIN_OF_THOUGHT_PROMPT_TEMPLATE_FOR_GSM8K_V2
        else:
            raise ValueError(f"Invalid version: {self.version}")

    def get_system_prompt(self, question: str, context: Optional[dict]) -> str:
        if self.dataset_type == DatasetType.GSM8K:
            return self.__get_system_prompt_for_gsm8k(question)
        else:
            raise ValueError(f"Invalid prompt type: {self.prompt_type}")

    def get_user_prompt(self, question: str, context: Optional[dict]) -> str:
        if self.version == "v1":
            return CHAIN_OF_THOUGHT_PROMPT_TEMPLATE_FOR_GSM8K_V1.format(question=question)
        elif self.version == "v2":
            return f"Q: {question}\nA: "
        else:
            raise ValueError(f"Invalid version: {self.__version}")
