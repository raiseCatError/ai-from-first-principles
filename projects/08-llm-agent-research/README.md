# Safe tool-using agent and research report

**Timing:** Weeks 44–48

## Scope

Build a framework-free tool-action-observation loop, evaluation harness and final research experiment. Start with offline mocked tools and deterministic policy; only enable real tools deliberately.

## Acceptance gates

- [ ] Tool allowlist, schema validation and max-step limit
- [ ] Tests for malformed actions, stuck loops and unsafe instructions
- [ ] 20+ evaluation tasks with pass/fail results
- [ ] Success/cost/latency/steps recorded versus baseline
- [ ] Original hypothesis with an ablation and reproducible protocol

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
