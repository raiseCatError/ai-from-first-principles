# AI from First Principles

**A build-first, evidence-based 48-week route from basic Python to building/trainable ML systems, a tiny GPT, reinforcement-learning agents, and evaluated LLM agents.**

- **Audience:** Python basics completed; previously studied matrices/calculus, now rusty.
- **Time budget:** ~10–12 focused hours a week, adjustable. Weeks are learning modules, **not deadlines**. Extra weeks are fine.
- **Rule:** first implement and test; use frameworks only after learning the mechanism. No API-wrapper curriculum.
- **Cost:** linked course readings/videos can be accessed without purchasing the optional certificates. Some graded labs and cloud GPU compute may have fees. Source materials are linked, not copied.
- **Current state:** all weeks are initially unstarted. The repository contains plans and scaffolds, **not completed models**.

## What do I actually watch first?

**Yes: watch selected Andrew Ng videos first.** Do not attempt all 151 lessons before writing code. Start with four weeks of NumPy/math refresh, then selected Machine Learning Specialization modules during weeks 05–10. Karpathy's Zero to Hero is the main neural-network implementation series from week 11 onward; Stanford CS336 is the advanced LLM resource much later.

| Weeks | Main learning resource | What you build |
|---|---|---|
| 01–04 | NumPy, 3Blue1Brown, D2L preliminaries | Mathematics + optimization primitives |
| 05–07 | Andrew Ng Course 1 W1–W3 | Linear and logistic regression from scratch |
| 08–10 | Andrew Ng Course 2 W3–W4; Course 3 W1, W2 PCA, W3 RL preview | Classical ML comparison suite |
| 11–16 | Karpathy Zero to Hero Lecture 1; optional Andrew C2 W1–W2 | Micrograd-style autodiff engine + MLP |
| 17–22 | PyTorch Basics, Karpathy Lectures 2–6, selected MIT 6.S191 | Character language models and training diagnostics |
| 23–32 | Karpathy Lecture 8 then 7, Stanford CS336 Assignment 1 | Tokenizer + decoder-only Transformer + tiny pretrained GPT |
| 33–40 | OpenAI Spinning Up, Berkeley CS285, Gymnasium | Tabular RL, DQN, REINFORCE, PPO + evaluation |
| 41–48 | Stanford CS336 post-training, Hugging Face agents Unit 1 (concepts), papers | SFT/preference experiments, tool-use agent, benchmark, research report |

Full lesson mapping: [Andrew's exact selection](curriculum/andrew-order.md) · [All weekly tasks](curriculum/weekly-index.md) · [Learning sources](resources/CATALOG.md).

## Start in 5 commands

```sh
# Clone this repository after it is published, or unzip the provided archive.
cd ai-from-first-principles
python3 -m tracker next                  # shows next module
python3 -m tracker show 1                # exact objectives and evidence gate
python3 -m tracker start 1
# Study and work in exercises/week-01, then later:
python3 -m tracker done 1 --evidence "experiments/2026-11-01-week-01.md"
python3 -m tracker report                # creates PROGRESS.md
```

Start with [Week 01](weeks/01.md) and [Day 1 exercises](exercises/week-01/README.md). For dependencies, see [setup](SETUP.md). No account or API key is required for the tracker.

## Repo contents

```text
START-HERE.md                first-day instructions
SETUP.md                     practical Python, macOS and storage setup
curriculum/weeks.json        canonical course machine-readable data
curriculum/weekly-index.md  phases and every week's focus
curriculum/andrew-order.md  exact Andrew Ng video/module order
weeks/01.md ... 48.md       one study + maths + build + acceptance sheet/week
progress.json                your tracked source of truth
tracker/                    dependency-free CLI with tests
exercises/week-01/          functional starter exercises and self-tests
projects/                   eight gated capstone specs
resources/                  math, papers, sources, experimentation, compute
notes/                      blank notes and concept recall templates
experiments/                reproducible experiment template
skills/                     AI learning mentor and research reproduction skills
.claude/skills/             ready-to-use Claude Code skill installations
prompts/                    prompts for ChatGPT and Claude Code
.github/workflows/          curriculum validation in CI
```

## Definition of a completed week

- You can explain the mechanism without a script.
- You have implemented the core idea in your own code.
- You have at least one correctness test, comparison, or numerical check.
- You have noted dataset provenance, deterministic seeds and assumptions where relevant.
- You have written down a failure or limitation, not just best-case results.
- You have linked a real evidence artifact with `tracker done`.

**Do not mark a lesson completed for watching a video alone.**

## Learning with AI without outsourcing the learning

Use the provided [AI learning mentor skill](skills/ai-learning-mentor/SKILL.md) for hints, Socratic questions, math verification, and code review. It must *not* immediately deliver completed assignments when you are trying to learn. You can relax that mode intentionally when studying a reference implementation after your own attempt.

## Research and credits

Course materials remain owned by their authors. The repository contains original instructional structure, links and exercise scaffolding; **no scraped slides, videos, textbook chapters, proprietary datasets, weights or course solution keys**. See [sources](resources/CATALOG.md) and [license](LICENSE). Course pages can change; check upstream links before starting a module.

## Publishing

This downloadable folder is already a Git repository with an initial commit. To create and publish a new repository in your own GitHub account, follow [PUBLISH.md](PUBLISH.md). Publishing is optional; the tracker works entirely locally.
