from ai_agent.chain_of_thought.presentation.commands.run_experiment_controller import RunExperimentController
from ai_agent.chain_of_thought.application.services.experiment_service import ExperimentService
from ai_agent.common.infrastructure.factories.llm_client_factory import LLMClientFactory
from ai_agent.common.application.services.llm_client_protocol import LLMClientProtocol
from ai_agent.chain_of_thought.presentation.commands.experiemt_config import ExperimentConfig, load_experiment_config


class DIContainer:
    def __init__(self, config_path: str):
        self.experiment_config: ExperimentConfig = load_experiment_config(config_path)
    
    def get_experiment_controller(self) -> RunExperimentController:
        llm_client: LLMClientProtocol = LLMClientFactory.create_llm_client(
            self.experiment_config.api_type,
            self.experiment_config.base_url,
            self.experiment_config.api_key,
            self.experiment_config.model_name,
            self.experiment_config.temperature,
            self.experiment_config.max_tokens
        )
        experiment_service: ExperimentService = ExperimentService(
            llm_client,
            self.experiment_config.sample_size
        )
        return RunExperimentController(experiment_service, self.experiment_config)

