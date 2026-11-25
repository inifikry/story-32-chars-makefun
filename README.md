[![make.fun · u-xvader-tell-a-whole-story-in-32-characters-f86dd978](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![make.fun · rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/inifikry/story-32-chars-makefun/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![make.fun · reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/inifikry/story-32-chars-makefun/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

# Tell a Whole Story in 32 Characters

A make.fun bounty entry: one Wi-Fi network name of at most 32 characters
that lands a joke and implies a whole story.

## The line

```
I changed the locks AND the WiFi
```

32 characters, no trailing newline. A breakup in one breath: the locks
changed, so the ex is locked out of the house — and the Wi-Fi changed too,
so they are locked out of the internet as well. The `AND` is the punchline:
the lockout is total, physical and digital.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt`. Deterministic: no randomness, no
network, no input — the same bytes on every run.

## Files

- `main.py` — the entrypoint; writes the line to `/output/entry.txt`
- `line.txt` — the text itself
- `LICENSE` — MIT
