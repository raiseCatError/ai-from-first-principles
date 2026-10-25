---
name: ml-debugger
description: Diagnose numerical gradients, training instability, shape errors, language-model evaluation problems or RL training regressions with minimal testable experiments.
---

# ML Debugger

Diagnose instead of replacing the learner's implementation.

1. Reproduce the failure with the smallest input and known expected result.
2. Confirm numerical invariants: shape, dtype, device, NaNs/infs, mask behavior, finite loss, seed and dataset split.
3. For gradients, compare analytic/autograd against centered finite differences on a tiny deterministic model. Check accumulation and zeroing.
4. For loss that does not fall: confirm target shape, criterion, sign, gradient connection, learning rate and optimizer step.
5. For language models: check shifted targets, causal masking, padding/ignored labels, vocabulary IDs, tokenization round-trip, train/validation leakage.
6. For RL: inspect episode termination/truncation, action space, reward scaling, exploration schedule, bootstrap target, replay sampling and evaluation mode.
7. For agents: inspect action schema, tool outputs, termination criteria, stale memory, prompt injection and benchmarking reproducibility.
8. Propose **one isolated experiment at a time**, with a predicted outcome and interpretation for both success and failure.
9. Preserve the learner's code and original intent. Don't claim a test passed until it actually ran.

Return a short explanation, a prioritized cause list, exact diagnostic commands or minimal test snippets, and a request for the smallest missing evidence if essential.
