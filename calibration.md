# M4 calibration — four inputs

Four calibration inputs (150–250 words each), run against /submit.

| # | Type | model_score | style_score | confidence |
|---|---|---|---|---|
| 1 | Clear AI | 0.7692 | 0.4118 | 0.6262 |
| 2 | Clear human (private email) | 0.6133 | 0.4796 | 0.5598 |
| 3 | Clear human (formal notice) | 0.8216 | 0.4551 | 0.6750 |
| 4 | Lightly-edited AI | 0.7286 | 0.3980 | 0.5964 |

## Findings

- **Clear-AI vs clear-human gap is 0.066**, below the M2 criterion 2 target of
  0.30. Not resolved in Unit 7; diagnosed and fixed in Unit 8.
- **Formal human notice scored highest (0.675)**, above clear AI (0.626) —
  signal one's reverse blind spot: formal boilerplate is highly predictable.
- **style_score flat at 0.40–0.48 across all four** — signal two's
  normalisation was tuned on short texts and degrades on long ones.
- **Lightly-edited AI dropped only 0.030 vs clear AI** — cheap manipulation
  barely moves the score.

These are the calibration problems Unit 8's run_eval and attack set will
diagnose.