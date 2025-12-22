from ai_agent.common.application.services.experiment_callback import ExperimentCallback
from typing import Any, Optional
from ai_agent.common.domain.chat.value_objects.chat_message import ChatMessage
import uuid
import datetime
import json
import logging
logger = logging.getLogger("experiment")


class ScExperimentCallback(ExperimentCallback):
    def __init__(
        self,
        experiment_id: Optional[str] = None,
        is_debug: bool = False
    ):
        self.__experiment_id = experiment_id if experiment_id is not None else str(uuid.uuid4())
        self.__is_debug = is_debug # デバッグオンの場合は llm のリクエストとレスポンスを出力、イテレーションごとの結果を出力

    def __get_timestamp(self) -> str:
        # ISO 8601 形式で返す
        return datetime.datetime.now().isoformat()

    def on_experiment_start(self, config: dict[str, Any]) -> None:
        json_Log = {
            "event": "experiment_start",
            "experiment_id": self.__experiment_id,
            "timestamp": self.__get_timestamp(),
            "config": config
        }
        logger.info(json.dumps(json_Log, indent=4))

    def on_experiment_end(self, summary: dict[str, Any]) -> None:
        json_Log = {
            "event": "experiment_end",
            "experiment_id": self.__experiment_id,
            "timestamp": self.__get_timestamp(),
            "summary": summary
        }
        logger.info(json.dumps(json_Log, indent=4))

    def on_iteration_start(self, index: int, sample: dict[str, Any]) -> None:
        json_Log = {
            "event": "iteration_start",
            "experiment_id": self.__experiment_id,
            "timestamp": self.__get_timestamp(),
            "index": index,
            "sample": sample
        }
        logger.info(json.dumps(json_Log, indent=4))

    def on_llm_request(self, index: int, system_prompt: Optional[str], question: str) -> None:
        if self.__is_debug:
            json_Log = {
                "event": "llm_request",
                "experiment_id": self.__experiment_id,
                "timestamp": self.__get_timestamp(),
                "index": index,
                "system_prompt": system_prompt,
                "question": question
            }
            logger.info(json.dumps(json_Log, indent=4))

    def on_llm_response(self, index: int, messages: list[ChatMessage]) -> None:
        if self.__is_debug:
            json_Log = {
                "event": "llm_response",
                "experiment_id": self.__experiment_id,
                "timestamp": self.__get_timestamp(),
                "index": index,
                "messages": [message.model_dump(mode="json") for message in messages]
            }
            logger.info(json.dumps(json_Log, indent=4))
            
    def on_iteration_end(self, index: int, result: dict[str, Any]) -> None:
        json_Log = {
            "event": "iteration_end",
            "experiment_id": self.__experiment_id,
            "timestamp": self.__get_timestamp(),
            "index": index,
            "result": result
        }
        logger.info(json.dumps(json_Log, indent=4))
            
    def on_error(self, index: Optional[int], exc: Exception) -> None:
        json_Log = {
            "event": "error",
            "experiment_id": self.__experiment_id,
            "timestamp": self.__get_timestamp(),
            "index": index,
            "error": str(exc)
        }
        logger.info(json.dumps(json_Log, indent=4))

    def on_experiment_result(self, result: dict[str, Any]) -> None:
        json_Log = {
            "event": "experiment_result",
            "experiment_id": self.__experiment_id,
            "timestamp": self.__get_timestamp(),
            "result": result
        }
        logger.info(json.dumps(json_Log, indent=4))