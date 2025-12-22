from ai_agent.common.domain.datasets.dataset_protocol import DatasetProtocol
from ai_agent.common.domain.reasoning_algorithms.reasoning_algorithm_protocol import ReasoningAlgorithmProtocol
from ai_agent.common.domain.task.task_protocol import TaskProtocol
from ai_agent.common.application.services.experiment_callback import ExperimentCallback
from ai_agent.common.domain.reasoning_algorithms.value_objects.reasoning_result import ReasoningResult
from ai_agent.common.domain.experiments.value_objects.experiment_config import ExperimentConfig


class ReasoningExperimentService:
    def __init__(
        self,
        experiment_config: ExperimentConfig,
        dataset: DatasetProtocol,
        reasoning_algorithm: ReasoningAlgorithmProtocol,
        task_protocol: TaskProtocol,
        experiment_callback: ExperimentCallback,
    ):
        self.__dataset: DatasetProtocol = dataset
        self.__experiment_config: ExperimentConfig = experiment_config
        self.__reasoning_algorithm: ReasoningAlgorithmProtocol = reasoning_algorithm
        self.__task_protocol: TaskProtocol = task_protocol
        self.__experiment_callback: ExperimentCallback = experiment_callback
    
    def __run_experiment(self) -> None:
        self.__experiment_callback.on_experiment_start({
            "experiment_name": self.__experiment_config.experiment_name,
            "dataset_name": self.__experiment_config.dataset_name
        })
        
        results = []

        for idx, item in enumerate[tuple[str, str]](self.__dataset):
            self.__experiment_callback.on_iteration_start(idx, item)
            question = item["question"]
            ground_truth = self.__task_protocol.extract_answer_from_ground_truth(item["answer"])
            system_prompt = self.__task_protocol.build_system_prompt(question, context=None)
            user_prompt = self.__task_protocol.build_user_prompt(question, context=None)

            self.__experiment_callback.on_llm_request(idx, system_prompt, user_prompt)
            reasoning_result: ReasoningResult = self.__reasoning_algorithm.infer_answer(system_prompt, user_prompt)
            self.__experiment_callback.on_llm_response(idx, reasoning_result.messages)
            
            answer = reasoning_result.final_answer
            is_correct = self.__task_protocol.is_correct(answer, ground_truth)
            if is_correct:
                results.append(True)
            else:
                results.append(False)

            self.__experiment_callback.on_iteration_end(idx, {
                "answer": answer,
                "ground_truth": ground_truth,
                "is_correct": is_correct
            })
        
        result = {
            "accuracy": sum(results) / len(results),
            "sample_size": len(results),
            "correct_count": sum(results),
            "incorrect_count": len(results) - sum(results)
        }

        self.__experiment_callback.on_experiment_end({
            "result": result
        })

        return result

    def run_experiment(self) -> None:
        #try:
        return self.__run_experiment()
        #except Exception as e:
        #    self.__experiment_callback.on_error(e)
        #    raise e