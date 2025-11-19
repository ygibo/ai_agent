import yaml
import os
from dataclasses import dataclass


@dataclass
class ExperimentConfig:
    experiment_type: str
    dataset_type: str
    sample_size: int
    model_name: str
    api_type: str
    base_url: str
    api_key: str
    temperature: float
    max_tokens: int

def load_experiment_config(config_path: str) -> ExperimentConfig:
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    config = ExperimentConfig(
        experiment_type=config['experiment']['experiment_type'],
        dataset_type=config['experiment']['dataset_type'],
        sample_size=config['experiment']['sample_size'],
        model_name=config['model']['model_name'],
        api_type=config['model']['api_type'],
        base_url=config['model']['base_url'] if 'base_url' in config['model'] else None,
        api_key=config['model']['api_key'] if 'api_key' in config['model'] else None,
        temperature=config['model']['temperature'],
        max_tokens=config['model']['max_tokens'],
    )
    if config.api_type == "openai" and not config.api_key:
        config.api_key = os.environ.get("OPENAI_API_KEY") if config.api_key is None else config.api_key
    if config.api_type == "openai" and not config.api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    if config.api_type == "lmstudio" and not config.base_url:
        raise ValueError("LMSTUDIO_BASE_URL is not set")
    return config