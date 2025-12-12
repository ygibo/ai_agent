from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol
from ai_agent.common.domain.sampling.sampling_protocol import SamplingMethodProtocol
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
from typing import Optional


class TopPSamplingMethod(SamplingMethodProtocol):
    def __init__(
        self,
        top_p: float,
        temperature: float,
        num_samples_per_query: int,
        llm_client: LLMClientProtocol
    ):
        self.__top_p = top_p
        self.__temperature = temperature
        self.__num_samples_per_query = num_samples_per_query
        self.__llm_client = llm_client

    def sample(self, system_prompt: Optional[str], messages: list[ChatMessage]) -> list[ChatMessage]:
        self.__llm_client.change_parameters(
            temperature=self.__temperature,
            max_tokens=None,
            top_p=self.__top_p,
            num_samples_per_query=self.__num_samples_per_query
        )
        return self.__llm_client.generate_text(system_prompt, messages)

