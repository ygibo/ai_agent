import random
from ai_agent.chain_of_thought.application.services.experiment_execution_service import ExperimentExecutionService
from ai_agent.common.domain.services.llm_client_protocol import LLMClientProtocol
from ai_agent.chain_of_thought.domain.value_objects.dataset_types import DatasetType
from datasets import load_dataset
from ai_agent.chain_of_thought.domain.services.prompt_service import PromptService
from ai_agent.chain_of_thought.domain.value_objects.prompt_type import PromptType
from ai_agent.common.application.services.experiment_callback import ExperimentCallback

class ExperimentService:
    def __init__(self, llm_client: LLMClientProtocol, sample_size: int, experiment_callback: ExperimentCallback):
        self.__llm_client = llm_client
        self.__sample_size = sample_size
        self.__experiment_callback = experiment_callback

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
        
        standard_result = ExperimentExecutionService(self.__llm_client)
        chain_of_thought_result = ExperimentExecutionService(self.__llm_client)
        
        # standard experiment
        self.__experiment_callback.on_experiment_start({
            "experiment_type": "standard",
            "dataset_type": dataset_type,
            "sample_size": self.__sample_size
        })
        standard_result = standard_result.run_experiment(dataset, standard_prompt_service, self.__experiment_callback)
        self.__experiment_callback.on_experiment_end({
            "experiment_type": "standard",
            "dataset_type": dataset_type,
            "sample_size": self.__sample_size,
            "result": standard_result
        })

        # chain of thought experiment
        self.__experiment_callback.on_experiment_start({
            "experiment_type": "chain_of_thought",
            "dataset_type": dataset_type,
            "sample_size": self.__sample_size
        })
        chain_of_thought_result = chain_of_thought_result.run_experiment(dataset, chain_of_thought_prompt_service, self.__experiment_callback)
        self.__experiment_callback.on_experiment_end({
            "experiment_type": "chain_of_thought",
            "dataset_type": dataset_type,
            "sample_size": self.__sample_size,
            "result": chain_of_thought_result
        })

        self.__experiment_callback.on_experiment_result({
            "standard_result": standard_result,
            "chain_of_thought_result": chain_of_thought_result
        })
