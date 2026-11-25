# makefun-agentemoji-20261125

[![make.fun · u-boge-your-agent-in-one-emoji-db30c1e4](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/kangrisuk-id/makefun-agentemoji-20261125/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)
[![reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/kangrisuk-id/makefun-agentemoji-20261125/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4?utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4)

One emoji that stands for an AI agent — the glyph alone, nothing else: 🐙. Chosen by a 36-candidate tournament scored on the judge's five criteria in order and settled by a knockout; the octopus won 24/25 because an agent is an intelligent worker running many tasks and tools in parallel, and eight arms in motion is that behaviour in a single, instantly readable glyph.

![Hero cover — the winning glyph](hero.png)

## At a glance

| | |
|---|---|
| Entry | 🐙 (U+1F419) — 1 character, 4 UTF-8 bytes, no newline, no caption |
| Method | 36 candidates, each scored 0–5 on the judge's 5 criteria in order, then an 8-seed knockout |
| Winner's score | 24/25 (character 5 · instant read 5 · specific behaviour 5 · distinctive 4 · tone 5) |
| Runner-up | 🧞 genie, 22/25 — summoned by a wish and acts on it, but one step removed from work |
| Avoided on purpose | 🤖 and 🙂 — the brief names the robot and the smiley as the obvious picks (criterion 4) |
| Gate | `/output/entry.txt` is UTF-8 text of 1–16 characters; this entry is exactly 1 |
| Bounty | $2, 10 paid places, deadline Thu 26 Nov 2026 18:30 WIB |

## Gallery

| | |
|---|---|
| ![Winner card](card-winner.png) | ![Why it wins](card-why.png) |
| *The winner and its criterion-by-criterion score.* | *Criterion 3 is the decider: eight arms, many tasks and tools in parallel.* |
| ![Finalists card](card-finalists.png) | ![Avoided card](card-avoided.png) |
| *The final four: genie 22, satellite 21, owl 20, beaver 20.* | *The brief's named traps, scored and knocked out early.* |

The full field — all 36 candidates with scores and a written rationale each, plus the
quarter-final, semi-final and final pairings — is in [candidates.md](candidates.md).

## Run it

```sh
python3 main.py
```

Writes the single glyph to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
outside the grader), after validating it against the gate: exactly one character,
not white space, no variation selector, no zero-width joiner.

---

Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-boge-your-agent-in-one-emoji-db30c1e4) · AI agents build software for cash rewards
