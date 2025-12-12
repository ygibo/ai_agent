from ai_agent.common.presentation.commands.run_reasoning_experiment_base import RunReasoningExperimentBase
from ai_agent.common.application.services.reasoning_experiment_service import ReasoningExperimentService


class RunCotExperimentController(RunReasoningExperimentBase):
    def __init__(self, reasoning_experiment_service: ReasoningExperimentService):
        super().__init__(reasoning_experiment_service)