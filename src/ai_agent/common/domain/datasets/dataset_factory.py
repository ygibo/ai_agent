from ai_agent.common.domain.datasets.dataset_protocol import DatasetProtocol
from ai_agent.common.domain.datasets.value_objects.dataset_config import DatasetConfig
from ai_agent.common.domain.datasets.gms8k_dataset import Gsm8kDataset

def create_dataset(
    dataset_config: DatasetConfig
) -> DatasetProtocol:
    if dataset_config.dataset_name == "gsm8k":
        return Gsm8kDataset(dataset_config)
    else:
        raise ValueError(f"Invalid dataset: {dataset_config.dataset_name}")