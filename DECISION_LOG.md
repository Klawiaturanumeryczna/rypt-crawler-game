# Crypt Crawler — Decision Log
Updated: 2026-10-19
Purpose: durable record of design decisions agreed in chat. This document records intent; it does not mean every feature is implemented.

## Core run and progression decisions

1. **Run goal — D (confirmed):** one main goal combining reaching the end/boss, building a strong character, and discovering items, secrets, and combinations.
2. **Meta-progression — B + C (prior decision, reaffirmed in today's discussion):** permanent progression may exist, alongside unlocks for new items, play styles, familiars, and possibilities. Keep balance in mind; unlocks should broaden choices rather than make future runs automatically easy. Exact permanent upgrades and values remain OPEN.
3. **Synergy strength — B + C (confirmed):** combinations should create a clear advantage; specific sets can radically change how a build plays. Build strength can escalate from modest early options toward powerful combinations.
4. **Exploration — D (confirmed):** both rushing forward and detouring to explore should be viable. Exploration offers worthwhile rewards, but must not become mandatory.
5. **Familiars — B + C + D (prior decision, reaffirmed today):** familiars have unique abilities, item/companion synergies, and possible evolutions/forms; they can define a build.

## Pace, unlocks, exploration, familiars, and run ending

6. **Pacing — C + D (confirmed):** speed-focused play and thorough exploration should both be rewarded. No forced timer; fast play should come from skill, while players can also slow down and explore.
7. **Unlock progression — C (confirmed):** prioritize unlocking new possibilities without making later runs automatically easy. This does not cancel the earlier decision that some permanent progression may exist; its exact implementation and balance remain OPEN.
8. **Exploration rewards — D (confirmed):** items, currency, unique familiars/secrets, and permanent unlocks are all possible rewards. Stronger rewards may require greater risk. Exploration should remain optional.
9. **Familiar limit — direction agreed, exact cap OPEN:** there should be an upper limit, with build trade-offs. Examples discussed: several companions with few/no special powers, or fewer companions with stronger abilities/equipment. Do not choose a numeric cap or exact slot rules without further design.
10. **After final boss — D (confirmed):** a standard victory can end the run, with optional continuation into a harder/escalating challenge. Long-term ambition: many floors, many bosses, and many unlocks.

## Floors, rooms, bosses, difficulty, and items

11. **Floor structure — specific rule confirmed:** each floor has a maximum of 30 rooms. After each cleared eligible room, the game rolls a chance that the *next* room will contain the descent/exit; the player must clear that room before using the exit. The chance rises with room progress. At room 20 the chance reaches 100%, so the exit appears in room 21; the player may descend or keep exploring. Room 30 guarantees the exit and a bonus item. There is no boss on floor 1. Starting from floor 2, a boss fight happens at the beginning of each new floor, in room 1.
12. **Floor variety — D (confirmed):** floors should vary in appearance, enemies, difficulty, mechanics/hazards, events, secrets, rewards, and ways they affect combat/builds.
13. **Bosses — D (confirmed):** range from simpler build checks to distinctive pattern-based fights, multi-phase bosses, weak points, special mechanics, hidden bosses, and optional superbosses.
14. **Difficulty scaling — C (confirmed):** introduce new threats, enemy types, and harder bosses; avoid relying excessively on inflated enemy stats.
15. **Item rarity and roles — D (confirmed):** ordinary items can be central to a powerful build; items have distinct offensive, defensive, utility, and mechanics-changing roles. Include transformative effects and exceptional synergies.

## Future modes — backlog only; do not implement now

- **Sandbox / Creative mode:** let players place/select mobs, try item combinations and synergies, assemble builds, and test combat freely.
- **Auto-Battle / Manager mode:** a separate mode inspired by bullet-heaven games such as Vampire Survivors, but with autonomous movement and combat while the player manages builds, items, modifiers, and multipliers. It may need its own item types and balance rules.
- Both are future ideas, not part of the current implementation scope. Revisit only when the core game is ready and the user explicitly prioritizes these modes.

## Design principles and open points

- Prefer many meaningful floors, bosses, unlocks, and discoveries over repetitive content or stat inflation.
- Speed and exploration must both be valid strategies.
- Meta-progression should open choices, not remove the challenge.
- Keep RNG variable but effects and rules understandable and consistent.
- Exact familiar cap/slots, precise progression upgrades, probabilities beyond the existing room rule, final floor count, and the implementation order of future modes remain OPEN.
- This is a design log, not a claim that all described systems already exist in the playable prototype.


## Interakcja i wybór stylu — 2026-10-19

- **Pokój startowy:** usuń oferty/pickupy przedmiotów z pierwszego pokoju; zachowaj 3 serca i 2 monety jako zapasy startowe.
- **Podnoszenie przedmiotów:** przedmiot zbiera się automatycznie dopiero po wejściu w jego obszar kolizji. Nie wymaga osobnego klawisza interakcji; samo podejście na odległość nie wystarcza.
- **Style startowe:** style strzelania i ruchu muszą różnić się nie tylko nazwą/liczbami, ale też czytelnym wyglądem w menu i podczas gry. Różnice mają być widoczne bez zmiany kierunku całej gry.


## Item catalogue — 2026-10-19
- **Implemented (presentation only):** replaced generic `Item 1` labels with 30 distinct Polish names and category-appropriate icons.
- **No gameplay/balance changes:** effects, values, drop logic, and item behaviour were not changed by this naming pass.
- **OPEN:** thematic naming and long-term item identities can be revised later as the full item catalogue, rarities, transformations, and synergies are designed. Names do not imply that synergies or rarity systems exist yet.


## Meta-progresja i śmierć — decyzje z 2026-10-19
- **D01 — Siła gracza:** potężne buildy są pożądane, ale bossowie i zagrożenia nadal wymagają uwagi i umiejętności.
- **D02 — Synergie:** docelowo wspierane są synergie liczbowe, zmiany mechaniki oraz rzadkie kombinacje, które mogą odmienić build.
- **D03 — Familiars:** elastyczne buildy od wielu słabszych stworzeń po kilku potężnych przywołańców; własne umiejętności, synergie, ewolucje i formy. Limit i sloty pozostają OPEN.
- **D04 — Odkrycie a odblokowanie:** odkrycie zapisuje się natychmiast, ale część elementów wymaga osobnego wyzwania lub warunku odblokowania.
- **D05 — Aktywna ochrona:** dopuszczone są ratunki wymagające timingu oraz ochrona uruchamiana z wyprzedzeniem.
- **D06 — Limity ratunków:** mechanizmy ratunkowe mają być ograniczone, mieć koszty/warunki i zależeć od buildu. Dokładne liczby OPEN.
- **D07 — Tryby:** każdy tryb ma własne zasady śmierci i progresji. Sandbox/Creator i Auto-Battle/Manager pozostają poza bieżącym zakresem, dopóki użytkownik ich osobno nie priorytetyzuje.
- **D08 — Stałe bonusy:** ograniczone ulepszenia statystyk mogą być zdobywane za osiągnięcia; specjalizacja jest opcjonalna. Wartości, koszty i limity OPEN.
- **Robocze zasady śmierci:** przedmioty/build i waluta z bieżącego runu przepadają; trwałe odblokowania, odkrycia i postęp długoterminowy zostają. Katalog rozróżnia odkrycie od odblokowania.
- **Wdrożone w tej partii:** lokalny profil zapisuje liczbę rozpoczętych runów, śmierci, łączne zabójstwa, najlepszy postęp, odkryte przedmioty i poznanych wrogów. Ekran śmierci pokazuje straty z runu, a Kodeks pokazuje zachowane odkrycia.
- **OPEN / jeszcze niewdrożone:** warunki konkretnych odblokowań, system ulepszeń statystyk i specjalizacji, synergie gameplayowe, familiars/ewolucje oraz szczegółowe mechaniki ratunkowe. Nie wprowadzamy arbitralnych kosztów, cooldownów ani limitów.


## Startowy arsenał i sterowanie ruchem — wdrożenie 2026-10-19
- **Decyzja użytkownika:** odłożyć ekran „Kodeks / Trwały Postęp” na późniejszy etap; usunąć Shift jako osobny klawisz uniku; urozmaicić style ruchu i dodać trzy bronie dostępne już na starcie.
- **Wdrożone:** Kodeks nie jest pokazywany w interfejsie startowym; kod zapisu profilu pozostaje nietknięty, aby nie usuwać wcześniejszych danych przed decyzją o docelowej meta-progresji.
- **Wdrożone:** Shift nie uruchamia już uniku. Styl „Skoczek” ma automatyczne krótkie susy podczas ruchu, a „Zwinny” automatyczne zrywy; pozostałe style zachowują własną obsługę pędu.
- **Wdrożone:** wybór startowej broni zawiera 7 stylów: Klasyczny, Precyzyjny, Rozrzut, Szybkostrzelny, Salwa (5 pocisków), Przebijający (przechodzi przez wrogów) i Wybuchowy (obrażenia obszarowe przy trafieniu).
- **Do weryfikacji w dalszym balansowaniu:** obrażenia, szybkostrzelność i siła broni są wartościami prototypowymi; nie uznajemy ich za finalny balans.

## Ratunek przed śmiercią — wdrożenie 2026-10-19
- **D05 — wdrożony pierwszy mechanizm:** `Amulet Ostatniej Szansy` jest jednorazowym przedmiotem pasywnym. Gdy cios obniży HP do zera lub mniej, amulet zużywa się i pozostawia gracza z 1 HP; run trwa dalej.
- Amulet jest możliwą nagrodą bonusową w pokoju 30. Nie zmieniono efektów istniejących 30 przedmiotów.
- **OPEN:** aktywna ochrona wymagająca timingu oraz ochrona uruchamiana z wyprzedzeniem; sterowanie, cooldowny, koszty i zależność od buildu wymagają dalszych decyzji.
