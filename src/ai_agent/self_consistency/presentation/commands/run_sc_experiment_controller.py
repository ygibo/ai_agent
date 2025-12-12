from typing import Any
from ai_agent.common.application.services.reasoning_experiment_service import ReasoningExperimentService
from ai_agent.common.presentation.commands.run_reasoning_experiment_base import RunReasoningExperimentBase

class RunScExperimentController(RunReasoningExperimentBase):
    def __init__(self, reasoning_experiment_service: ReasoningExperimentService):
        super().__init__(reasoning_experiment_service)