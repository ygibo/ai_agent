from omegaconf import DictConfig
from ai_agent.self_consistency.presentation.commands.run_sc_experiment_controller import RunScExperimentController
from ai_agent.common.application.services.reasoning_experiment_service import ReasoningExperimentService
from ai_agent.common.infrastructure.factories.llm_client_factory import create_llm_client
from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol
from ai_agent.common.application.services.experiment_callback import ExperimentCallback
from ai_agent.self_consistency.infrastructure.services.sc_experiment_callback import ScExperimentCallback

# Sampling
from ai_agent.common.domain.sampling.value_objects.sampling_config import SamplingConfig
from ai_agent.common.domain.sampling.sampling_factory import create_sampling_method
from ai_agent.common.domain.sampling.sampling_protocol import SamplingMethodProtocol
# Aggregation
from ai_agent.common.domain.aggregation.aggregation_factory import create_aggregation_method
from ai_agent.common.domain.aggregation.aggregation_protocol import AggregationMethodProtocol
from ai_agent.common.domain.aggregation.value_objects.aggregation_config import AggregationConfig
# Reasoning Algorithm
from ai_agent.common.domain.reasoning_algorithms.reasoning_algorithm_factory import create_reasoning_algorithm
from ai_agent.common.domain.reasoning_algorithms.value_objects.reasoning_algorithm_config import ReasoningAlgorithmConfig
from ai_agent.common.domain.reasoning_algorithms.reasoning_algorithm_protocol import ReasoningAlgorithmProtocol
# LLM Client
from ai_agent.common.domain.ports.value_objects.llm_model_config import LLMModelConfig
from ai_agent.common.infrastructure.factories.llm_client_factory import create_llm_client
from ai_agent.common.domain.ports.llm_client_protocol import LLMClientProtocol
# Task
from ai_agent.common.domain.task.task_factory import create_task_protocol
from ai_agent.common.domain.task.task_protocol import TaskProtocol
from ai_agent.common.domain.task.value_objects.task_config import TaskConfig
# Prompt Service
from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol
from ai_agent.common.domain.prompt.prompt_service_factory import create_prompt_service
from ai_agent.common.domain.prompt.value_objects.prompt_config import PromptConfig
# Dataset
from ai_agent.common.domain.datasets.dataset_protocol import DatasetProtocol
from ai_agent.common.domain.datasets.dataset_factory import create_dataset
from ai_agent.common.domain.datasets.value_objects.dataset_config import DatasetConfig
# Experiment
from ai_agent.common.domain.experiments.value_objects.experiment_config import ExperimentConfig
from ai_agent.common.application.services.reasoning_experiment_service import ReasoningExperimentService


### Build functions
def build_dataset(
    cfg: DictConfig
) -> DatasetProtocol:
    dataset_config = DatasetConfig(
        dataset_name=cfg.dataset.dataset_name,
        max_samples=cfg.dataset.max_samples,
        use_all_samples=cfg.dataset.use_all_samples
    )
    return create_dataset(dataset_config)

def build_llm_client(
    cfg: DictConfig
) -> LLMClientProtocol:
    llm_model_config = LLMModelConfig(
        api_type=cfg.model.api_type,
        model_name=cfg.model.model_name,
        max_tokens=cfg.model.max_tokens,
        api_key=cfg.model.api_key if "api_key" in cfg.model else None
    )
    return create_llm_client(llm_model_config)

def build_sampling_method(
    cfg: DictConfig,
    llm_client: LLMClientProtocol
) -> SamplingMethodProtocol:
    sampling_config = SamplingConfig(
        sampling_method_name=cfg.sampling.sampling_method_name,
        temperature=cfg.sampling.temperature,
        top_p=cfg.sampling.top_p,
        num_samples_per_query=cfg.sampling.num_samples_per_query
    )
    return create_sampling_method(sampling_config, llm_client)

def build_aggregation_method(
    cfg: DictConfig
) -> AggregationMethodProtocol:
    aggregation_config = AggregationConfig(
        aggregation_method_name=cfg.aggregation.aggregation_method_name,
    )
    return create_aggregation_method(aggregation_config)

def build_prompt_service(
    cfg: DictConfig
) -> PromptServiceProtocol:
    prompt_config = PromptConfig(
        prompt_name=cfg.prompt.prompt_name
    )
    dataset_config = DatasetConfig(
        dataset_name=cfg.dataset.dataset_name,
        max_samples=cfg.dataset.max_samples,
        use_all_samples=cfg.dataset.use_all_samples
    )
    return create_prompt_service(prompt_config, dataset_config)

def build_task_protocol(
    cfg: DictConfig
) -> TaskProtocol:
    prompt_service = build_prompt_service(cfg)
    task_config = TaskConfig(
        task_name=cfg.task.task_name
    )
    return create_task_protocol(task_config, prompt_service)

def build_reasoning_algorithm(
    cfg: DictConfig
) -> ReasoningAlgorithmProtocol:
    llm_client = build_llm_client(cfg)
    sampling_method = build_sampling_method(cfg, llm_client)
    aggregation_method = build_aggregation_method(cfg)
    task_protocol = build_task_protocol(cfg)

    reasoning_algorithm_config = ReasoningAlgorithmConfig(
        reasoning_algorithm_name=cfg.reasoning_algorithm.reasoning_algorithm_name
    )
    return create_reasoning_algorithm(reasoning_algorithm_config, sampling_method, aggregation_method, task_protocol)

def build_reasoning_experiment_service(
    cfg: DictConfig,
    experiment_callback: ExperimentCallback
) -> ReasoningExperimentService:
    dataset = build_dataset(cfg)
    reasoning_algorithm = build_reasoning_algorithm(cfg)
    task_protocol = build_task_protocol(cfg)
    experiment_config = ExperimentConfig(
        experiment_name=cfg.experiment.experiment_name,
        dataset_name=cfg.dataset.dataset_name
    )
    return ReasoningExperimentService(
        experiment_config,
        dataset,
        reasoning_algorithm,
        task_protocol,
        experiment_callback
    )
