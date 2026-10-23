### Decyzja z 2026-10-23: audyt ekonomii i diagnostyka śmierci
- Jedno źródło prawdy dla salda: `changeCoins(delta)`; osobno zapisujemy sumę wpływów i wydatków runu.
- Śmierć w trybie one-hit ma ujawniać nie tylko typ źródła, lecz także współrzędne i kontekst kolizji, o ile są dostępne.
- Jeśli raport wskazuje dystans większy niż suma promieni, to jest konkretny błąd kolizji do naprawienia; nie zgadujemy przyczyny bez danych.

## BIEŻĄCY KONTEKST IMPLEMENTACJI — 2026-10-23

- Decyzja z 2026-10-23: **Śrutownik** zastępuje Precyzyjnego w dostępnym arsenale; strzela pojedynczym pociskiem co 6 klatek, z losowym odchyleniem ±0,13 rad. Nie emituje salwy wielu pocisków.
- Pokój grywalny zwiększono do 900×540 px; osłony to 3 formacje na pokój z promieniem kamieni 18.
- Przyczyna trafienia musi być widoczna na ekranie śmierci, by diagnozować zgłoszenia o „niewidzialnym” zagrożeniu. Pułapki podłogowe nie zadają obrażeń w trybie Hotline.
- Monety są walutą runu, nie trwałą: HUD pokazuje „MONETY (RUN)”.



Ten dziennik zapisuje decyzje projektowe i historię zmian, nie gwarantuje, że każda opisana niżej decyzja nadal jest aktywna. Dla bieżącej implementacji nadrzędne są aktualny `index.html`, testy oraz blok „STATUS AKTUALNY” w `PROJECT_STATUS.md`.

- Eksperyment Hotline Miami: 10 pokojów na piętrze, siatka 5×2, boss w pokoju 10; pokoje 1–9 muszą być oczyszczone. Starsze wpisy o 30 pokojach, losowych wyjściach i bossie w innych pokojach są historyczne.
- Wybory gracza: ruch **Drifter / Skoczek**; strzelanie **Śrutownik / Klasyk / Salwa**. Stare nazwy archetypów gracza/arsenału nie oznaczają, że te opcje są obecnie dostępne.
- Zasada walidacji: automatyczne testy i Chromium nie zastępują ręcznego playtestu; nie zapisuj subiektywnej jakości ruchu ani balansu jako potwierdzonej bez takiego testu.

---

# Crypt Crawler — Decision Log
Updated: 2026-10-19
Purpose: durable record of design decisions agreed in chat. This document records intent; it does not mean every feature is implemented.

## Research-backed combat iteration — 2026-10-19
- **Player preference evidence:** Dead Cells developers describe weapons as worthwhile when they have distinct purpose, feel, effects and play-style changes, not merely different damage numbers. Source: https://www.gamedeveloper.com/design/designing-each-of-the-50-weapons-in-i-dead-cells-i-to-feel-distinctive
- **Community feedback evidence:** Brotato players praise build/weapon variety but some criticize options that feel mechanically similar or are so weak that they become false choices. Sources: https://www.metacritic.com/game/brotato/user-reviews/ and https://steamcommunity.com/app/1942280/discussions/0/651430371783646078/
- **Design rule:** make each starter weapon communicate its role and trade-off; avoid adding cooldowns just for the sake of having them. Core automatic fire remains responsive, while firing intervals can differ by weapon.
- **Implemented:** starter selection shows per-projectile damage multiplier and actual firing interval in game frames.
- **Balance pass 2026-10-19:** lowered Spread from `0.62` to `0.40` damage per projectile and Salwa from `0.42` to `0.25`. Before this, the projectile count gave these weapons theoretical raw single-target DPS of about 1.50× standard. With current values, Spread is about 0.97× standard and Salwa about 0.89×, before hit chance and their multi-target advantages. This preserves the reason to choose them (coverage) without letting projectile count alone dominate.
- **Caveat:** piercing and explosive damage are not captured by raw single-target DPS; their multi-target value needs actual playtesting. Research supports avoiding dominant/false choices, but does not prove these exact numbers are final.
- **OPEN:** weapon balance remains provisional until hands-on playtesting.
- **Regression coverage added 2026-10-19:** browser smoke tests now exercise the real projectile collision/update loop: Piercing damages at most three targets; Explosive deals full damage to its primary target and 60% damage to other enemies within 72 px. These tests protect existing behavior and do not claim the final balance is settled.
- **Player preference evidence:** Dead Cells developers describe weapons as worthwhile when they have distinct purpose, feel, effects and play-style changes, not merely different damage numbers. Source: https://www.gamedeveloper.com/design/designing-each-of-the-50-weapons-in-i-dead-cells-i-to-feel-distinctive
- **Community feedback evidence:** Brotato players praise build/weapon variety but some criticize options that feel mechanically similar. Sources: https://www.metacritic.com/game/brotato/user-reviews/ and https://www.reddit.com/r/brotato/comments/1le5h5o
- **Design rule:** make each starter weapon communicate its role and trade-off; avoid adding cooldowns just for the sake of having cooldowns. Core automatic fire remains responsive, while firing intervals can differ by weapon.
- **Implemented:** starter selection now shows per-projectile damage multiplier and the actual firing interval in game frames. Values are calculated from each weapon's current `rate` multiplier, which is also used by gameplay. This is clarity/readability work, not a major balance change.
- **OPEN:** weapon balance remains provisional until hands-on playtesting; do not claim the research proves exact numeric damage/cooldown values.

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


## Płynność ruchu — iteracja 2026-10-20
- **Cel:** sterowanie ma być równie przyjemne i płynne jak w dobrych twin-stick/room-based roguelike'ach, ale nie ma kopiować 1:1 TBoI ani Enter the Gungeon.
- **Zakres:** wyłącznie parametry i testy fizyki ruchu; brak zmian animacji, grafiki i mapowania sterowania. Zachować odrębne role stylów.
- **Zmiana prototypowa:** Drifter szybciej reaguje na kierunek i ma wyraźniejszy poślizg po puszczeniu wejścia; Momentum rozpędza się szybciej niż wcześniej. Testy mierzą osiąganie prędkości, zmianę kierunku, coast i normalizację ruchu po skosie.
- **OPEN:** ostateczne odczucie wymaga ręcznego testu z klawiaturą; automatyczne testy nie potrafią same potwierdzić, że ruch jest przyjemny.


## Test regresyjny modyfikatorów terenu — 2026-10-20
- Dodano w `tests/browser_smoke.py` test uruchamiający rzeczywistą funkcję `update()` z kontrolowanym stanem gracza na zwykłym terenie, piasku i lodzie.
- Test chroni istniejące mnożniki ruchu: piasek ×0,62 oraz lód ×1,25, a także sprawdza powrót do normalnej prędkości po wyjściu z pola.
- To wyłącznie test regresyjny: kod produkcyjny, fizyka, grafika, animacje i balans broni pozostają bez zmian. CI przeszło na SHA `9b04a069a3ea0b1c6e1c78a04253882f41000f0a`; ręczny test klawiaturą nadal pozostaje OPEN jako ocena subiektywnego odczucia sterowania.
- Uwaga o procesie: pierwsze dwa przebiegi CI wykazały błędy konfiguracji nowego helpera testowego; zostały poprawione, a trzeci przebieg na powyższym SHA zakończył się sukcesem.


## Czytelność HUD, drzwi, sklepu i ról — 2026-10-20
- **HP:** zdrowie musi być widoczne na samej planszy przez cały run; dodano stały panel z liczbą HP i paskiem zdrowia.
- **Drzwi:** etykiety zwiększono z 10 px do 20 px i przeniesiono na tabliczki wewnątrz pokoju, aby nie leżały na samym przejściu.
- **Sklep:** osobny pokój, bez zakupów przez kliknięcie UI. Serce leży na podłodze i kupuje się automatycznie po wejściu w kontakt, jeśli gracz ma co najmniej 2 monety i brakuje mu HP. Cena 2 monety / leczenie 2 HP pozostają bez zmian.
- **Log:** pickupy i zmiany każdej statystyki nie powinny tworzyć historii komunikatów; zachowujemy pojedynczy status ważnego zdarzenia, bez logowania podniesienia przedmiotu.
- **Ruch:** każdy styl ma jawne plusy i minusy. Taran dostaje rzeczywistą redukcję obrażeń 25% i niższą prędkość. Nie przywracamy aktywnego uniku.
- **Broń:** pozostaje 7 wyborów, ale zbalansowanych pod różne role; ekran wyboru pokazuje obrażenia, teoretyczny DPS i plusy/minusy. Wartości są nowym punktem startowym, nie finalnym balansem.

- Sklep zawiera trzy oferty na podłodze: losowy przedmiot pasywny za 4 monety, losowy aktywny za 5 monet oraz serce za 2 monety (+2 HP). Ceny są wartościami prototypowymi do późniejszego testu ekonomii; wszystkie zakupy odbywają się przez kontakt z ofertą, bez myszy.

## Czytelność UI, mapa i zachowanie przeciwników — 2026-10-21
- Dodano stałe przyciski **BROŃ: ... · ZMIEŃ** i **RUCH: ... · ZMIEŃ** poza planszą. W trakcie runu wybór broni wraca bezpośrednio do gry i nie wymusza ponownego wyboru ruchu; skrót **B** otwiera wybór broni, **M** otwiera mapę piętra, a **V** wybiera ruch.
- Ekrany wyboru mają responsywny układ trzech kolumn na szerokim ekranie, przewijanie w obrębie overlayu i mniejsze odstępy, żeby karty nie wychodziły poza planszę.
- Interfejs i arena dostały spokojniejszą, stonowaną paletę ziemi/kamienia, prostsze obramowania i bardziej klasyczny, oldschoolowy charakter RPG. To tymczasowy placeholder graficzny, nie finalne assety.
- Opis przedmiotu/sklepu używa większej czcionki 13–14 px i dynamicznego łamania tekstu.
- Dodano niewielką mapkę pokoju w prawym górnym rogu: gracz, przeciwnicy i drzwi są oznaczeni osobnymi punktami.
- Ruch wrogów rozdzielono na sześć ról: bezpośredni pościg (chaser), krążenie (spitter), ciężki ruch z fazami przyspieszenia (brute), szarża (dasher), boczne manewry (hexer) i boss z krótkimi szarżami.
- Testy Chromium sprawdzają przyciski wyboru w trakcie runu, obecność mapki, czytelność tekstu i odmienne role ruchu. Ręczny test rozgrywki nadal potrzebny do oceny odczuć i balansu.


## Nagroda bossa i mocniejsze trade-offy — 2026-10-21
- Boss gwarantuje losowy przedmiot z puli statystyk/ruchu/strzelania; nie wypuszcza monet ani serc, a zabójstwo bossa nie uruchamia bonusu monetowego za serię.
- W pokoju bossa wskazane są specjalne złote drzwi; po zwycięstwie gracz musi do nich dojść, aby wejść na kolejne piętro.
- Log zachowuje informację o nowym piętrze i celu bossa, zamiast nadpisywać ją zwykłym opisem pokoju.
- Style ruchu i strzelania otrzymały wyraźniejsze plusy/minusy. Stalowe Obcasy zostawiają krótko działające pola raniące przeciwników; rozmiar pocisku z itemu Pocisk Oblężniczy jest już obsługiwany.
- Powiększono tekst ofert sklepu; wartości balansu pozostają prototypowe i wymagają ręcznego playtestu.


## 2026-10-21 — eksploracja lochu
- Każde piętro ma stałą siatkę 6×5. Położenie pokoju wyznacza jego ID; przejście przez drzwi prowadzi tylko do pola obok, a ruch wstecz prowadzi do wcześniej odwiedzonego pola.
- M jest przypisane do pełnej mapy piętra; zmiana stylu ruchu odbywa się przyciskiem RUCH, a broń przyciskiem BROŃ lub klawiszem B.
- Pokoje oczyszczone są oznaczane w bieżącej rozgrywce i pozostają bez wrogów przy powrocie.
- Teren: kolizyjne kamienie i dziury z okresowym obrażeniem/spowolnieniem; odpychające wentylatory zostały wycofane w pakiecie spawn/vent.


## Korekta progresji zejścia — 2026-10-21
- W siatce 6×5 numer pokoju oznacza pozycję, nie kolejność eksploracji. Szansa na zejście rośnie więc na podstawie liczby unikalnych oczyszczonych pokojów na bieżącym piętrze (+5 pp za każdy), a nie na podstawie `roomNo`.
- Licznik ignoruje ponowne wejście do już oczyszczonego pokoju. Po 20 unikalnych oczyszczonych pokojach szansa wynosi 100%; gwarantowane wyjście z pokoju 30 pozostaje osobną regułą.


## Trwałość wyjścia piętra — 2026-10-21
- Po wylosowaniu zejścia lokalizacja jest stała przez całe piętro. Backtracking odtwarza to samo oznaczenie drzwi, a wejście do sklepu nie przenosi oznaczenia na drzwi powrotne.
- Wyjście bossa i graniczne wyjścia pokoju 30 także są traktowane jako lokalizacje, a nie jednorazowy efekt rysowania pokoju.


## Wyjście bossa — lokalizacja trwała (2026-10-21)
- Pokonanie bossa zapisuje `floorExitRoomId` i `floorExitSide` wraz z oznaczeniem drzwi. Nie wystarcza samo jednorazowe `floorExit=true`, bo pokój jest rysowany/konfigurowany ponownie przy powrocie.


## Stan pokoju podczas backtrackingu — 2026-10-21
- Każdy pokój na piętrze ma migawkę pod kluczem `piętro:ID pokoju`, zapisywaną przy opuszczeniu. Obejmuje drzwi, dropy, teren, źródła ognia, przeszkody, przeciwników i ich pociski.
- Sklep jest osobnym widokiem/obszarem i nie może zapisywać swojego stanu pod kluczem pokoju, z którego gracz do niego wszedł.


## Progresja w siatce — 2026-10-21
- ID pokoju identyfikuje pozycję, nie kolejność przejścia. Skalowanie liczby wrogów korzysta z pasma `floor((x+y)*5/9)`, które rośnie wraz z odległością od pokoju startowego.
- Zachowujemy ogólny zakres progresji (0–5 pasm), ale usuwamy przypadkowe skoki wynikające z przejścia z ID 6 na 7 lub między wierszami.


## Powrót do pokoju a poziom trudności — 2026-10-21
- `roomTier` należy do stanu pokoju. Przywracanie migawki odtwarza jego poziom, co zachowuje spójność HUD-u i mnożnika łupu po wejściu do sklepu i powrocie.


## Sklep jednorazowy na piętro — 2026-10-21
- Po wykorzystaniu sklepu drzwi wejściowe zostają zwykłymi drzwiami przy każdym ponownym wejściu do pokoju. Nie można odświeżać ofert przez ponowne otwieranie sklepu.


## Proceduralny układ lochu i mocniejsze specjalizacje — 2026-10-21
- **Sterowanie:** M = mapa piętra, V = wybór ruchu, B = wybór broni. Nie przywracamy Shift jako uniku.
- **Topologia:** każde piętro generuje połączony graf 30 pokojów na siatce 6×5. Losowe drzewo gwarantuje osiągalność każdego pokoju, a niewielka szansa na dodatkowe połączenia tworzy skróty/pętle. Drzwi fizyczne i linie mapy muszą używać dokładnie tego samego grafu.
- **Pokój 30:** gwarantowane zejście pokazuje się tylko przy krawędziach planszy. Brak korytarza między dwoma sąsiadami nie może być pokazywany jako drzwi.
- **Ruch:** mocne role (precyzyjny Biegacz, szybki i ślizgający Drifter, cykliczny Skoczek, bardzo szybki lecz bezwładny Rozpęd, wolny zrywający Zwinny, opancerzony lecz ciężki Taran). Wartości numeryczne pozostają prototypowe.
- **Broń:** Precyzyjny = duży pojedynczy strzał i długa przerwa; Rozrzut = mocny z bliska, słaby z daleka; Szybkostrzelny = częste słabe trafienia; Salwa = duży potencjał wielopociskowy i długa przerwa; Przebijający = linie wrogów; Wybuchowy = mocny pocisk i obszar kosztem prędkości; Klasyczny = opcja stabilna bez specjalizacji.


## Wizualna mikro-rewolucja i sterowanie — 2026-10-21
- Kierunek: autorskie, czytelne sylwetki fantasy (wilkołak, wiedźma, ogr, wampir, mumia, smok; rzadziej krasnolud i krowa), bez kopiowania rozpoznawalnych postaci z istniejących gier.
- `M` służy wyłącznie do mapy; zmianę stylu ruchu przypisujemy do `Q`. `WASD` porusza postacią, strzałki strzelają kierunkowo, LPM strzela do kursora.
- Ruch ma mocne kompromisy mechaniczne, nie tylko różnice prędkości. Strzelanie ma być bardziej wybaczające, dlatego poprawiamy wielkość hitboxa i czas życia pocisków oraz zmniejszamy nadmierny rozrzut.
- Generowana mapa ma pokazywać rzeczywiste połączenia, a stan nieodwiedzonych pokoi powinien być wizualnie odróżniony od odwiedzonych.


## Motywy proceduralnych pięter — 2026-10-21
- Każde piętro cyklicznie używa innego autorskiego motywu wizualnego: zarośnięta krypta, grota grzybów, kuźnia popiołu, lodowa świątynia, krwawy księżyc.
- Motyw zmienia paletę, detale płytek, runy i światło. Wzory są deterministyczne i czysto wizualne; nie mają wpływu na hitboxy ani topologię lochu.


## Sterowanie i rozdzielenie ról broni — 2026-10-21
- Zatwierdzony w kodzie skrót wyboru ruchu to **V**; **M** jest wyłącznie mapą, a **B** wyborem broni. Nowszy kod oraz instrukcja są źródłem prawdy nad starszymi notatkami, które przez chwilę wymieniały Q.
- Drifter zostaje szybki i lekko bezwładny, ale po puszczeniu kierunku traci pęd szybciej (0,70 na klatkę). Rozpęd zostaje wolniejszy w reakcji na nowe wejście (współczynnik 0,14), ale mocniej hamuje po puszczeniu kierunku (0,65). To zachowuje ich rolę, a usuwa długi, niekontrolowany poślizg.
- Rozrzut oraz Salwa nie mogą być dwiema odmianami tego samego wachlarza. Rozrzut: szerokie ±0,42 rad, śrut ×0,50, krótki dystans. Salwa: wąskie ±0,07 rad, pociski ×0,62, większa prędkość pocisków i długa przerwa między seriami — średni dystans i skupienie na jednym celu.
- Wartości są iteracją prototypową. Decyzja o ich finalności wymaga pomiaru TTK/obrażeń oraz ręcznego playtestu; testy automatyczne nie dowodzą przyjemności sterowania.

## Sterowanie i odrębne style uniku — 2026-10-21

- W aktualnym kodzie obowiązuje **M = mapa, V = wybór stylu ruchu, B = broń**. W PROJECT_STATUS.md znaleziono stary zapis o Q; poprawiono go w tej iteracji.
- Skoczek i Zwinny nie mogą mieć tego samego automatycznego zrywu. Skoczek zachowuje rytmiczny sus co 22 klatki. Zwinny uruchamia krótki zryw ochronny tylko po ostrym skręcie, z 24-klatkowym odnowieniem i +10% otrzymywanych obrażeń.
- Usunięto okrągły ring przy zrywie, który wyglądał jak przypadkowe kółka. Feedback jest kreskowy i kierunkowy, nie kołowy.
- Nie dodawać osobnego klawisza Shift do uniku bez uzgodnienia; to nie jest wymagane do rozdzielenia tych archetypów.
- Research: w dyskusjach graczy ETG często powtarza się, że zwykłe omijanie pocisków jest ważniejsze niż spamowanie rollem, a roll powinien być narzędziem sytuacyjnym; część graczy wskazuje też na trade-off: mysz daje precyzję celowania, pad daje wygodę kierunków ruchu. Źródła: https://www.reddit.com/r/EnterTheGungeon/comments/1t4crf0/dificuldade_em_desviar/ ; https://www.reddit.com/r/EnterTheGungeon/comments/1dc0fgy/ ; https://enterthegungeon.wiki.gg/wiki/Dodge_Roll_%28Move%29 . W Isaac gracze wprost opisują bezwładność po puszczeniu klawisza jako coś, co część osób lubi, a innych frustruje: https://www.reddit.com/r/bindingofisaac/comments/18om7ee . To jakościowe przykłady opinii, nie reprezentatywna ankieta.


## 2026-10-22 — tymczasowy limit piętra i boss
- Decyzja użytkownika: na czas kolejnego eksperymentu zmniejszyć liczbę pokojów piętra z 30 do 10; po dziewięciu pokojach kolejnym obowiązkowym pokojem jest boss, a zejście na niższe piętro odblokowuje się po jego pokonaniu.
- Implementacja: proceduralna siatka 5×2 z 10 węzłami; boss w pokoju 10 na każdym piętrze; brak losowych zejść przed bossem.
- Wymóg: po weryfikacji zachować osobną gałąź backupową tej dokładnej wersji przed rozpoczęciem dużego eksperymentu. To zmiana tymczasowa, nie nowa nieodwracalna reguła produktu.


## 2026-10-22 — eksperymentalna walka w stylu Hotline Miami
- Użytkownik wybrał duży eksperyment: Crypt Crawler ma zachować własną tożsamość i progresję 10-pokojową, ale walka ma być szybka i śmiertelna, z osłoną, pogonią i reagowaniem na hałas.
- Backup przed eksperymentem: `backup/pre-hotline-miami-2026-10-22`, commit `b26b5d913fb06d0f124d92a9a17d24ae031df91c`. Nie nadpisywać tej gałęzi eksperymentem.
- Prototyp: jedno życie gracza; zwykli przeciwnicy giną od jednego trafienia; boss jest wyjątkiem wielotrafieniowym; kamienie blokują LOS/pociski i kolidują z ruchem; strzały tworzą krótkotrwały hałas; wróg strzela tylko przy czystej linii widzenia.
- Wnioski: adaptować szybki restart, czytelne reguły i swobodę rozwiązywania starć z HLM1 oraz różnorodność przeciwników/układów z HLM2; unikać strzałów spoza ekranu i niespójnego AI.
- Źródła i acceptance criteria w `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md`.
- Doprecyzowanie eksperymentu: R w czasie gry/po śmierci natychmiast rozpoczyna nową próbę z zachowaną bronią i ruchem. Serca w trybie jednego życia dają pierwszy amulet ratunkowy, kolejne zamieniają się w monety; sklep sprzedaje amulet zamiast dodatkowego HP.


## 2026-10-22 — doprecyzowanie zasad prototypu Hotline
- Research rozszerzony o recenzje GameSpot, PC Gamer, GamesRadar, Pocket Gamer oraz jakościowe dyskusje Reddit. Powtarzające się motywy: one-hit lethality, szybki restart, hałas jako trade-off, użyteczna geometria i swoboda rozwiązań; ostrzeżenia: strzały spoza czytelnego pola widzenia i niespójne AI.
- Źródła i konkretne zasady implementacji znajdują się w `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md`.
- Walidacja automatyczna dla main HEAD `6ae4fb9630dfb90f43c260eaeb6743a8f703676b` jest zielona (run 39808650676); mirror deployment jest zielony (run 39806755919), a backup pozostaje na `b26b5d913fb06d0f124d92a9a17d24ae031df91c`.
- Ręczny playtest nie został wykonany. Nie uznawać ścieżkowania AI ani fairness za potwierdzone bez obserwacji.

## 2026-10-22 — live audit eksperymentu Hotline
- Ponowny audyt potwierdził najnowszy dokumentacyjny HEAD `a497bc64f85bc1eb593a069eb0cdc08b52ebca75` oraz niezmieniony backup `b26b5d913fb06d0f124d92a9a17d24ae031df91c`.
- Run Chromium dla dokładnego HEAD został anulowany; job ponowiono. Dopóki wynik ponowienia nie będzie sukcesem, nie twierdzić, że najnowszy HEAD ma pełne zielone CI. Kodowy poprzednik `6ae4fb9630dfb90f43c260eaeb6743a8f703676b` ma zielony run `39808650676`.
- Zweryfikowano zgodność SHA i treści ośmiu plików SSOT/mirror. Pages deployment oraz mirror browser smoke zielone na mirror HEAD `da343edaeedd6bb6c35ea8265ac6c8190bf580e0`.
- Brak ręcznego playtestu pozostaje jawnym ograniczeniem. Nie wprowadzać balansowych wniosków o pathfindingu/fairness bez testu człowieka.

## 2026-10-22 — iteracja czytelności walki
- Mapa piętra musi być wyśrodkowana i jasno odróżniona od mini-podglądu aktualnego pokoju; M pozostaje skrótem do pełnej mapy, V do stylu ruchu, B do broni.
- Wrogowie dystansowi w trybie śmiertelnym mają ujawniać linię strzału przez krótki windup przed wystrzałem. To ma poprawić czytelność zagrożenia, a nie osłabiać pocisków ani zmieniać zasad one-hit.
- Gdy kamień blokuje bezpośrednią trasę, przeciwnik powinien próbować obejścia przez punkt styczny. Implementacja jest heurystyczna; jeśli testy ręczne pokażą oscylowanie lub utknięcia przy kilku kamieniach, kolejnym krokiem będzie prosty lokalny pathfinding, nie podbijanie statystyk wrogów.
- Wszystkie trzy zachowania wymagają zielonego CI i ręcznej oceny; automatyczne testy są tylko regresyjnymi kontraktami.


## 2026-10-22 — windup z zablokowanym celowaniem (eksperyment)
- Zwiększyć okno ostrzeżenia z 10/16 do 18/24 klatek (zwykły strzelec/boss) jako hipotezę do testu, nie jako finalny balans.
- Linia ostrzegawcza musi odpowiadać miejscu/kierunkowi, do którego faktycznie poleci pocisk. Nie śledzić gracza bez końca podczas windup, bo wtedy strafe nie daje czytelnej możliwości uniknięcia ataku.
- Jeśli linia do zapisanej pozycji jest zasłonięta kamieniem, anuluj windup. Nie zmieniaj reguły one-hit ani obrażeń pocisku.


## 2026-10-22 — wynik walidacji windup
- PR #56 scalono po zielonym CI dla dokładnego SHA `2b3aadfa41fa5a197a0319534430f298fbc92038`; main run `39824282975` również zakończył się sukcesem.
- Test Chromium potwierdził windup 18 klatek, jeden pocisk po windup oraz zablokowany kierunek po sidestepie. To potwierdza implementację, nie subiektywną uczciwość walki.
- W workflow testowym usunięto `--with-deps`, ponieważ logi wykazały bardzo wolne pobieranie pakietów APT na runnerze. Instalacja Chromium bez ponownej instalacji zależności systemowych pozwoliła zakończyć pełny test.
- Mirror został zsynchronizowany, wszystkie 9 współdzielonych plików ma identyczny blob SHA/treść. Mirror browser smoke jest zielony; deployment Pages trzeba potwierdzić osobno.
- Ręczny playtest pozostaje niewykonany.


## 2026-10-22 — regresja dwóch osłon
- Zamiast od razu przepisywać heurystykę na A*, dodano test rzeczywistej pętli gry dla dwóch kolejnych kamieni blokujących prostą trasę.
- Test przechodzi: dystans do celu spada do 1,79 px w 180 klatkach, a przeciwnik zachowuje wymagany odstęp od obu skał. To ograniczony test regresyjny, nie dowód ogólnej poprawności AI.
- Jeśli ręczny playtest lub dalsze scenariusze pokażą utknięcia, następnym krokiem będzie lokalny pathfinding uwzględniający kilka przeszkód.


## 2026-10-22 — uzgodnienie dokumentacji z bieżącym kodem
- Audyt wykazał, że README i część sekcji handoff/prompt opisywały poprzedni wariant (30 pokojów, 6×5 oraz starsze skróty). Bieżący `index.html` ma 10 pokojów w siatce 5×2, bossa w pokoju 10, M=mapa, V=ruch, B=strzelanie i śmiertelność jednego trafienia.
- Zaktualizowano README, handoff i prompt kolejnej sesji; historyczne notatki pozostają jako historia, lecz nowy blok statusu wyraźnie wskazuje aktualny stan.
- Nie zmieniono mechaniki gry w tej iteracji — tylko dokumentację, aby ograniczyć ryzyko podejmowania kolejnych prac na podstawie sprzecznych założeń.


## 2026-10-22 — brak bezużytecznego leczenia w trybie one-hit
- Audyt wykazał, że Mała/Wielka Apteczka oraz dwa przedmioty zwiększające HP zachowywały stare efekty leczenia, mimo że w Hotline mode dowolne trafienie zeruje całe zdrowie. Były więc funkcjonalnie bezużyteczne.
- W trybie one-hit te cztery przedmioty dają amulet ratunkowy, jeśli gracz go nie ma; duplikat zamieniają w 2/3 monety. W trybie standardowym zachowują dotychczasowe działanie.
- Dodano regresję Chromium dla obu rodzajów przedmiotów, przypadku bez amuletu i duplikatu oraz czytelności opisów. To chroni użyteczność mechaniki, ale nie zatwierdza balansu ekonomii.

- Wynik walidacji: PR #59 scalony jako `05aa3c9e70da03d96d826493392e4ae45f7b109a`; CI main run `39826837619` zielony. Mirror smoke `39826896790` i Pages deployment `39826897083` zielone.


## Czytelność sklepu i osłon — 2026-10-22
- **Zgłoszenie użytkownika:** waluta wydawała się niesprawna, oferta sklepu znikała bez jasnej intencji zakupu, a kamienie były losowo rozrzucone i nie tworzyły użytecznych miejsc do ukrycia.
- **Decyzja UX:** dotknięcie oferty sklepu nie może wydawać monet. Zakup sklepowego przedmiotu lub amuletu wymaga pojedynczego naciśnięcia `E`, a etykieta pokazuje koszt. Zwykłe znajdźki nadal podnoszą się przez kontakt, żeby nie zmieniać ogólnego rytmu zbierania łupów.
- **Wyjaśnienie amuletu:** amulet ratunkowy automatycznie blokuje jeden śmiertelny cios i pozostawia 1 HP; zużywa się po aktywacji. W trybie jednego trafienia oferta za 2 monety kupuje tę ochronę, nie leczenie HP.
- **Decyzja level design:** zamiast kilku niezależnych, przypadkowych kamieni, pokoje Hotline używają skupionych formacji `U`, `X`, `L`, `I`, `T`. Formacje mają dawać zarówno osłonę przed linią strzału, jak i przestrzeń do obejścia; ich jakość nadal wymaga ręcznego playtestu.
- **Status:** PR #60 scalony do `main` jako `97d0b289f92f8651f4da0a8423a3832e63135b96`; browser smoke run `39830353160` zakończył się sukcesem. Ręczny playtest nadal otwarty.

## 2026-10-22 — Player collision with cover
- Decision: when a diagonal player step intersects a rock, attempt movement along each axis separately and retain a safe axis rather than reverting both coordinates. This should make cover feel less sticky while preserving rock collision.
- Validation required: deterministic Chromium regression, source verification, green CI on exact PR head. Manual feel is still unverified.


## 2026-10-22 — trzy style broni i dwa style ruchu

- **Decyzja:** z wyboru gracza usunąć wszystkie style strzelania poza Precyzyjnym, Klasykiem i Salwą. Pozostałe implementacje pocisków pozostają w kodzie, aby nie uszkodzić niezależnych systemów, ale nie są oferowane jako broń startowa.
- **Decyzja:** Precyzyjny ma wolniejsze, świadome strzelanie; Klasyk ma mniejszą szybkostrzelność i zasięg; Salwa ma twardy minimalny cooldown 150 klatek, także przy ciągłym przytrzymaniu przycisku.
- **Decyzja:** wybór ruchu gracza zawiera wyłącznie Driftera i Skoczka. Drifter ma kontrolowaną bezwładność; Skoczek ma wyraźniejszy skok z ograniczoną losowością cooldownu. Pozostałe definicje wewnętrzne nie są automatycznie usuwane, jeśli inne mechaniki nadal z nich korzystają.
- **Status testów:** osłony PR #63 i broń PR #64 przeszły browser smoke; ręczny playtest pozostaje otwarty.


## 2026-10-22 — cztery klasy przeciwników

- **Decyzja:** normalna pula przeciwników ma cztery czytelne role: Drifter (bezwładność), Skoczek (zryw z losowym, ograniczonym odstępem), Taran (ciężki, wytrzymały) i Biegacz (agresywny zryw). Boss pozostaje osobnym archetypem.
- **Decyzja:** Taran otrzymuje dokładnie +2 HP względem poprzedniej wartości bazowej 5, czyli bazowo 7 HP. Nie zwiększamy równocześnie jego prędkości ani obrażeń.
- **Ograniczenie trybu:** jednouderzeniowa eliminacja zwykłych przeciwników w Hotline pozostaje osobną regułą; wartość HP Tarana nadal jest poprawnie zdefiniowana i skalowana w systemie.
