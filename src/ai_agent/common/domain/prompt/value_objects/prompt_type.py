from enum import Enum

class PromptType(Enum):
    FEW_SHOT_CHAIN_OF_THOUGHT = "few_shot_cot" # Few-shot CoT 方式のプロンプト
    ZERO_SHOT_CHAIN_OF_THOUGHT = "zero_shot_cot" # Zero-shot CoT 方式のプロンプト
    STANDARD = "standard" # 標準的なプロンプト

    @classmethod
    def from_str(cls, value: str) -> "PromptType":
        try:
            normalized = value.lower().strip()
            return cls(normalized)
        except Exception as e:
            raise ValueError(f"Invalid prompt type: {value}")