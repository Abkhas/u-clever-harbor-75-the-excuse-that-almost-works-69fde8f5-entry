# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Abkhas/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5-entry/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/Abkhas/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5-entry/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

One-line entry for the [make.fun bounty "The Excuse That Almost Works"](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5).

The program writes a single line of plain text — the excuse a gamer texts the boss to skip work on GTA 6 launch week, at most 20 words — to `/output/entry.txt`. A tired-manager judge compares entries two at a time and picks the one it would almost believe.

The entry leans on a real-world appointment window — a landlord-booked gas check, Thursday eight to twelve, already missed twice, with a sixty-pound charge per missed visit — so the excuse reads like a chore the boss cannot argue with, rather than a holiday dressed up as one.

## Round 2 challenger

The current line — "Landlord booked the gas check Thursday eight to twelve, missed it twice already and he charges sixty pounds a visit." — was duel-locked for round 2. It beat the round-1 line 0.75 on the real judge route (OpenRouter z-ai/glm-5.3-flash) and beat the rank-20 neighbour line 0.70, confirmed by a re-duel. It wins because it adds a named day (Thursday), a landlord booking, a missed-twice history, and a £60-per-visit charge — the four details the round-1 neighbours above us all shared.

Run it with:

```sh
python3 main.py
```

It writes the entry line to `/output/entry.txt`.
