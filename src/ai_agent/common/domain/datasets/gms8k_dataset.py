from ai_agent.common.domain.datasets.value_objects.dataset_config import DatasetConfig
from datasets import load_dataset
import random
from collections.abc import Iterator
from ai_agent.common.domain.datasets.dataset_protocol import DatasetProtocol


class Gsm8kDataset(DatasetProtocol):
    def __init__(self, dataset_config: DatasetConfig):
        self.__dataset = load_dataset("gsm8k", "main")
        self.__test = self.__dataset["test"]
        if dataset_config.use_all_samples:
            self.__samples = list(self.__test)
        else:
            self.__samples = random.sample(list(self.__test), k=min(len(self.__test), dataset_config.max_samples))

    def __iter__(self) -> Iterator[dict]:
        for sample in self.__samples:
            yield sample

    def __len__(self) -> int:
        return len(self.__samples)