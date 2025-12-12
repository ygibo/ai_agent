from omegaconf import DictConfig
from ai_agent.common.presentation.commands.run_reasoning_experiment_base import RunReasoningExperimentBase
from ai_agent.chain_of_thought.presentation.commands.run_cot_experiment_controller import RunCotExperimentController
from ai_agent.common.application.services.reasoning_experiment_service import ReasoningExperimentService
from ai_agent.chain_of_thought.infrastructure.services.cot_experiment_callback import CotExperimentCallback
from ai_agent.common.application.services.experiment_callback import ExperimentCallback
from ai_agent.common.di.reasoning_di import build_reasoning_experiment_service


def build_cot_experiment_controller(
    cfg: DictConfig
) -> RunReasoningExperimentBase:
    experiment_callback: ExperimentCallback = CotExperimentCallback(
        experiment_id=None,
        is_debug=True
    )
    reasoning_experiment_service: ReasoningExperimentService = build_reasoning_experiment_service(cfg, experiment_callback)
    return RunCotExperimentController(reasoning_experiment_service)
