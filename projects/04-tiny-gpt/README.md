# Own tokenizer and decoder-only GPT

**Timing:** Weeks 23–32

## Scope

Implement character/byte/BPE tokenizers, positional embeddings, causal multi-head attention, blocks, generation, an optimizer and a pretraining loop from RANDOM initial weights. Tiny model only; must not claim frontier-model capabilities.

## Acceptance gates

- [ ] Tokenizer Unicode round-trip tests
- [ ] Causal mask never reads future positions
- [ ] Tiny-batch overfit test before expensive training
- [ ] Checkpoint and restore without silent config mismatch
- [ ] Held-out loss/perplexity, sampling and at least two ablations
- [ ] Dataset provenance, licensing and compute budget

## Deliverable structure

```text
README.md    — this specification plus your design decisions
src/         — your own algorithms (create when you start)
tests/       — correctness checks (create when you start)
reports/     — reproducible experiment notes (create when you start)
```

## Before seeing reference solutions

Make a hypothesis, write a minimal prototype, add tests and compare with mathematical/numerical ground truth. Note failure modes and hardware limits.

## Record after completing

- Commit SHA or release:
- Dataset source and use rights:
- Hardware/runtime:
- Reproduction command:
- Baseline vs result:
- Limitations:
