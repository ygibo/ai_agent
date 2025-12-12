from ai_agent.common.domain.task.value_objects.task_config import TaskConfig
from ai_agent.common.domain.task.task_protocol import TaskProtocol
from ai_agent.common.domain.task.gsm8k_task import GSM8KTask
from ai_agent.common.domain.prompt.prompt_service_protocol import PromptServiceProtocol


def create_task_protocol(
    task_config: TaskConfig,
    prompt_service: PromptServiceProtocol
) -> TaskProtocol:
    if task_config.task_name == "gsm8k":
        return GSM8KTask(
            prompt_service=prompt_service
        )
    else:
        raise ValueError(f"Invalid task: {task_config.task_name}")