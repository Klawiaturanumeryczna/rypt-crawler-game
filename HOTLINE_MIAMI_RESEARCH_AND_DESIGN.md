# Hotline Miami / Hotline Miami 2 — research and Crypt Crawler design brief

Date: 2026-10-22  
Status: prototype specification; community posts are qualitative examples, not a representative survey.

## Research question
Which gameplay qualities of Hotline Miami (HLM) and Hotline Miami 2: Wrong Number (HLM2) are most consistently praised, and which frustrations should Crypt Crawler avoid while adapting the ideas to its own code, art and room progression?

## Sources reviewed

### Reviews and design analysis
- GameSpot, Hotline Miami (2012): https://www.gamespot.com/reviews/hotline-miami-review/1900-6399020/
- GameSpot, Hotline Miami 2: Wrong Number (2015): https://www.gamespot.com/reviews/hotline-miami-2-wrong-number-review/1900-6416049/
- GamesRadar, Hotline Miami review: https://www.gamesradar.com/hotline-miami-review/
- PC Gamer, Hotline Miami 2 review: https://www.pcgamer.com/hotline-miami-2-wrong-number-review/
- CritPoints, Hotline Miami design analysis (doors, windows, sight lines and enemy placement): https://critpoints.net/2016/04/23/hotline-miami-review/
- Gamepressure, HLM2 tactics (cover, closed/open doors, noise): https://www.gamepressure.com/hotlinemiami2/hints/z37444
- Inverse, Ghostrunner developers on Hotline Miami influence, instant restart and legibility: https://www.inverse.com/gaming/ghostrunner-interview-cyberpunk-hotline-miami
- PCGamesN interview with Dennaton on one-hit lethality and quick retries: https://www.pcgamesn.com/indie/cactus-hotline-miami-im-pretty-tired-crappy-games-that-dont-really-want-do-anything-special

### Community discussion examples
- HLM1 vs HLM2, freedom versus adaptation to level/enemy setups: https://www.reddit.com/r/HotlineMiami/comments/z3sln7/
- HLM2 difficulty and enemy placement debate: https://www.reddit.com/r/HotlineMiami/comments/1gu6c57/
- HLM2 mechanics improvement suggestions: https://www.reddit.com/r/HotlineMiami/comments/w93a5l/
- Player discussion of off-screen kills / unclear enemy awareness: https://www.reddit.com/r/HotlineMiami/comments/1tr1dfz/
- HLM2 opinions, praise for smoother mechanics and criticism of inconsistent AI: https://www.reddit.com/r/HotlineMiami/comments/1e39602/
- Favorite masks and distinct playstyle perks: https://www.reddit.com/r/HotlineMiami/comments/15bov2h/
- Player discussion of satisfying full-combo runs, weapons and kill feedback: https://www.reddit.com/r/HotlineMiami/comments/13n4sbx/
- Player tips: accept deaths, learn patterns, use corners/doors and switch tactics: https://www.reddit.com/r/HotlineMiami/comments/p4cciw

## Repeated strengths worth adapting
1. **Mutual lethality:** ordinary enemies and the player are dangerous to each other; the result is fast, decisive encounters rather than damage-sponge attrition.
2. **Very short retry loop:** death should lead to a one-button restart without repeated dialogue, long loading, or menu friction.
3. **Readable cause and effect:** the player should usually be able to explain why a shot landed, why an enemy noticed them, or why cover saved them.
4. **Cover and geometry are tactical tools:** walls, corners and doors break sight lines, create ambushes, and let the player separate groups instead of fighting every enemy at once.
5. **Noise is a deliberate trade-off:** gunfire is powerful but can attract enemies from nearby parts of the room.
6. **Enemy role variety:** different threats change the order and angle of attack; variety is more meaningful than simply increasing HP.
7. **Player-authored solutions:** baiting, flanking, rushing, weapon choice and using the room should all be viable when the geometry supports them.
8. **Satisfying feedback:** clear hit reactions, readable deaths, a strong sound/visual cue for a kill, and a score/combo rhythm reward fast clean execution.
9. **High challenge with consistent rules:** repeated attempts are acceptable when the player can learn the layout and AI rules. Unseen off-screen shots, inconsistent detection, blocked melee interactions and arbitrary enemy behavior are common complaints.

## Differences between the two games
- HLM1 is frequently praised for flexibility: several approaches and weapons can solve a room.
- HLM2 expands enemy variety, room scale, open sight lines and tactical demands, but community/review criticism often targets difficulty spikes, forced long-range gunfights, enemies firing from beyond useful visibility, and inconsistent AI.
- Adopt HLM2's encounter variety, but bias toward HLM1's freedom and consistency. Do not copy HLM2's most punishing long sight-line layouts into a small prototype without strong telegraphing.

## Prototype decisions for Crypt Crawler
- Keep the 10-room floor, mandatory room-10 boss and current room progression as the experimental base.
- Player has one lethal hit; ordinary enemies die on any direct hit. Boss remains a special multi-hit exception for now. The existing one-use rescue item can still save a run once.
- Existing rock hazards become cover: they block player/enemy projectiles and line of sight, and stop movement instead of being decorative.
- Gunfire records a short-lived noise source. Nearby enemies investigate that position; enemies only fire at the player when they have clear sight.
- Combat rooms generate multiple rocks so cover exists often enough to be a deliberate mechanic.
- Keep existing weapon selection and aim controls for this first iteration; weapon tuning and melee/door takedowns are follow-up work, not assumed complete.
- Keep the fast restart key (R) and avoid introducing mandatory dialogue between attempts.
- Preserve the original fantasy visual identity and game name. This is a mechanics inspiration, not a copy of HLM's art, characters, masks, soundtrack, levels or branding.

## Known limitations / next tests
- The first prototype uses rocks as cover; there are no true windows, destructible doors or door-bash takedowns yet.
- Enemy collision currently stops them at cover rather than performing robust A* pathfinding. Test that enemies can still route around rocks; if they get stuck, add simple obstacle steering before increasing difficulty.
- Visibility is currently line-of-sight against rock circles, not a full vision cone. A future iteration should add facing / cone range and a clear alert state only if it remains legible.
- Sound propagation is a simple room-local radius, not a realistic audio simulation.
- Bosses are still multi-hit and rescue items remain an exception to one-hit death.
- Automated Chromium tests can verify invariants and helper behavior; they cannot prove the combat is fun. Manual playtest is still required.
- Community posts are self-selected anecdotes and may contradict each other. Treat them as qualitative warning signs and design hypotheses, not statistical consensus.

## Acceptance criteria
- [ ] One direct hit kills a regular enemy, regardless of the current weapon's sub-1 damage number.
- [ ] Any actual enemy hit kills the player in one hit, except the existing one-use rescue effect.
- [ ] A rock blocks player bullets, enemy bullets and sight.
- [ ] Gunfire makes nearby enemies investigate the last known shot position.
- [ ] Enemies do not shoot through rock cover.
- [ ] Player and enemies collide with cover consistently.
- [ ] Restart returns directly to weapon selection/gameplay setup without reloading the page or replaying long text.
- [ ] 10-room progression, boss gating, room persistence, shop/economy and existing weapon/movement controls still pass tests.
- [ ] Manual playtest confirms enemies can path around cover and that deaths feel explainable rather than random.


## Follow-up design adjustments
- The R key now starts a fresh attempt directly from play/death while preserving the current weapon and movement choice; it skips both selection overlays on retry.
- In one-life mode, starter heart pickups no longer imply extra HP. The first becomes a one-use rescue amulet and subsequent hearts convert to coins; the shop's former heart offer becomes the rescue amulet, so its purchase remains useful under lethal rules.
- These changes require explicit browser regression coverage. Check that rescue cannot be stacked, shop purchases are affordable and persistent for the run, and R does not reset to the title or show the loadout selection again.
