# Weekly study process

## Recommended 12 hours/week

- **6h implementing:** type, debug and test your own algorithms.
- **3h study:** lectures and primary-source reading.
- **2h experiments:** baselines, repeated runs, inspection of failures.
- **1h writing:** derivations, reproducibility notes and explaining what you learned.

If short on time, prioritize core implementation over optional lectures. Weeks are milestone buckets; let any week take longer.

## A lecture loop

1. **Before** (5 min): predict what the mechanism does and list 2 questions.
2. **During:** pause before the instructor writes the solution; work out shapes and equations yourself.
3. **After:** reproduce from a blank file with notes but not copied source.
4. **Check:** write a numerical test, baseline, evaluation split and failure case.
5. **Retain:** explain the concept out loud without notes; reimplement critical parts after a few days.

## Completion gates

The tracker requires an **evidence link/string** before marking a week done. Evidence is not a score, and the tracker cannot inspect the quality of your solution automatically.

Evidence should contain code/test files or experiment reports with:
- What question were you answering?
- What model, optimizer and dataset were used?
- What were the metrics, seeds, splits, configs and machine constraints?
- What are at least two failures or limitations?
- Could someone reproduce the result from your repository?

## Working with Claude Code or ChatGPT

Use the bundled learning mentor in `skills/`. In learning mode, the assistant must teach through small questions, debugging hints, mathematical checks, and code reviews. It should **not** replace your implementation with an unrelated generated system or auto-complete all TODOs unless you explicitly request a worked solution after an attempt.

## Do not confuse these two achievements

- **Model built from scratch:** own model architecture, loss, training loop and randomly initialized weights; source code can depend on PyTorch tensor operations after week 17.
- **Foundation model trained at scale:** requires very large curated datasets, compute, systems engineering and extensive evaluation. Your tiny GPT is real ML, not proof of frontier capability.

## Learning outcomes over certificates

Prefer a tested 200-line implementation and a clear writeup to a playlist marked 100% complete without understanding. Revisit weak concepts before advancing.
