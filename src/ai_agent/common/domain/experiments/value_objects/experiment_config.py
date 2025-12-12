from dataclasses import dataclass


@dataclass
class ExperimentConfig:
  experiment_name: str
  dataset_name: str