from dataclasses import dataclass
from ai_agent.common.domain.datasets.value_objects.dataset_types import DatasetType


@dataclass
class DatasetConfig:
    dataset_name: str
    max_samples: int
    use_all_samples: bool

    def get_dataset_type(self) -> DatasetType:
        return DatasetType.from_str(self.dataset_name)