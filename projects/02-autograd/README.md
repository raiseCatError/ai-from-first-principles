# Scalar autodiff and MLP engine

**Timing:** Weeks 11–16

## Scope

Create Value with a graph of operations, local derivative rules, reverse topological traversal, and gradient accumulation. Train a small MLP on a nonlinear toy task.

## Acceptance gates

- [ ] Finite difference checks for branching and shared nodes
- [ ] Explicit zero_grad and a gradient accumulator
- [ ] Neuron/Layer/MLP composition
- [ ] Learning curve and convergence test
- [ ] Explain chain rule by hand on one graph

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
