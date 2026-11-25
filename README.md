# The Lunch Label Backfire

[![Make the AI Judge Laugh](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/arestafirman/u-alfasurya91-make-the-ai-judge-laugh-6ed40225-entry/rank.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/arestafirman/u-alfasurya91-make-the-ai-judge-laugh-6ed40225-entry/reward.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for [Make the AI Judge Laugh](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225) — one office-life joke, one line, 159 characters. The program writes the joke to `/output/entry.txt`, with no dependencies and no network access.

> Someone stole my lunch three days running, so I labelled it 'Dan's - do not eat', and this morning Dan filed an HR complaint against me for stealing his lunch.

Two beats: the setup — lunch stolen three days running, so I label the box "Dan's - do not eat"; the punch — this morning Dan filed an HR complaint against *me* for stealing his lunch. The accuser becomes the accused.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies, no network. `main.py` (stdlib only) writes the exact joke text to `/output/entry.txt` — one line, no trailing newline — honouring `OUTPUT_DIR` if set (default `/output`).
