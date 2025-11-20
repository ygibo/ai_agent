from typing import Any
from ai_agent.chain_of_thought.application.services.experiment_service import ExperimentService
from ai_agent.chain_of_thought.presentation.commands.experiemt_config import ExperimentConfig
from ai_agent.common.application.services.experiment_callback import ExperimentCallback


class RunExperimentController:
    def __init__(self, experiment_service: ExperimentService, experiment_config: ExperimentConfig, experiment_callback: ExperimentCallback):
        self.experiment_service = experiment_service
        self.experiment_config = experiment_config
        self.experiment_callback = experiment_callback
    
    def run(self) -> dict[str, Any]:
        result = self.experiment_service.run_experiment(
            self.experiment_config.dataset_type
        )
        return result