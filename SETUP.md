# Setup: Mac, Python and learning environment

## Minimal Python environment

Use any supported recent Python version (3.11–3.13 for the tracker). The tracker uses **only Python's standard library**. The starter math exercises require NumPy.

```sh
cd ai-from-first-principles
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements-foundations.txt
python -m unittest discover -s tests -v
python -m tracker next
```

Optional plotting: `python -m pip install matplotlib`. Start PyTorch only when reaching Week 17 using the **current official** [PyTorch installation instructions](https://pytorch.org/get-started/locally/) rather than a pinned copy of an outdated command. Check GPU support with:

```python
import torch
print('MPS built:', torch.backends.mps.is_built())
print('MPS available:', torch.backends.mps.is_available())
```

For RL in weeks 33+, follow [Gymnasium](https://gymnasium.farama.org/) documentation and install it then; nothing needs installing now.

## External-disk hygiene (especially on an 8 GB M2 Mac)

- Small code, tiny datasets and docs are fine in a normal repository. Large data, caches and model checkpoints belong on your external drive.
- Recommended: clone repo under `/Volumes/T7Projects/Projects/ai-from-first-principles`, and store heavy experimental scratch under `/Volumes/T7Tmp`.
- Before large experiments: `bash scripts/check-storage.sh`. It **fails closed** if the required mount points cannot be verified; it does not create or mount them.
- Never silently fall back to internal storage if an external disk is absent. Don't commit downloaded corpora, weights, checkpoints, logs or secrets.
- Experiment costs depend on compute provider. Explicitly approve GPU usage and spending yourself; no workflow in this repo automatically starts cloud jobs.

## Recommended editor workflow

Use your existing editor and terminal. Prefer `.py` scripts + a README + tests for core algorithms. Notebooks are okay for exploration, but move important functions into importable Python modules for testing.

## Security and ethics

Only use data that you have rights to use. Avoid confidential material in model training or public commits. In tool-using agents, begin with mocked or allowlisted tools; disable arbitrary shell, network and filesystem writes by default. Document known risks and evaluation leakage.
