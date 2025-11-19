from ai_agent.common.application.services.llm_client_protocol import LLMClientProtocol
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from ai_agent.common.domain.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.value_objects.chat_role import ChatRole
from typing import Optional


class OpenAIClientService(LLMClientProtocol):
    def __init__(self, api_key: str, model_name: str, temperature: float, max_tokens: int):
        self.__client = ChatOpenAI(
            api_key=api_key,
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )

    def __to_messages(self, system_prompt: Optional[str], messages: list[ChatMessage]) -> list[dict[str, str]]:
        __messages = []

        if system_prompt:
            __messages.append(SystemMessage(content=system_prompt))

        for message in messages:
            if message.role == ChatRole.USER:
                __messages.append(HumanMessage(content=message.content))
            elif message.role == ChatRole.ASSISTANT:
                __messages.append(AIMessage(content=message.content))
            elif message.role == ChatRole.TOOL:
                __messages.append(ToolMessage(content=message.content))
            else:
                raise ValueError(f"Invalid message role: {message.role}")
        return __messages

    def generate_text(self, system_prompt: str, messages: list[ChatMessage]) -> ChatMessage:
        __messages = self.__to_messages(system_prompt, messages)
        try:
            response = self.__client.invoke(__messages)
            return ChatMessage(
                role=ChatRole.ASSISTANT,
                content=response.content
            )
        except Exception as e:
            raise ValueError(f"Failed to generate text: {e}")