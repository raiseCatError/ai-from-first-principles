# Publish to GitHub

The folder is a **real local Git repository with an initial commit**, not yet a remotely hosted GitHub repository. Your connected GitHub integration may not have permission to *create* a new repository through chat; GitHub CLI can create one after **you** authenticate on your Mac.

**Suggested repository:** `raiseCatError/ai-from-first-principles` (private initially; make public only if you decide to share notes/code).

## Option A: one command with GitHub CLI

1. Install [GitHub CLI](https://cli.github.com/) if necessary (`brew install gh` on macOS).
2. Authenticate on your own machine with `gh auth login`.
3. From this folder, run:

```sh
gh repo create raiseCatError/ai-from-first-principles --private --source=. --remote=origin --push
```

This creates a **new private repository** and pushes the current commit. Change `--private` to `--public` if intentionally publishing it. If the repo name already exists, choose a different name rather than overwriting it.

## Option B: create an empty repository via the website

Create a **private, empty** repo at https://github.com/new . Do **not** initialize it with a README, license or gitignore because those are already here. Then:

```sh
git remote add origin https://github.com/raiseCatError/ai-from-first-principles.git
git push -u origin main
```

## Before any public push

Run `python3 -m unittest discover -s tests -v`, inspect `git status`, and check that your notes/logs/datasets contain no secrets or private data.
