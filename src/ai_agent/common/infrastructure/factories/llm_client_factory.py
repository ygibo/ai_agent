import os
from typing import Optional
from ai_agent.common.application.services.llm_client_protocol import LLMClientProtocol
from ai_agent.common.infrastructure.services.open_ai_client_service import OpenAIClientService
from ai_agent.common.infrastructure.services.lm_studio_client_service import LMStudioClientService


class LLMClientFactory:
    @staticmethod
    def create_llm_client(
        api_type: str,
        base_url: Optional[str],
        api_key: Optional[str],
        model_name: str,
        temperature: float,
        max_tokens: int
    ) -> LLMClientProtocol:
        if api_type == "openai":
            key = api_key or os.environ.get("OPENAI_API_KEY")
            if not key:
                raise ValueError("OPENAI_API_KEY が設定されていません。.env または環境変数で設定してください。")
            return OpenAIClientService(
                key,
                model_name,
                temperature,
                max_tokens
            )
        elif api_type == "lmstudio":
            return LMStudioClientService(
                base_url,
                model_name,
                temperature,
                max_tokens
            )
        else:
            raise ValueError(f"Invalid LLM client type: {api_type}")
