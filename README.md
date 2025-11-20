# AI agent フレームワーク再現実験

現在は以下を行った
- chain of thought (https://arxiv.org/abs/2201.11903)
  gpt4 の場合は standard prompt と CoT prompt で正答率に差はなく gpt3.5 を使用した場合正答率が 42% から 80% と上昇。gsm8k データセットの一部を使用し再現に成功


# 実行方法
- chain of thought
  uv run python -m ai_agent.chain_of_thought.run_experiment
  