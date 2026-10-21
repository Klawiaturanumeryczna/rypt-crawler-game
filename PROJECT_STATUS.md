# Crypt Crawler — PROJECT STATUS
Updated: 2026-10-19

## Latest implementation batch — persistent profile foundation
- Added a versioned browser-local profile (`cryptCrawlerProfileV1`) with run starts, deaths, lifetime kills, best floor/room, discovered items and encountered enemy types.
- Item discoveries are saved at pickup time and are independent of run inventory. Enemy types are recorded when encountered.
- Death screen explicitly reports coins and carried items lost in the run, while long-term profile records remain. The Codex / Persistent Progress screen exists in code but its entry button is currently hidden, per the user's decision to defer meta-progression UI.
- Added `Amulet Ostatniej Szansy`: a one-use passive item that consumes itself on a fatal hit and leaves the player at 1 HP. It can appear as the room-30 bonus reward; the existing 30 item effects are unchanged.
- This is the foundation only: exact unlock requirements, permanent stat upgrades/specializations, actual gameplay synergies, familiars/evolutions, and death-prevention abilities remain OPEN; no arbitrary balance values were introduced.

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
- Item catalogue pass: all 30 existing items now have distinct Polish names and category-appropriate icons. This is a presentation-only change; effects and balance remain unchanged. Synergies, rarity, transformations, and full item identities remain OPEN.
- Recent automated checks cover the starter room, contact-only pickup, all ten active-item effects/consumption, exit probabilities and placement, room-30 bonus, shop purchase, boss-room clearing and floor transition, six movement-physics styles, shooting projectile differences, and static invariants.
- Historical file hashes from an earlier sync (not current after subsequent changes; always fetch both repositories and compare current blob SHAs before relying on parity):
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
2. Define concrete unlock conditions and implement actual permanent unlocks / optional stat specializations.
3. Design familiar cap/slots and implement familiars, abilities, synergies and evolutions.
4. Implement item synergies and both active protection styles after control/cooldown/cost rules are agreed. The one-use automatic rescue item is implemented.
5. Expand floor identity, secrets/events and boss variety.
6. Next testing gap: longer multi-room/floor/boss runs and gameplay playtesting; automated smoke tests do not replace human gameplay testing.

## Fast, safe workflow for every session
1. Check latest commit on both default branches and latest relevant CI/deployment runs. Do this once at session start. The browser-smoke workflow pins Playwright 1.64.0 and caches pip packages plus Chromium to avoid repeat downloads.
2. Fetch only files relevant to the current task. Do not re-read every project file unless needed.
3. Before editing a synced file, fetch it from both repos and compare content/SHA. Treat private repo as source of truth unless live repo evidence shows otherwise.
4. Make a coherent batch of code, tests and documentation changes; avoid unnecessary commits that trigger duplicate CI runs.
5. Run static verification and browser smoke where relevant. Clearly distinguish static checks, browser smoke, CI, deployment, and actual human gameplay testing.
6. Synchronize the exact changed files to the public mirror only after confirming the intended source content; then verify both copies match.
7. Check the resulting CI/deployment status before claiming success. Never claim a test or gameplay session occurred unless it did.
8. Update this file only when durable state, priorities, or workflow materially changes. Keep it concise; put detailed design decisions in `DECISION_LOG.md` and balance data in `BALANCE_NOTES.md`.

## Current gameplay batch (2026-10-20)
- Movement feel pass: modestly increased Drifter's steering response while preserving a longer coast, and increased Momentum's acceleration. Added browser regression checks for time-to-95%-speed, direction reversal, coast, and diagonal speed. No animation/art/control mapping changes. Human playtesting still required.
- Added browser regression coverage for actual enemy HP creation: floor scaling, easy/hard door HP multipliers, and the floor-2 boss HP formula. This protects current prototype values; it does not establish that the balance is fun or final.

## Previous gameplay batch (2026-10-19)
- Starter weapon choice displays per-projectile damage multiplier and firing interval (frames), using the same values that govern actual weapon cadence.
- Research-backed first balance pass: Spread damage reduced to `0.40` per projectile and Salwa to `0.25`; static and browser-smoke checks now guard against projectile-count alone making their raw single-target DPS exceed the standard weapon. Exact balance remains provisional pending playtesting.
- Browser smoke now verifies real collision behavior for Piercing (three targets maximum) and Explosive (primary hit plus 60% splash damage within 72 px).
- Research basis: Dead Cells developer commentary emphasizes distinct weapon purpose/feel; Brotato player feedback praises build variety but warns against weapons that feel too similar. See `DECISION_LOG.md` for sources and caveats.
- Startowe bronie rozszerzone z 4 do 7 stylów: dodano Salwę, Przebijający i Wybuchowy.
- Usunięto aktywację uniku przez Shift; Skoczek i Zwinny korzystają z automatycznych zrywów, pozostałe style zachowują różnice w przyspieszeniu/pędzie.
- Ekran Kodeksu / Trwałego Postępu jest ukryty do czasu zaprojektowania pełnej meta-progresji. Kod profilu i lokalny zapis pozostają zachowane.
- Zmiany z gałęzi `feature/starter-weapons-movement` zostały scalone; publiczny mirror zsynchronizowany. Najnowszy odczyt CI nie zwrócił statusów uruchomień, więc testów tej ostatniej poprawki nie oznaczamy jako potwierdzonych.

## Collaboration rules
- Work in Polish with precise, direct reports; no guessing or overstated claims.
- When the user says “OK, ROB”, inspect current state, choose the highest-value safe task, implement, test, verify, document, and continue while sensible work remains.
- Do not ask “what next?” if a safe, useful next task is clear.
- Do not make major balance/mechanics decisions without approval. Record unresolved questions as OPEN and gather evidence before recommending.
- Do not modify Fly With Me or Music Manager while working on Crypt Crawler.


## Movement terrain regression coverage — 2026-10-20
- Added a browser regression test that drives the real `update()` loop using controlled player state on ordinary floor, sand, and ice.
- The test protects the current terrain movement multipliers (sand ×0.62, ice ×1.25) and checks that moving off the patch returns to normal speed. It changes no production physics, artwork, animation, or weapon values.
- CI: PR #14 passed `verify.py` and Chromium browser smoke on head `9b04a069a3ea0b1c6e1c78a04253882f41000f0a`. Manual keyboard playtesting remains necessary to judge game feel.


## Gameplay UX i balans — iteracja 2026-10-20
- Dodano widoczny wewnątrz planszy pasek HP z wartością liczbową i paskiem zdrowia, niezależny od małego HUD-u nad canvasem.
- Etykiety drzwi mają teraz 20 px (wcześniej 10 px) i są umieszczane na tabliczkach po wewnętrznej stronie pokoju, zamiast na samym przejściu.
- Sklep pozostaje osobnym pokojem. Zakup serca odbywa się przez podejście do przedmiotu na podłodze (2 monety, +2 HP); nie wymaga kliknięcia przycisku ani myszy.
- Kanał zdarzeń pokazuje tylko ostatni ważny komunikat, a podnoszenie przedmiotów/monet nie spamuje historią statystyk.
- Style ruchu dostały jawne zalety i wady. Taran faktycznie otrzymuje 25% mniej obrażeń, ale porusza się wolniej. Prędkości pozostałych stylów skorygowano, aby zmniejszyć dublowanie ról.
- Siedem broni startowych zachowano, ale przebudowano ich parametry i dodano do wyboru DPS teoretyczny oraz konkretne plusy/minusy. To wstępny balans wymagający dalszych testów walki.
- Testy przeglądarkowe rozszerzono o zakup bez myszy, widoczność HP i redukcję obrażeń Tarana. Wyniki CI należy oceniać dla najnowszego SHA gałęzi.

- Rozszerzono sklep o dwie fizyczne oferty przedmiotów: pasywny za 4 monety i aktywny za 5 monet, obok serca za 2 monety. Zakup następuje przez kontakt z ofertą, jeśli gracz ma wystarczająco monet.

## Test balansu broni — 2026-10-20
- Scalono PR #16: test Chromium mierzy czas do zadania 5 obrażeń wszystkim siedmiu broniom z odległości 40 px i 180 px, używając rzeczywistej pętli gry, pocisków i kolizji.
- Wyniki zapisano w BALANCE_NOTES.md. Rozrzut: 95 klatek z bliska / 321 z daleka; Salwa: 94 / 526. To potwierdza ich wyraźną zależność od dystansu w kontrolowanym teście.
- Testy Chromium i weryfikacja statyczna przeszły dla PR #16. Nie zmieniano parametrów broni; pomiar nie zastępuje walki z ruchomymi przeciwnikami ani ręcznego playtestu.

- Rozszerzono test o trzy cele w skupisku i w linii. W 180 klatkach Rozrzut i Salwa faktycznie rozdzielają obrażenia na cele w skupisku; Przebijający zadaje 6,8 obrażeń każdemu z trzech celów w linii (20,4 łącznie); Wybuchowy zadaje 12,32 łącznie dzięki obrażeniom obszarowym.
- Pełny test Chromium i weryfikacja statyczna przeszły dla PR #17. Obserwacja do ręcznego playtestu: Precyzyjny zadaje nieco więcej obrażeń niż Klasyczny w równym oknie czasu; statystyki pozostają bez zmian do czasu oceny odczuć i walki z ruchomymi wrogami.

- Analiza ekonomii sklepu: przy 4–6 zabójstwach przed sklepem i bazowym dropie monet 8% szansa na zakup przedmiotu za 4/5 monet może być niska (szczegóły i założenia w BALANCE_NOTES.md). Ceny pozostają otwarte do testu dłuższego runu; bez automatycznej zmiany balansu.

- Scalono PR #18 po poprawce testu: zakupy w sklepie mają teraz test progów cenowych w Chromium. Oferta pasywna odrzuca 3 monety i przyjmuje 4; aktywna odrzuca 4 i przyjmuje 5. Test weryfikuje fizyczny kontakt, saldo, zniknięcie oferty i kategorię zakupionego przedmiotu. CI: run 39485755846 — sukces.


## Test ekonomii sklepu — 2026-10-20
- Dodano deterministyczną symulację Chromium: 10 000 wywołań rzeczywistej funkcji `damageEnemy()` dla każdego z trzech poziomów trudności pokoju.
- Test mierzy częstość dropów monet i serc oraz premię za serię co 5 zabójstw; wyniki są wypisywane w logu CI.
- To test reguł dropu, nie symulacja pełnego runu ani dowód na dostępność zakupów przed sklepem. Ceny 4/5 monet nadal pozostają bez zmian.


## Czytelność UI, mapa i zachowanie przeciwników — 2026-10-21
- Dodano stałe przyciski **BROŃ: ... · ZMIEŃ** i **RUCH: ... · ZMIEŃ** poza planszą. W trakcie runu wybór broni wraca bezpośrednio do gry i nie wymusza ponownego wyboru ruchu; skrót **B** otwiera wybór broni, **M** pozostaje wyborem ruchu.
- Ekrany wyboru mają responsywny układ trzech kolumn na szerokim ekranie, przewijanie w obrębie overlayu i mniejsze odstępy, żeby karty nie wychodziły poza planszę.
- Interfejs i arena dostały spokojniejszą, stonowaną paletę ziemi/kamienia, prostsze obramowania i bardziej klasyczny, oldschoolowy charakter RPG. To tymczasowy placeholder graficzny, nie finalne assety.
- Opis przedmiotu/sklepu używa większej czcionki 13–14 px i dynamicznego łamania tekstu.
- Dodano niewielką mapkę pokoju w prawym górnym rogu: gracz, przeciwnicy i drzwi są oznaczeni osobnymi punktami.
- Ruch wrogów rozdzielono na sześć ról: bezpośredni pościg (chaser), krążenie (spitter), ciężki ruch z fazami przyspieszenia (brute), szarża (dasher), boczne manewry (hexer) i boss z krótkimi szarżami.
- Testy Chromium sprawdzają przyciski wyboru w trakcie runu, obecność mapki, czytelność tekstu i odmienne role ruchu. Ręczny test rozgrywki nadal potrzebny do oceny odczuć i balansu.


## Nagroda bossa, balans i czytelność — 2026-10-21
- Gwarantowany losowy item po bossie (pula ruch/strzelanie/statystyki), bez monet i serc; jeden specjalny złoty exit prowadzi na kolejne piętro po wejściu w drzwi.
- Poprawiono komunikat o kolejnym piętrze i celu bossa, wzmocniono różnice między stylami ruchu i strzelania.
- Stalowe Obcasy zostawiają krótkotrwałe pola raniące wrogów; etykiety sklepu mają większy font.
- Dodano testy kontraktów nagrody bossa, wyjścia piętra i przedmiotu zostawiającego szkodliwy ślad. Ręczny playtest odczuć ruchu i broni nadal wymagany.


## Aktualizacja 2026-10-21 — siatka lochu i teren
- Każde piętro ma połączoną siatkę 6×5 (30 pól). Drzwi prowadzą do konkretnego sąsiada zamiast losowo tworzyć kolejny pokój; przejście wstecz wraca do poprzedniego pola.
- M pokazuje pełną mapę piętra; legenda rozróżnia bieżący pokój, odwiedzone i oczyszczone pola.
- Oczyszczone pokoje nie odradzają automatycznie przeciwników po powrocie.
- Dodano kamienie blokujące ruch, dziury spowalniające i zadające okresowe obrażenia oraz wentylatory z okresowym podmuchem.
- Instrukcja pod grą opisuje sterowanie, mapę, teren, ekonomię, przedmioty i bossów.
- M jest mapą; styl ruchu nadal wybiera się przyciskiem RUCH.


## Aktualizacja 2026-10-21 — progresja zejścia
- Skorygowano szansę na zejście: zależy od liczby unikalnych oczyszczonych pokojów na piętrze, nie od ID pokoju w siatce 6×5.
- Test regresyjny potwierdza, że wysokie ID nie podbija szansy, a 20 unikalnych oczyszczonych pokojów gwarantuje wynik losowania.


## Aktualizacja 2026-10-21 — trwałość wyjścia
- Zapamiętywana jest lokalizacja wyjścia na kolejne piętro (ID pokoju i strona drzwi); po powrocie do pokoju wyjście nie przeskakuje losowo.
- Licznik oczekującego zejścia czeka na nowy pokój, zamiast zużywać się przy backtrackingu.


## Aktualizacja 2026-10-21 — wyjście bossa
- Naprawiono zapis konkretnej lokalizacji złotych drzwi po pokonaniu bossa; powrót do pokoju zachowuje to samo wyjście.
- Dodano test regresyjny rzeczywistej funkcji obrażeń i osobny niezmiennik źródła.


## Aktualizacja 2026-10-21 — stan pokojów
- Dodano migawki pokojów przy przejściu: zachowują układ drzwi, dropy, środowisko, zagrożenia oraz stan przeciwników i ich pocisków.
- Powrót do pokoju odtwarza stan zamiast generować nowy układ; sklep nie nadpisuje migawki pokoju gospodarza.


## Aktualizacja 2026-10-21 — trudność według głębokości
- Skalowanie liczby wrogów opiera się na głębokości pola na mapie, a nie na identyfikatorze wierszowym pokoju.
- Dodano test regresyjny pasm głębokości dla startu, dalekich pól i pokoju 30.


## Aktualizacja 2026-10-21 — poziom trudności pokoju
- Migawka stanu zachowuje `roomTier`, aby powrót do pokoju nie resetował poziomu trudności do średniego.


## Aktualizacja 2026-10-21 — sklep bez ponownego losowania ofert
- Po wyjściu ze sklepu fioletowe drzwi w pokoju macierzystym przestają być wejściem do sklepu. Nie da się wracać i losować nowego zestawu ofert w nieskończoność.
- Dodano test Chromium sprawdzający odtworzenie pokoju po wykorzystaniu sklepu.


## Aktualizacja 2026-10-21 — proceduralna mapa i skrót ruchu
- M otwiera wyłącznie mapę piętra; V otwiera wybór ruchu; B otwiera wybór broni. Instrukcje startowe i stałe sterowanie zostały ujednolicone.
- Generowanie piętra zmieniono z pełnej kratownicy na połączony losowy labirynt 6×5: najpierw powstaje drzewo łączące wszystkie 30 pokojów, potem losowo dodawane są nieliczne pętle. Drzwi i mapa korzystają z tej samej listy połączeń.
- Mapa pokazuje faktyczne korytarze, większe pola, bieżący pokój i oznaczone zejście. Pokój 30 ma tylko prawdziwe wyjścia brzegowe; brakujące połączenia wewnętrzne nie tworzą fałszywych drzwi.
- Style ruchu i strzelania mają teraz znacznie mocniejsze różnice. Parametry są prototypowe i podlegają dalszemu balansowaniu po testach.


## Iteracja grafiki i odczuć — 2026-10-21
- W toku: własne sylwetki potworów fantasy w Canvas, bardziej czytelna mapa odkrywania, mocniejsze trade-offy stylów ruchu i łatwiejsze trafianie bronią.
- Sterowanie zmiany ruchu przeniesione z `V` na `Q`; `M` pozostaje mapą.
- Testy przeglądarkowe obejmują archetypy skórek i nowy mnożnik obrażeń Biegacza. Ręczny playtest nie jest deklarowany.
