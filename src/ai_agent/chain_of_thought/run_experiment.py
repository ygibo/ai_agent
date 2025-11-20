from typing import Any
from dotenv import load_dotenv  # type: ignore[reportMissingImports]
from ai_agent.chain_of_thought.di import DIContainer
from ai_agent.chain_of_thought.presentation.commands.run_experiment_controller import RunExperimentController


if __name__ == "__main__":
    load_dotenv()
    config_path: str = "config/chain_of_thought/cot_config.yaml"
    di_container: DIContainer = DIContainer(config_path)
    controller: RunExperimentController = di_container.get_experiment_controller()
    result: dict[str, Any] = controller.run()
