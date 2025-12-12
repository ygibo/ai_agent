from typing import Any
from ai_agent.common.application.services.reasoning_experiment_service import ReasoningExperimentService


class RunReasoningExperimentBase:
    def __init__(self, experiment_service: ReasoningExperimentService):
        self.experiment_service = experiment_service
   
    def run(self) -> dict[str, Any]:
        result = self.experiment_service.run_experiment()
        return result