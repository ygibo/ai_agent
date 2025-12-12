from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol
from typing import Optional
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
from ai_agent.common.domain.sampling.sampling_protocol import SamplingMethodProtocol


class GreedySamplingMethod(SamplingMethodProtocol):
    def __init__(
        self,
        temperature: float,
        llm_client: LLMClientProtocol
    ):
        self.__temperature = temperature
        self.__llm_client = llm_client
    
    def sample(self, system_prompt: Optional[str], messages: list[ChatMessage]) -> list[ChatMessage]:
        self.__llm_client.change_parameters(
            temperature=self.__temperature,
            max_tokens=None,
            top_p=1.0,
            num_samples_per_query=1
        )
        results = self.__llm_client.generate_text(system_prompt, messages)
        return [results[0]] if results is not None and len(results) > 0 else []
