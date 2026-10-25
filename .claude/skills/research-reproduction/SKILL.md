---
name: research-reproduction
description: Read and critically evaluate an ML paper or model claim, design a faithful small replication, preserve provenance and report uncertainty and failure modes.
---

# Research Reproduction

## Objective

Help reproduce *verifiable* AI results without conflating author claims, independent replications, and original experiments.

## Procedure

1. Identify paper version/date, authors, official code, dataset, licenses and accessible compute requirements; cite primary sources and distinguish unverified information.
2. Restate hypothesis, task, objective, evaluation protocol, metric and comparisons in plain language.
3. Derive the training objective and trace tensor shapes before coding.
4. Define the narrowest practical replica; explicitly record differences from the paper. Label reduced-size experiments **toy replications**.
5. Baseline first: random, simple supervised, older architecture, or officially supplied result as appropriate.
6. Fix and record data split, preprocessing, seeds, optimizer settings, hardware, epochs/steps and token counts.
7. Run correctness checks (gradient checks, toy-batch overfit, invariant tests) before investing in compute.
8. Report all runs and failures, not just the best seed. Avoid cherry-picking and accidental test-set tuning.
9. Write a report using `experiments/TEMPLATE.md`: claim, method, setup, baseline, result, uncertainty, limitations, replication instructions.
10. Never say “reproduced” without checking the **same** metric and comparable experimental conditions; distinguish directional/partial reproduction.

## Boundaries

Do not download or redistribute data/weights without legal permission. Never submit paid-course answer keys or copy proprietary teaching material into the repo. Do not fake unavailable logs or source verification.

## Output

A concise replication plan or evidence-backed report, runnable commands where feasible, and a clear list of differences and unresolved uncertainty.
