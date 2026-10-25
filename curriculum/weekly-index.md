# All 48 weeks

This is the index. The actual study, math, implementation and evidence for every module live in `weeks/NN.md`.

| Week | Phase | Topic | Main build |
|---:|---|---|---|
| [01](../weeks/01.md) | Foundations | Python scientific computing | Finish exercises/week-01; implement elementwise operations and a dot product by loops, then validate with NumPy |
| [02](../weeks/02.md) | Foundations | Linear algebra in code | Implement matrix multiply with explicit loops; compare with NumPy using multiple shapes |
| [03](../weeks/03.md) | Foundations | Derivatives and computation graphs | Implement centered finite differences; numerically estimate gradients on simple functions |
| [04](../weeks/04.md) | Foundations | Probability, coding hygiene and optimization | Simulate noisy observations; use gradient descent to minimize a convex loss |
| [05](../weeks/05.md) | Classical ML | Regression: data to learning | Univariate regression from scratch; no sklearn estimators |
| [06](../weeks/06.md) | Classical ML | Vectorized multivariable regression | Build multivariate linear regression in NumPy with standardization |
| [07](../weeks/07.md) | Classical ML | Logistic regression and classification | Binary logistic regression from scratch with NumPy |
| [08](../weeks/08.md) | Classical ML | Generalization and reliable experiments | Reusable train/validation/test split and metric suite with confusion matrix |
| [09](../weeks/09.md) | Classical ML | Trees and unsupervised learning | Build a small decision-tree classifier and k-means from scratch |
| [10](../weeks/10.md) | Classical ML | ML capstone and reinforcement-learning preview | Train and compare 3 classical models on one dataset; implement 2-D PCA |
| [11](../weeks/11.md) | Neural Networks | Micrograd introduction | Create Value data structure and scalar operation graph without automatic differentiation yet |
| [12](../weeks/12.md) | Neural Networks | Automatic differentiation | Implement Value.backward with topological order and accumulation |
| [13](../weeks/13.md) | Neural Networks | A trainable neuron and MLP | Build Neuron, Layer and MLP objects on own autograd |
| [14](../weeks/14.md) | Neural Networks | Training dynamics | Train XOR; add reproducible seeding, learning-rate sweep, plotted metrics |
| [15](../weeks/15.md) | Neural Networks | Backprop debugging | Implement automated finite-difference gradient checks and diagnostics |
| [16](../weeks/16.md) | Neural Networks | Autodiff engine capstone | Package and document your from-scratch scalar autodiff MLP |
| [17](../weeks/17.md) | Deep Learning | Tensor PyTorch fundamentals | Recreate micrograd XOR network in PyTorch; compare gradients |
| [18](../weeks/18.md) | Deep Learning | Text bigrams and makemore | From-scratch count-based and neural character bigram models |
| [19](../weeks/19.md) | Deep Learning | Embedding and language MLP | Train a context-window MLP language model in PyTorch |
| [20](../weeks/20.md) | Deep Learning | Activation, gradient and initialization diagnostics | Visualize activation and gradient distributions; try normalization |
| [21](../weeks/21.md) | Deep Learning | Backprop by hand in tensor models | Implement manual backprop for a small MLP language model |
| [22](../weeks/22.md) | Deep Learning | Deeper networks and baseline language model | Construct deeper causal sequence model and baseline comparison |
| [23](../weeks/23.md) | LLMs From Scratch | Tokenizers: character and bytes | Implement character tokenizer and UTF-8 byte tokenizer |
| [24](../weeks/24.md) | LLMs From Scratch | Byte pair encoding | Implement BPE training and encoding from scratch |
| [25](../weeks/25.md) | LLMs From Scratch | Attention mathematics | Single-head self-attention with numpy then PyTorch |
| [26](../weeks/26.md) | LLMs From Scratch | Causal self-attention and multi-heads | Implement multi-head causal attention and positional embeddings |
| [27](../weeks/27.md) | LLMs From Scratch | Transformer block construction | Build decoder-only block: norm, attention, MLP, residual connections |
| [28](../weeks/28.md) | LLMs From Scratch | Full tiny GPT architecture | Stack decoder blocks, embedding, LM head, causal loss and generation |
| [29](../weeks/29.md) | LLMs From Scratch | Optimization and training engine | Implement training loop with optimizer, clipping, checkpoint and resume |
| [30](../weeks/30.md) | LLMs From Scratch | Pretrain a tiny GPT | Pretrain a tiny random-initialized GPT on a permitted text corpus |
| [31](../weeks/31.md) | LLMs From Scratch | Decoding and inference | Implement sampling options and KV cache as separate experiment |
| [32](../weeks/32.md) | LLMs From Scratch | LLM capstone and evaluation | Publish tiny GPT model card, tests, learning curves, ablation and limitations |
| [33](../weeks/33.md) | Reinforcement Learning | MDPs and value functions | Implement a small grid world and random policy baseline |
| [34](../weeks/34.md) | Reinforcement Learning | Tabular Q-learning | Train tabular Q-learning in a grid world/FrozenLake-like environment |
| [35](../weeks/35.md) | Reinforcement Learning | DQN fundamentals | Build DQN with replay buffer and target network |
| [36](../weeks/36.md) | Reinforcement Learning | DQN evaluated properly | Train DQN on CartPole or equivalent classic control task |
| [37](../weeks/37.md) | Reinforcement Learning | Policy gradients | Implement REINFORCE from scratch in PyTorch |
| [38](../weeks/38.md) | Reinforcement Learning | Baselines and actor-critic | Add critic and value baseline to policy-gradient agent |
| [39](../weeks/39.md) | Reinforcement Learning | PPO and training stability | Implement minimal PPO on a simple environment |
| [40](../weeks/40.md) | Reinforcement Learning | RL agent capstone | Build reproducible environment + agent comparison suite |
| [41](../weeks/41.md) | Post-training & Agents | Instruction tuning fundamentals | Construct small instruction dataset and supervised-tuning experiment |
| [42](../weeks/42.md) | Post-training & Agents | Parameter-efficient fine-tuning and evaluation | Fine-tune a manageable existing open-weight small model or your tiny model |
| [43](../weeks/43.md) | Post-training & Agents | Preferences, reward models and DPO | Create toy preference pairs; implement a small reward/preference objective |
| [44](../weeks/44.md) | Post-training & Agents | Raw tool-use loop (no framework) | Create safe typed tool registry, action/observation loop, termination |
| [45](../weeks/45.md) | Post-training & Agents | Planning, memory and recovery | Add short-term state, retrieval, retries and tool-error handling |
| [46](../weeks/46.md) | Post-training & Agents | Agent evaluation and safety | Build benchmark harness of 20+ fixed tasks and deterministic mock cases |
| [47](../weeks/47.md) | Post-training & Agents | Reasoning RL and post-training experiment | Replicate a modest toy RL-for-reasoning experiment in constrained compute |
| [48](../weeks/48.md) | Post-training & Agents | Independent AI research capstone | Choose one prior model/agent component; improve or falsify one hypothesis |
