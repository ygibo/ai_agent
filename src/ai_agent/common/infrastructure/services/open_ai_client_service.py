from langchain_core.outputs import ChatGeneration, ChatResult, LLMResult
from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.chat.value_objects.chat_role import ChatRole
from typing import Optional


class OpenAIClientService(LLMClientProtocol):
    def __init__(
        self, 
        api_key: str,
        model_name: str,
        max_tokens: int
    ):
        self.__client = ChatOpenAI(
            api_key=api_key,
            model=model_name,
            max_tokens=max_tokens
        )
        self.__max_tokens = max_tokens

    def change_parameters(
        self,
        temperature: Optional[float],
        max_tokens: Optional[int],
        top_p: Optional[float],
        num_samples_per_query: Optional[int]
    ) -> None:
        if temperature:
            self.__client.temperature = temperature
        if max_tokens:
            self.__client.max_tokens = max_tokens
        if top_p:
            self.__client.top_p = top_p
        if num_samples_per_query:
            self.__client.n = num_samples_per_query
        
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

    def generate_text(self, system_prompt: Optional[str], messages: list[ChatMessage]) -> list[ChatMessage]:
        __messages = self.__to_messages(system_prompt, messages)
        try:
            response: LLMResult = self.__client.generate([__messages])
            results: list[ChatMessage] = []
            for gen in response.generations[0]:
                ai_msg: AIMessage = gen.message
                if ai_msg.tool_calls:
                    for tool_call in ai_msg.tool_calls:
                        # TODO: 必要になったら実装する
                        # tool_call は TypedDict:
                        #   name: str, args: dict[str, Any], id: str | None
                        raise NotImplementedError("Tool calls are not supported yet")
                        # 例えば:
                        #results.append(
                        #    ChatMessage(
                        #        role=ChatRole.TOOL,
                        #        content=tool_call["name"],
                        #    )
                        #)
                else:
                    results.append(
                        ChatMessage(
                            role=ChatRole.ASSISTANT,
                            content=ai_msg.content
                        )
                    )
            return results
        except Exception as e:
            raise ValueError(f"Failed to generate text: {e}")