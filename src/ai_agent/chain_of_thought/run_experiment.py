import hydra
from omegaconf import DictConfig
from dotenv import load_dotenv  # type: ignore[reportMissingImports]
from ai_agent.chain_of_thought.di import build_cot_experiment_controller
from ai_agent.common.presentation.commands.run_reasoning_experiment_base import RunReasoningExperimentBase


@hydra.main(
    config_path="../../../config/chain_of_thought",
    config_name="config.yaml",
    version_base=None
)
def main(cfg: DictConfig):
    controller: RunReasoningExperimentBase = build_cot_experiment_controller(cfg)
    _: dict[str, str] = controller.run()


if __name__ == "__main__":
    load_dotenv()
    main()