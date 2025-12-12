from dataclasses import dataclass
from typing import Optional

@dataclass
class LLMModelConfig:
    api_type: str
    model_name: str
    max_tokens: int
    api_key: Optional[str] = None