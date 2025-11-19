from enum import Enum

class PromptType(Enum):
    CHAIN_OF_THOUGHT = "chain_of_thought" # CoT 方式のプロンプト
    STANDARD = "standard" # 標準的なプロンプト