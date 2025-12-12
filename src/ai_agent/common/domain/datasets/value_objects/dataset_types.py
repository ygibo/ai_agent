from enum import Enum


# データセットのタイプ
class DatasetType(Enum):
    GSM8K = "gsm8k"

    @classmethod
    def from_str(cls, value: str) -> "DatasetType":
        try:
            normalized = value.lower().strip()
            if normalized == cls.GSM8K.value:
                return cls.GSM8K
        except Exception as e:
            raise ValueError(f"Invalid dataset type: {value}")

    