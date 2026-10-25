# Hardware and computing plan

Current assumed laptop: Apple Silicon MacBook Air M2, 8 GB unified memory. Keep compute proportional to learning goals.

| Phase | Expected practical device | Data/model expectation |
|---|---|---|
| 1–3 | CPU laptop | NumPy, scalar autograd, toy datasets |
| 4 | CPU / MPS | Small image and character models |
| 5 | Laptop for tiny GPT; hosted GPU optional | Small context length, small batches, limited data |
| 6 | Laptop for tabular RL; MPS/hosted GPU for DQN/PPO | Classic control, not Atari-scale video |
| 7 | May require hosted GPU for SFT and alignment | Tiny/custom models or small open-weight models |

## Safety checks

Do not fetch many gigabytes of corpora or load multiple checkpoint copies automatically. Configure an explicit memory/compute budget before training. Start on CPU for correctness, then test acceleration. Use reproducible seeds and checkpoint resumption. Clean old scratch/data only after confirming it is reproducible and backed up.

External storage convention: `/Volumes/T7Projects` for repos and durable work; `/Volumes/T7Tmp` for transient heavyweight work. The script `scripts/check-storage.sh` confirms availability before large experiments; it never mounts drives or copies files without permission.

PyTorch's Apple MPS notes: https://docs.pytorch.org/docs/stable/notes/mps.html
