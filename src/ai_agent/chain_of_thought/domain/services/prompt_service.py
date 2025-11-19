from ai_agent.chain_of_thought.domain.value_objects.dataset_types import DatasetType
from ai_agent.chain_of_thought.domain.value_objects.prompt_type import PromptType
from ai_agent.chain_of_thought.domain.value_objects.prompts import CHAIN_OF_THOUGHT_PROMPT_TEMPLATE, STANDARD_PROMPT_TEMPLATE


class PromptService:
    def __init__(self, dataset_type: DatasetType, prompt_type: PromptType):
        self.dataset_type = dataset_type
        self.prompt_type = prompt_type

    def get_prompt(self, question: str) -> str:
        if self.prompt_type == PromptType.CHAIN_OF_THOUGHT:
            return CHAIN_OF_THOUGHT_PROMPT_TEMPLATE.format(question=question)
        else:
            return STANDARD_PROMPT_TEMPLATE.format(question=question)
