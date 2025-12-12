from omegaconf import DictConfig
from ai_agent.self_consistency.presentation.commands.run_sc_experiment_controller import RunScExperimentController
from ai_agent.common.application.services.reasoning_experiment_service import ReasoningExperimentService
from ai_agent.common.application.services.experiment_callback import ExperimentCallback
from ai_agent.self_consistency.infrastructure.services.sc_experiment_callback import ScExperimentCallback
from ai_agent.common.di.reasoning_di import build_reasoning_experiment_service
from ai_agent.common.presentation.commands.run_reasoning_experiment_base import RunReasoningExperimentBase


def build_sc_experiment_controller(
    cfg: DictConfig
) -> RunReasoningExperimentBase:
    experiment_callback: ExperimentCallback = ScExperimentCallback(
        experiment_id=None,
        is_debug=True
    )
    reasoning_experiment_service: ReasoningExperimentService = build_reasoning_experiment_service(
        cfg,
        experiment_callback
    )
    return RunScExperimentController(reasoning_experiment_service)
