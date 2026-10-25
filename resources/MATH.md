# Mathematics refresh, just in time

This is a **working checklist**, not a mathematical textbook. Do the short derivations with a pen and implement small numerical checks.

## Vectors and matrices — Weeks 1–2

- Vector `x ∈ Rⁿ`, matrix `W ∈ R^(m×n)`. If `x` is `(n,)`, `W @ x` is `(m,)`.
- Dot product `x·w = Σ xᵢwᵢ`; it measures weighted alignment and builds affine models.
- Matrix multiplication `(a,b) @ (b,c) → (a,c)`; the inner dimensions must match.
- Transpose interchanges axes. Broadcasting is **not** the same as matrix multiplication.

**Derive:** for X `(m,n)` and w `(n,)`, prove predictions `X @ w` have shape `(m,)`.

## Calculus and gradients — Weeks 3–7

- A derivative approximates a local rate of change.
- Partial derivatives are slopes holding other variables fixed.
- Chain rule: `d f(g(x))/dx = f'(g(x)) g'(x)`.
- Gradient of a scalar loss with respect to a vector points toward steepest local increase; gradient descent subtracts `η∇L`.
- Centered finite difference `(f(x+ε) - f(x-ε))/(2ε)` estimates a scalar derivative for smooth functions and an appropriate ε.

**Derive:** if `L(w) = (w x - y)²`, then `dL/dw = 2(wx-y)x`. Test numerically with several `(x,y,w)` values.

## Probabilities — Weeks 4, 7, 18–24

- Conditional probability, expectation, variance, distributions, log probabilities.
- Sigmoid maps a scalar logit to `(0,1)`; softmax maps a vector of logits to a probability distribution.
- Cross-entropy measures negative log-probability assigned to observed labels or tokens.
- For token probability p, surprise is `-log(p)`; average token NLL is a natural language-model metric.

**Derive:** why is assigning `p=0.01` to the true event penalized more than `p=0.9`?

## Backprop and optimization — Weeks 11–21

- Build a computation graph, compute forward values, and propagate derivatives in reverse topological order.
- Multiple graph paths contribute gradients that must be **added**, not overwritten.
- Validate gradients against finite differences before trusting an optimizer.
- Learn SGD, mini-batching, learning-rate schedules, momentum/Adam, gradient clipping, and weight decay.

## Transformer mathematics — Weeks 25–32

- Inputs `X` map to queries `Q=XWq`, keys `K=XWk`, values `V=XWv`.
- Scaled attention: `softmax(QKᵀ/√d_k + causal_mask) V`.
- Each attention row distributes weights across **allowed previous/current positions** in a causal model.
- LayerNorm, residual connections and embedding dimensions must agree.

**Derive:** if batch B, sequence T, embedding dimension D, and H attention heads, describe the shapes before and after concatenating heads when D is divisible by H.

## RL and post-training — Weeks 33–48

- Returns `G_t = Σ γᵏ r_(t+k)` reward later events with discount factor `γ`.
- Bellman updates express current value as immediate reward plus discounted future value.
- Policy gradient uses log probabilities and returns/advantages to improve an action distribution.
- Evaluate stochastic agents over **multiple random seeds**, not one lucky rollout.
- Preference-based language-model objectives compare distributions over preferred and rejected completions.

Do not just memorize notation; write a small numerical or tensor example for each concept. Full explanations: [D2L](https://d2l.ai/chapter_preliminaries/index.html), [3Blue1Brown](https://www.3blue1brown.com/topics/linear-algebra), [Spinning Up](https://spinningup.openai.com/en/latest/).
