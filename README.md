# AI agent フレームワーク再現実験

現在は以下を行った
- chain of thought (https://arxiv.org/abs/2201.11903)
  gpt4 の場合は standard prompt と CoT prompt で正答率に差はなく gpt3.5 を使用した場合正答率が 42% から 80% と上昇。gsm8k データセットの一部を使用し再現に成功
- self consistency (https://arxiv.org/abs/2203.11171)
  gpt3.5 の場合では Self-Consistency を用いても明示的に性能の向上がみられなかった。


# 実行方法
- chain of thought
  - few shot chain of thought prompting
    - uv run python -m ai_agent.chain_of_thought.run_experiment
  - standard prompt
    - uv run python -m ai_agent.chain_of_thought.run_experiment prompt=standard experiment.experiment_name=standard_prompt_gsm8k_small_test
- self consistency
  - sampling 1,5,10
    - uv run python -m ai_agent.self_consistency.run_experiment prompt=few_shot_cot sampling.num_samples_per_query=1,5,10
  