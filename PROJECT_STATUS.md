# Crypt Crawler — PROJECT STATUS
Updated: 2026-10-19

## Purpose
Compact handoff / source of operational context for new ChatGPT sessions. This file records the working state and workflow; verify live GitHub state before relying on commit or CI status.

## Repositories
- Private source of truth: https://github.com/Klawiaturanumeryczna/crypt-crawler
- Public mirror / GitHub Pages: https://github.com/Klawiaturanumeryczna/rypt-crawler-game
- Playable build: https://klawiaturanumeryczna.github.io/rypt-crawler-game/
- CI: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions and https://github.com/Klawiaturanumeryczna/rypt-crawler-game/actions

## Current prototype
- Browser roguelike, Canvas, primary game implementation in `index.html`.
- Supporting files: `README.md`, `DECISION_LOG.md`, `BALANCE_NOTES.md`, `ENEMY_PROGRESSION.md`, `verify.py`, `tests/browser_smoke.py`.
- Recent gameplay changes: no item offers/pickups in floor 1 room 1 (keep 3 hearts + 2 coins); item pickup requires physical contact; four visibly distinct shooting styles; six visibly distinct movement styles.
- Recent automated checks cover starter room, pickup contact, shooting style differences, movement style menu, all ten active-item effects/consumption, and static invariants.
- Last known matching file hashes from the previous verified sync (re-check before relying on them):
  - `index.html`: `8853c2e434c96948d605aa7f1ff0ad8f774be75b`
  - `tests/browser_smoke.py`: `3cdf86d030f7771afe25d79f1f6106431f7fe762`
  - `verify.py`: `b2e7c9c0879d1bacfcea05795fd0db109420197f`
  - `README.md`: `cedfa6155e7081a2e1da3a4a6dbacee88bc49e8a`
  - `BALANCE_NOTES.md`: `367ef8fc39f08070740f68ae65b3133d4ab38f0e`
  - `DECISION_LOG.md`: `d898e872759a9c9ee3b8c0b1c31116ac6670e985`
- These hashes are historical checkpoints, not proof of the current head or deployment.

## Confirmed design constraints
- Up to 30 rooms per floor. Floor 1 has no boss; from floor 2, boss is in room 1.
- Exit chance after eligible cleared rooms rises by 5 percentage points per room; after room 20 it is guaranteed to appear in room 21. Room 30 guarantees exit + bonus item. Exit room must be cleared; exploration beyond an available exit remains optional.
- Reward both fast skilled play and optional exploration; no forced timer.
- Floors should gain variety through mechanics, hazards, events, secrets, enemies and rewards, not mainly inflated stats.
- Items should have distinct roles and potentially powerful synergies; familiars should have unique abilities, synergies and evolutions/forms.
- Meta progression should unlock choices without making future runs automatically easy. After final boss, optional harder continuation is envisioned.
- Sandbox/Creative and Auto-Battle/Manager are future ideas only; do not implement them unless explicitly prioritized.
- Read `DECISION_LOG.md` for full decisions and OPEN items. Never invent a value for an OPEN decision.

## Next priorities
1. Verify latest CI runs and current parity between private source and public mirror.
2. Expand meaningful item catalogue and synergies (current item labels/catalogue are still prototype-level).
3. Design the familiar system before implementation; familiar cap/slots remain OPEN.
4. Expand floor identity, secrets/events and boss variety.
5. Plan save data and permanent unlocks after scope is agreed.
6. Next testing gap: longer multi-room/floor/boss runs and gameplay playtesting; automated smoke tests do not replace human gameplay testing.

## Fast, safe workflow for every session
1. Check latest commit on both default branches and latest relevant CI/deployment runs. Do this once at session start.
2. Fetch only files relevant to the current task. Do not re-read every project file unless needed.
3. Before editing a synced file, fetch it from both repos and compare content/SHA. Treat private repo as source of truth unless live repo evidence shows otherwise.
4. Make a coherent batch of code, tests and documentation changes; avoid unnecessary commits that trigger duplicate CI runs.
5. Run static verification and browser smoke where relevant. Clearly distinguish static checks, browser smoke, CI, deployment, and actual human gameplay testing.
6. Synchronize the exact changed files to the public mirror only after confirming the intended source content; then verify both copies match.
7. Check the resulting CI/deployment status before claiming success. Never claim a test or gameplay session occurred unless it did.
8. Update this file only when durable state, priorities, or workflow materially changes. Keep it concise; put detailed design decisions in `DECISION_LOG.md` and balance data in `BALANCE_NOTES.md`.

## Collaboration rules
- Work in Polish with precise, direct reports; no guessing or overstated claims.
- When the user says “OK, ROB”, inspect current state, choose the highest-value safe task, implement, test, verify, document, and continue while sensible work remains.
- Do not ask “what next?” if a safe, useful next task is clear.
- Do not make major balance/mechanics decisions without approval. Record unresolved questions as OPEN and gather evidence before recommending.
- Do not modify Fly With Me or Music Manager while working on Crypt Crawler.
