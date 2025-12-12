
from dataclasses import dataclass


@dataclass
class SamplingConfig:
    sampling_method_name: str
    temperature: float
    top_p: float
    num_samples_per_query: int
    