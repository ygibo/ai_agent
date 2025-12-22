from dataclasses import dataclass
from ai_agent.common.domain.prompt.value_objects.prompt_type import PromptType

@dataclass
class PromptConfig:
    prompt_name: str
    version: str

    def get_prompt_type(self) -> PromptType:
        return PromptType.from_str(self.prompt_name)

    