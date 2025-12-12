from typing import Protocol

class PromptServiceProtocol(Protocol):
    def get_prompt(self, question: str) -> str: ...