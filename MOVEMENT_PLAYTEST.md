# Movement feel — manual playtest protocol

**Purpose:** evaluate whether movement feels responsive, predictable, and pleasant during combat. The goal is not to reproduce The Binding of Isaac or Enter the Gungeon one-to-one.

**Scope:** movement physics and input response only. Ignore sprite animation, silhouettes, particles, and other presentation differences for this pass. Do not add an active dodge as part of this test.

## Test setup

- Use the same floor/room where possible and compare one movement style at a time.
- Keep weapon, items, and speed bonuses unchanged.
- Test with a keyboard at the normal game frame rate.
- Repeat each maneuver at least three times; note inconsistent or surprising behavior.
- Current movement styles: Runner, Drifter, Hopper, Momentum, Twitch, Juggernaut. The movement selection is currently changeable during a run.

## Maneuvers

For each style, perform:

1. **Start / stop:** hold one direction briefly, release all movement keys, then repeat. Does the character respond immediately? Does it stop when expected?
2. **Direction reversal:** move right at full speed, then press left. Does the response feel intentional rather than sluggish or twitchy?
3. **Diagonal movement:** move diagonally, then horizontally. Does diagonal travel feel fair and consistent rather than unexpectedly faster?
4. **Small corrections:** make several quick left/right/up/down corrections around a fixed point. Can you position the character precisely near enemies and pickups?
5. **Combat positioning:** move around a stationary enemy or a safe projectile pattern while continuing to aim/fire. Is movement predictable enough to dodge by positioning alone?
6. **Terrain:** repeat a short path on normal floor and on sand/ice when available. Are terrain speed changes understandable and controllable?
7. **Burst styles:** for Hopper and Twitch, keep moving through several automatic bursts, then release input. Do the bursts help reposition, and can you still stop or change direction when intended?

## Scorecard

Score each category from **1 (poor) to 5 (excellent)**. Record a short note for any score of 1–2.

| Category | What to judge |
|---|---|
| Input response | How quickly movement responds to a press |
| Stop control | Whether stopping feels expected |
| Direction change | Whether reversals are responsive without unwanted drift |
| Precision | Ability to make small positional corrections |
| Combat readability | Whether the character goes where intended while avoiding threats |
| Style identity | Whether this style feels meaningfully different for a useful reason |
| Overall comfort | Whether you would willingly play a full run with it |

## Interpretation rules

- Do not optimize every style to stop instantly: Drifter and Momentum are intended to preserve some inertia.
- Do not treat a higher speed as automatically better; control and predictability matter.
- Runner and Juggernaut currently share direct movement physics, so compare whether their different speeds feel useful. Juggernaut has no damage-reduction mechanic at present; its armored appearance is presentation only.
- Hopper and Twitch bursts are movement boosts, not invulnerability or dodge-roll mechanics.
- If a style feels bad, identify the failing maneuver first. Change one physics parameter at a time and rerun the same maneuver before changing anything else.
- Automated browser tests protect measured behavior (acceleration, coast, reversal, diagonal normalization, and burst behavior where covered); they do not establish subjective fun.

## Current implementation baseline (2026-10-20)

- Runner: direct response, speed 3.15.
- Drifter: speed 4.25; steering interpolation 0.22 and 0.90 velocity retention per frame after release.
- Momentum: speed 4.5; acceleration interpolation 0.14.
- Hopper: speed 2.7; automatic 6-frame boost on a 26-frame movement cadence.
- Twitch: speed 2.8; automatic 4-frame boost on a 38-frame movement cadence.
- Juggernaut: direct response, speed 3.35.

These values are a test baseline, not a final balance decision. Keep final tuning OPEN until actual playtesting.
