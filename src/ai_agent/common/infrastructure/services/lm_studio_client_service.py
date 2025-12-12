from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol
try:
    from langchain_openai import ChatOpenAI  # type: ignore[reportMissingImports]
except Exception:
    ChatOpenAI = None  # type: ignore[assignment]
try:
    from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  # type: ignore[reportMissingImports]
except Exception:
    SystemMessage = HumanMessage = AIMessage = None  # type: ignore[assignment]
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.chat.value_objects.chat_role import ChatRole
from typing import Optional


class LMStudioClientService(LLMClientProtocol):
    def __init__(self, base_url: str, model_name: str, temperature: float, max_tokens: int):
        if ChatOpenAI is None or SystemMessage is None or HumanMessage is None or AIMessage is None:
            raise ImportError("LangChain 関連の依存が解決できません。`uv sync` もしくは `uv add langchain langchain-openai` を実行してください。")
        self.__model_name = model_name
        self.__temperature = temperature
        self.__max_tokens = max_tokens
        self.__client = ChatOpenAI(
            base_url=base_url,
            api_key="not-needed",
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    def __to_messages(self, system_prompt: Optional[str], messages: list[ChatMessage]):
        lc_messages = []
        if system_prompt:
            lc_messages.append(SystemMessage(content=system_prompt))

        for m in messages:
            if m.role == ChatRole.USER:
                lc_messages.append(HumanMessage(content=m.content))
            elif m.role == ChatRole.ASSISTANT:
                lc_messages.append(AIMessage(content=m.content))
            else:
                lc_messages.append(SystemMessage(content=m.content))
        return lc_messages

    def generate_text(self, system_prompt: str, messages: list[ChatMessage]) -> ChatMessage:
        try:
            result = self.__client.invoke(self.__to_messages(system_prompt, messages))
            return ChatMessage(role=ChatRole.ASSISTANT, content=result.content)
        except Exception as e:
            raise ValueError(f"Failed to generate text: {e}") from e