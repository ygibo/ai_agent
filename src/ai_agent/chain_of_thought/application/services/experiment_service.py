import random
from ai_agent.chain_of_thought.application.services.experiment_execution_service import ExperimentExecutionService
from ai_agent.common.application.services.llm_client_protocol import LLMClientProtocol
from ai_agent.chain_of_thought.domain.value_objects.dataset_types import DatasetType
from datasets import load_dataset
from ai_agent.chain_of_thought.domain.services.prompt_service import PromptService
from ai_agent.chain_of_thought.domain.value_objects.prompt_type import PromptType

class ExperimentService:
    def __init__(self, llm_client: LLMClientProtocol, sample_size: int):
        self.__llm_client = llm_client
        self.__sample_size = sample_size

    @staticmethod
    def __get_dataset(dataset_type: DatasetType, sample_size: int) -> list[dict]:
        dataset = load_dataset(dataset_type, "main")
        test = dataset["test"]
        samples = random.sample(list(test), k=min(len(test), sample_size))
        return samples

    def run_experiment(self, dataset_type: DatasetType) -> None:
        dataset = self.__get_dataset(dataset_type, self.__sample_size)
        standard_prompt_service = PromptService(dataset_type, PromptType.STANDARD)
        chain_of_thought_prompt_service = PromptService(dataset_type, PromptType.CHAIN_OF_THOUGHT)
        
        print("executing standard experiment")
        standard_result = ExperimentExecutionService(self.__llm_client)
        print("executing chain of thought experiment")
        chain_of_thought_result = ExperimentExecutionService(self.__llm_client)
        print("experiments executed")

        standard_result = standard_result.run_experiment(dataset, standard_prompt_service)
        chain_of_thought_result = chain_of_thought_result.run_experiment(dataset, chain_of_thought_prompt_service)
        
        print(f"Standard result: {standard_result}")
        print(f"Chain of thought result: {chain_of_thought_result}")
