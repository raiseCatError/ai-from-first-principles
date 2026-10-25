# Suggested original papers (in order, not all immediately)

Use papers to answer an implementation question, not as a reading-only competition.

| When | Paper | Read with question |
|---|---|---|
| 25–28 | [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762) | Why do Q/K/V and causal masks work? |
| 28–32 | [GPT-2: Language Models are Unsupervised Multitask Learners (2019)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | How is decoder-only LM training framed? |
| 29 | [Decoupled Weight Decay Regularization (2017)](https://arxiv.org/abs/1711.05101) | Why AdamW vs naive L2 in Adam? |
| 35–36 | [Human-level control through deep reinforcement learning (2015)](https://www.nature.com/articles/nature14236) | Which engineering choices stabilize Q-learning? |
| 39 | [Proximal Policy Optimization Algorithms (2017)](https://arxiv.org/abs/1707.06347) | What does policy clipping constrain? |
| 43 | [Direct Preference Optimization (2023)](https://arxiv.org/abs/2305.18290) | What is optimized without an explicit reward-model training loop? |

## Paper notes template

- Claim made by authors:
- What assumptions are hidden in the setup?
- Which equations define the actual learning objective?
- What do I need to implement to test it?
- What baseline would falsify the claim?
- Does the result reproduce with multiple seeds?
- What can't I infer from the published experiments?
