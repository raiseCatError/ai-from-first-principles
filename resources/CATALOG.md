# Verified course/reference catalog (October 2026)

All third-party materials live at their upstream sites. This repo provides original exercises and links, **not copies** of those lessons. Not every linked course has free grading, lab environments, or certifications.

## Foundations — weeks 01–04

| Resource | Purpose | URL |
|---|---|---|
| NumPy absolute beginner guide | Arrays, indexing, broadcasting | https://numpy.org/doc/stable/user/absolute_beginners.html |
| 3Blue1Brown: Essence of Linear Algebra | Geometric intuition | https://www.3blue1brown.com/topics/linear-algebra |
| 3Blue1Brown: Essence of Calculus | Derivatives and chain rule | https://www.3blue1brown.com/topics/calculus |
| Dive into Deep Learning: Preliminaries | Algebra, calculus, probability, autodiff | https://d2l.ai/chapter_preliminaries/index.html |

## Core ML — weeks 05–10

| Resource | Priority | URL |
|---|---|---|
| Andrew Ng Machine Learning Specialization | Required selected weeks | https://www.deeplearning.ai/specializations/machine-learning |

Read [exact viewing order](../curriculum/andrew-order.md). No need to finish all paid assignments or learn TensorFlow deeply.

## Neural networks — weeks 11–22

| Resource | Priority | URL |
|---|---|---|
| Karpathy Zero to Hero | Required lectures 1–6 | https://karpathy.ai/zero-to-hero.html |
| Karpathy lesson notebooks | Reference **after own attempts** | https://github.com/karpathy/nn-zero-to-hero |
| Karpathy micrograd | Implementation comparison | https://github.com/karpathy/micrograd |
| Karpathy makemore | Model comparison | https://github.com/karpathy/makemore |
| PyTorch tutorials | Required from week 17 | https://docs.pytorch.org/tutorials/beginner/basics/intro.html |
| MIT 6.S191 | Selective conceptual supplement | https://introtodeeplearning.com/ |

## LLM construction — weeks 23–32

| Resource | Priority | URL |
|---|---|---|
| Karpathy GPT and tokenizer lectures | Required; tokenizer then GPT | https://karpathy.ai/zero-to-hero.html |
| Karpathy minbpe | Reference after implementation | https://github.com/karpathy/minbpe |
| Karpathy nanoGPT | Reference after implementation | https://github.com/karpathy/nanoGPT |
| Stanford CS336 Spring 2026 | Assignment 1 is primary stretch project | https://cs336.stanford.edu/ |
| Attention Is All You Need | Original Transformer paper | https://arxiv.org/abs/1706.03762 |
| AdamW: Decoupled Weight Decay Regularization | Optimization reference | https://arxiv.org/abs/1711.05101 |

**Warning:** CS336's advanced systems, Triton and distributed GPU work requires hardware and skills not yet assumed here. Do Assignment 1 in constrained form first; the rest is a later extension, not a requirement for finishing week 32.

## Reinforcement learning — weeks 33–40

| Resource | Priority | URL |
|---|---|---|
| OpenAI Spinning Up — RL Key Concepts | First principles | https://spinningup.openai.com/en/latest/spinningup/rl_intro.html |
| OpenAI Spinning Up — Policy Gradient | REINFORCE derivation | https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html |
| Berkeley CS285 | Advanced lectures/selective problem sets | https://rail.eecs.berkeley.edu/deeprlcourse/ |
| Gymnasium | Standard learning environments | https://gymnasium.farama.org/ |
| PPO | Paper | https://arxiv.org/abs/1707.06347 |

Spinning Up contains older examples and package instructions. Use its **mathematics and design** as reference, not blindly install its old environment.

## Post-training and agents — weeks 41–48

| Resource | Purpose | URL |
|---|---|---|
| Stanford CS336 Assignment 5 | Supervised post-training, reasoning RL, alignment | https://cs336.stanford.edu/ |
| Direct Preference Optimization | Understand preference-based objectives | https://arxiv.org/abs/2305.18290 |
| Hugging Face Agents Unit 1 | Action–observation concepts | https://huggingface.co/learn/agents-course/en/unit1/introduction |

Use frameworks such as smolagents or LangGraph only as optional comparisons after building your own tool loop, safety gates, and evaluation harness.

## Licensing and link maintenance

This catalog records official pages rather than mirroring their files or claiming that all downloads are redistributable. Check links and licensing before using example datasets or publishing trained models. No proprietary course handouts, videos, solved assessments or datasets are committed here.

## Direct Karpathy lectures — verified from the official Zero to Hero syllabus

| Lecture | Focus | Video |
|---:|---|---|
| 1 | Build micrograd | https://www.youtube.com/watch?v=VMj-3S1tku0 |
| 2 | Build makemore (bigram) | https://www.youtube.com/watch?v=PaCmpygFfXo |
| 3 | Makemore MLP | https://www.youtube.com/watch?v=TCH_1BHY58I |
| 4 | Activations, gradients, batch normalization | https://www.youtube.com/watch?v=P6sfmUTpUmc |
| 5 | Manual backpropagation | https://www.youtube.com/watch?v=q8SA3rM6ckI |
| 6 | Building a WaveNet-style hierarchy | https://www.youtube.com/watch?v=t3YJ5hKiMQ0 |
| 7 | GPT architecture | https://www.youtube.com/watch?v=kCc8FmEb1nY |
| 8 | Build a tokenizer | https://www.youtube.com/watch?v=zduSFxRajkE |

CS336 official Spring 2026 lecture playlist: https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV

CS336 Assignment 1: https://github.com/stanford-cs336/assignment1-basics
