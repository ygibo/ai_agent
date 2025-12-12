import os
from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol
from ai_agent.common.domain.ports.value_objects.llm_model_config import LLMModelConfig
from ai_agent.common.infrastructure.services.open_ai_client_service import OpenAIClientService
from ai_agent.common.infrastructure.services.lm_studio_client_service import LMStudioClientService


def create_llm_client(
    model_config: LLMModelConfig
) -> LLMClientProtocol:
    if model_config.api_type == "openai":
        key = model_config.api_key or os.environ.get("OPENAI_API_KEY")
        if not key:
            raise ValueError("OPENAI_API_KEY が設定されていません。.env または環境変数で設定してください。")
        return OpenAIClientService(
            key,
            model_config.model_name,
            model_config.max_tokens
        )
    elif model_config.api_type == "lmstudio":
        return LMStudioClientService(
            model_config.base_url,
            model_config.model_name,
            model_config.max_tokens
        )
    else:
        raise ValueError(f"Invalid LLM client type: {model_config.api_type}")
