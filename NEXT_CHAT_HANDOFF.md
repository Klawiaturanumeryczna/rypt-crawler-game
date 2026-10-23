## Kontynuacja: monety i „niewidzialne” zgony — 2026-10-23

- Monety są teraz księgowane przez `changeCoins(delta)`; `coinsEarned` i `coinsSpent` są resetowane przy nowym runie i zapisywane w podsumowaniu śmierci. Oczekiwany niezmiennik: saldo końcowe = zebrano − wydano.
- Przyczyna trafienia rozszerza się o pozycję/klatkę i dane kolizji (wróg, pocisk albo ogień), by zgłoszenie śmierci dało się odtworzyć.
- Test dodany do Chromium smoke: 5 monet wpływu, 2 wydane, saldo 3 oraz etykieta `MONETY (RUN)`.
- Zmiany są na gałęzi `fix/economy-hit-diagnostics-2026-10-23`; przed merge sprawdź Chromium smoke oraz statyczne `verify.py`. Nie deklaruj ręcznego playtestu.

---

## Najnowsza iteracja rozgrywki — 2026-10-23

- Nowa broń startowa **Śrutownik** zastępuje Precyzyjnego: 1 pocisk na strzał, odstęp 6 klatek, losowe odchylenie ±0,13 rad. Dostępne bronie: Śrutownik, Klasyk, Salwa.
- Pokój ma 900×540 px (wcześniej 816×484; ok. +23% powierzchni). Generacja Hotline próbuje 3 formacje osłon; kamienie mają promień 18.
- Ekran śmierci pokazuje przyczynę ostatniego trafienia. Sprawdzaj ją przy zgłoszeniach „niewidzialnych” śmierci; w Hotline pułapki podłogowe nie zadają obrażeń.
- HUD waluty wyświetla „MONETY (RUN)”; waluta jest resetowana przy rozpoczęciu nowej próby, nie jest walutą trwałą.
- Zmiany scalono: source PR #74 (`6797c294`), mirror PR #5 (`7371790f`). Source Chromium runy `39972336976` / `39972499418` oraz mirror run `39972909369` przeszły. Wszystkie 9 współdzielonych plików mają zgodne blob SHA. Nie potwierdzono niezależnie najnowszego deploymentu Pages; ręczny playtest pozostaje otwarty.

---

## Audyt dokumentacji balansu — 2026-10-23

- Dodano nadrzędne bloki aktualnego stanu do `BALANCE_NOTES.md` i `DECISION_LOG.md`, aby stare notatki o 30 pokojach, losowych wyjściach i wcześniejszych wyborach nie były odczytywane jako aktualne wymagania.
- Przy każdej zmianie balansu potwierdzaj liczby w `index.html` i testach; sekcje historyczne mogą zawierać dawne wartości.
- Nie wykonano ręcznego playtestu. Nie uznawaj sterowania, balansu ani nawigacji za zaakceptowane.

---

# Crypt Crawler — handoff dla kolejnego czatu
**Aktualizacja:** 2026-10-23  
**Ten plik jest punktem startowym dla nowej sesji.** Najpierw przeczytaj go, następnie `PROJECT_STATUS.md`, `DECISION_LOG.md`, `BALANCE_NOTES.md` oraz `verify.py` i `tests/browser_smoke.py`. Nie opieraj się wyłącznie na podsumowaniu rozmowy — sprawdź bieżący stan repozytorium.

## Najnowszy zgłoszony problem / aktualna praca
- Użytkownik zgłosił, że monety są nieczytelne/niedziałające, amulet za 2 monety jest niezrozumiały, przedmiot sklepu znika bez jasnej intencji zakupu, a osłony są przypadkowo rozrzucone.
- PR #60 scalony do `main` (merge `97d0b289f92f8651f4da0a8423a3832e63135b96`; browser smoke `39830353160` success): oferty sklepu wymagają pojedynczego `E` (nie kupują się przy samym kontakcie); prompt sklepu komunikuje koszt i efekt; tryb Hotline generuje formacje kamieni `U/X/L/I/T` zapewniające sensowne zasłony. Dodano browser-smoke assertions. Następny krok: zsynchronizuj 8 wspólnych plików do mirrora, porównaj blob SHA i sprawdź najnowszy workflow Pages.
- W grze moneta to waluta runu; amulet ratunkowy blokuje jeden śmiertelny cios i zostawia 1 HP, po czym znika. W sklepie koszt 2 monet dotyczy jednorazowego amuletu — nie leczenia HP.

## Linki i architektura repo
- Gra grywalna (GitHub Pages): https://klawiaturanumeryczna.github.io/rypt-crawler-game/
- SSOT — prywatne/główne repo: https://github.com/Klawiaturanumeryczna/crypt-crawler
- Publiczny mirror i deployment: https://github.com/Klawiaturanumeryczna/rypt-crawler-game
- Zasada: `crypt-crawler` jest źródłem prawdy. Po zatwierdzeniu zmian aktualizuj mirror i sprawdź zgodność blob SHA plików współdzielonych oraz status GitHub Pages.

## Tryb współpracy użytkownika
- **„OK, rob”** = działaj autonomicznie: sprawdź stan repo i kolejkę problemów, wybierz największą sensowną poprawkę, zaimplementuj, dodaj/uruchom testy, zweryfikuj, zaktualizuj dokumentację, otwórz PR. Nie pytaj „co dalej?”, jeśli są oczywiste zadania.
- **„START”** = długi autonomiczny maraton, kontynuuj po kolejnych zadaniach aż do blokady albo decyzji wymagającej użytkownika.
- Pracuj większymi, logicznymi partiami. Nie udawaj ręcznego playtestu, jeśli go nie wykonano. Rozróżniaj testy statyczne, Chromium i prawdziwe granie.
- Nie zgaduj nazw narzędzi, funkcji ani stanu CI. Pobieraj aktualne pliki i workflowy przez GitHub connector. Po zmianie testu, która nie przechodzi, napraw test/kod i uruchom ponownie; nie scalaj przy czerwonym CI.
- Dokumentacja projektu ma być po polsku; nazwy kodowe/keywords mogą pozostać po angielsku. Zapisuj trwałe decyzje w `DECISION_LOG.md`, aktualny stan w `PROJECT_STATUS.md`, balans w `BALANCE_NOTES.md`. Przy nowych ważnych decyzjach aktualizuj ten handoff lub dodaj kolejny plik, a prompt dla następnej sesji ma wskazywać wszystkie nowe pliki.
- Fundamentalnych zmian celu gry, zasad zwycięstwa/porażki, struktury pięter, bossów, progresji i checkpointów nie wdrażaj bez uzgodnienia. Bugfixy, UX, sterowanie, wydajność, testy i dokumentację rób autonomicznie.
- Użytkownik chce konkretów i rzetelności. Nie deklaruj, że poprawka jest opublikowana, dopóki nie sprawdzisz merge, synchronizacji mirrora i deploymentu.

## Obecna gra i ważne decyzje
- Gra to przeglądarkowy top-down dungeon crawler, obecnie w jednym głównym `index.html`, z testami w `tests/browser_smoke.py` i kontrolami źródła w `verify.py`.
- **Aktualny kod ma 10 pokojów na siatce 5×2**, a pokój 10 jest bossem. Wszystkie dziewięć pozostałych pokojów trzeba oczyścić przed wejściem do bossa. Starsze zapisy o 30 pokojach/siatce 6×5 dotyczą wcześniejszej wersji i są nieaktualne dla bieżącego `index.html`.
- Pokój ma stan zachowywany przy powrocie: drzwi, dropy, teren, wrogów i pociski. Oczyszczone pokoje nie powinny resetować się losowo.
- Mapa piętra jest pod `M`. Zmiana stylu ruchu jest pod `V`, wybór broni pod `B`; ruch `WASD`, strzałki strzelają kierunkowo, LPM strzela do kursora. Sprawdź rzeczywisty kod i instrukcje przed zmianą mapowania; nie przywracaj `Shift` jako uniku.
- Wyjście na następne piętro zależy od liczby unikalnych oczyszczonych pokojów, a nie numeru ID. Wylosowane wyjście ma stałą lokalizację podczas backtrackingu; wyjście bossa i graniczne wyjścia pokoju 30 również mają być trwałe.
- Sklep jest jednorazowy na piętro; powrót nie może odświeżać ofert.
- Dodano przeszkody terenowe (kamienie, doły, okresowe podmuchy), kilka autorskich motywów pięter i autorskie sylwetki fantasy rysowane w Canvas. Grafika jest nadal prototypowa.
- Testy automatyczne nie zastępują ręcznego testu płynności i przyjemności rozgrywki.

## Najważniejszy aktywny zakres pracy — stan na 2026-10-22

Bieżącym celem jest prototyp walki inspirowany Hotline Miami. Nie traktuj dawnych notatek o 30 pokojach, skrótach M/Shift ani wcześniejszych parametrach ruchu jako aktualnych; kod `index.html` i testy są źródłem prawdy.

1. **Pętla piętra:** 10 pokojów w siatce 5×2, boss w pokoju 10, wymagane oczyszczenie pokojów 1–9. Nie zmieniaj tego flow bez zgody.
2. **Śmiertelność:** gracz ginie od jednego rzeczywistego trafienia, z wyjątkiem istniejącego jednorazowego ratunku i wyraźnych okien uniku. Zwykły wróg ginie od jednego trafienia; boss jest wielotrafieniowy.
3. **Osłony i AI:** kamienie blokują ruch, pociski i widoczność. AI ma obchodzić osłony; istnieją deterministyczne testy pojedynczego kamienia oraz dwóch kolejnych kamieni, ale nie obejmują wszystkich geometrii.
4. **Czytelność strzałów:** zwykły strzelec ma 18 klatek windup, boss 24; kierunek zostaje zablokowany na początku ostrzeżenia. Ręcznie oceń, czy gracz widzi telegraph i może zareagować.
5. **Sterowanie:** WASD = ruch, strzałki = strzelanie kierunkowe, mysz + LPM = strzał do kursora, M = mapa, V = wybór ruchu, B = wybór strzelania, Spacja = aktywny przedmiot, P = pauza, R = restart.
6. **Następny priorytet techniczny:** naprawiaj wykazane błędy w generatorze, mapie, kolizjach, strzelaniu lub czytelności. Przed dużą zmianą mechaniki dodaj test regresyjny i najpierw ustal rzeczywisty stan kodu. Nie przepisuj AI na A* bez reprodukowalnego przypadku, w którym aktualna heurystyka zawodzi.
7. **Oprawa wizualna:** pozostaje długoterminowym celem — własne, czytelne sylwetki potworów, itemy i podłoże — ale nie może maskować błędów w walce i nawigacji.
8. **Publikacja:** po każdej zmianie sprawdź CI na dokładnym SHA, scalaj wyłącznie przy zielonym CI, synchronizuj mirror, porównuj treści plików i sprawdzaj deployment Pages. Ręcznego playtestu nie deklaruj, jeśli go nie wykonano.

## Następny ruch dla nowego czatu

Najpierw pobierz aktualny HEAD main, stan PR/CI i status Pages; porównaj `index.html`, README, handoff, status, checklistę i testy. Dokumentacja historyczna zawiera wcześniejsze warianty (w tym 30 pokojów i starsze skróty), więc aktualizuj ją przy rozbieżnościach. Następnie kontynuuj od największego konkretnego problemu możliwego do odtworzenia. Nie pytaj użytkownika „co dalej?”, jeśli można bezpiecznie wykonać kolejny test lub bugfix.

## Dopisane po audycie 2026-10-21 — sterowanie i strzelanie
- Aktualny skrót zmiany ruchu: **V** (M = mapa, B = broń). Starsze notatki z Q są historyczne i nie mogą nadpisywać aktualnego kodu.
- Drifter i Rozpęd dostały mocniejsze hamowanie po pomiarze Chromium: Drifter zachowuje 70% prędkości na klatkę po puszczeniu kierunku, Rozpęd 65%. Prógi drogi po puszczeniu pozostają regresyjną blokadą. Drifter ma krótszy, kontrolowany poślizg (0,70); Rozpęd nadal przyspiesza i skręca ciężej, ale lepiej hamuje (0,65).
- Rozrzut to szeroki strzał z bardzo bliska; Salwa to wąska, skupiona seria na średni dystans. Asercje TTK i obrażeń grupowych należy przejrzeć po zmianie kształtu wachlarza.
- Najnowsze zmiany wymagają uruchomienia `python verify.py` i `python tests/browser_smoke.py` oraz sprawdzenia CI przed scaleniem. Nie wykonano ręcznego playtestu.

## Dopisek 2026-10-21 — różne mechaniki Skoczka i Zwinnego
- W poprzedniej wersji oba style wykonywały automatyczne przyspieszenie z krótką nietykalnością; różniły się głównie cyklem 22/26 klatek. To było zbyt podobne.
- Skoczek: rytmiczny automatyczny sus co 22 klatki, 8 klatek przyspieszenia/ochrony, wolny między susami.
- Zwinny: prędkość bazowa 3,3; zryw 2,2× na 4 klatki po ostrym skręcie, 24 klatki odnowienia i +10% otrzymywanych obrażeń. Zryw wymaga świadomego zmieniania kierunku, nie odpala się sam w stałym ruchu.
- Usunięto okrągłe obrysy zrywu, które były mylące. Brak nowego klawisza uniku; M mapa, V ruch, B broń.
- Wnioski z researchu: gracze ETG polecają najpierw precyzyjnie omijać pociski, a roll zostawiać na sytuacje wymagające szybkiego repositioningu; w Isaac bezwładność jest polaryzująca. Zachowuj wybór między ruchem natychmiastowym i bezwładnym, ale nie zmuszaj wszystkich archetypów do podobnego auto-zrywu.
- PR wymaga zielonego verify.py i Chromium; nie wykonano ręcznego playtestu.


## MAX MARATON — audyt topologii mapy (2026-10-21)
- W gałęzi `test/dungeon-grid-seed-sweep` dodano test `window.__testDungeonGridBatch()`: 128 deterministycznych seedów generatora.
- Kontrole obejmują wymiary/ID 30 pokojów, współrzędne 6×5, prawidłowe kierunki, brak wyjść poza granice, korytarze wzajemne, spójność grafu, 29–48 krawędzi i różnorodność co najmniej 100 grafów.
- Test nie zmienia mechaniki gry; przed scaleniem wymagane zielone CI (verify.py + Chromium). Po scaleniu trzeba zsynchronizować mirror i potwierdzić Pages.
- Następny większy kierunek po teście: audyt czytelności mapy i zgodności widocznych korytarzy z odkryciem pokoi. Nie zmieniać zasad piętra ani limitu 30 pokojów bez zgody użytkownika.


## MAX MARATON — markery mapy piętra (2026-10-21)
- W gałęzi `ux/map-room-markers-v2` dodano czytelne znaczniki `B` dla bossa (piętro 2+) oraz `S` dla dostępnego sklepu. Marker sklepu opiera się na rzeczywistym stanie drzwi i znika po użyciu sklepu.
- Legenda mapy została rozdzielona na dwie linie. Test Chromium sprawdza marker aktualnego i zapisanego sklepu, bossa, zejścia i sklepu już wykorzystanego.
- To zmiana wyłącznie informacyjna/UI; nie zmienia układu piętra, walki ani ekonomii. Wymagane zielone CI przed scaleniem.


## MAX MARATON — powtarzany skrót ruchu (2026-10-21)
- W gałęzi `fix/repeated-movement-hotkey` dodano V do strażnika powtarzanych zdarzeń klawiatury. Przytrzymanie V nie powinno wielokrotnie otwierać wyboru stylu ruchu.
- Dodano asercję Chromium i kontrolę `verify.py`. Wymagane zielone CI, potem synchronizacja mirrora i Pages.


## MAX MARATON — czytelniejszy drop monet (2026-10-21)
- Gałąź `ui/coin-drop-visual` dodaje `drawCoinDrop`: okrągły złoty żeton z obwódką, wewnętrznym pierścieniem i centralnym znakiem.
- Test Chromium sprawdza dwa łuki, wypełnienie, trzy obrysy i centralny znak. Zmiana jest wizualna; nie rusza ekonomii.
- Przed scaleniem wymagane zielone CI, po scaleniu synchronizacja mirrora i deployment.


## MAX MARATON — checklista ręcznego playtestu (2026-10-21)
- Dodano `MANUAL_PLAYTEST_CHECKLIST.md` — scenariusze do sprawdzenia ruchu, strzelania, skrótów, mapy, sklepu, dropów i przeszkód oraz format raportowania obserwacji.
- To instrukcja na przyszłość, nie dowód wykonania ręcznego playtestu. Po zebraniu obserwacji użyj ich do kolejnej iteracji; nie zgaduj balansu bez danych.


## MAX MARATON — poprawki przed nowym pomysłem (2026-10-22)
- Gałąź `gameplay/ten-room-boss-floor-and-movement-fixes` zmniejsza piętro z 30 do 10 pokojów, siatka ma 5×2 węzły, a pokój 10 jest bossem na każdym piętrze.
- Losowe wcześniejsze zejścia są wyłączone. Pokój 10 nie ma aktywnego zejścia przed pokonaniem bossa; pokonanie bossa ustawia trwałe drzwi przejścia.
- Zwinny: wyraźny zryw po ostrym skręcie 3×/5 klatek, 5 klatek ochrony, cooldown 18 klatek, +15% obrażeń otrzymywanych. Biegacz bez zrywu.
- Skoczek: usunięto kreski zawsze rysowane z lewej strony postaci podczas susa.
- Zaktualizowano testy generatora, mapy, głębokości pokojów i zejścia. Po zielonym CI należy scalić, zsynchronizować mirror i Pages, a następnie utworzyć branch backupowy (np. `backup/pre-new-idea-2026-10-22`) wskazujący dokładnie zatwierdzony commit.
- Ważne: to celowo tymczasowa wersja do eksperymentu. Nie wdrażać późniejszego dużego pomysłu bez zachowania tego punktu powrotu.


## MAX MARATON — eksperyment Hotline Miami (2026-10-22)
### Punkt powrotu (nie ruszać)
- Gałąź: `backup/pre-hotline-miami-2026-10-22`
- Commit: `b26b5d913fb06d0f124d92a9a17d24ae031df91c`
- To jest zatwierdzona wersja przed eksperymentem: 10 pokojów, pokoje 1–9 do oczyszczenia, boss w pokoju 10, zejście dopiero po bossie; Zwinny ma wyraźny zryw, Skoczek nie ma lewych smug.
- Repo główne: https://github.com/Klawiaturanumeryczna/crypt-crawler
- Mirror: https://github.com/Klawiaturanumeryczna/rypt-crawler-game
- Public Pages: https://klawiaturanumeryczna.github.io/rypt-crawler-game/

### Stan po merge
- PR #52 scalony do main; commit: `21b828777bd42ecd344cd15b9700445651162ff3`.
- Zielone CI dla dokładnego HEAD: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39805719924 oraz https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39805761699.
- Mirror/Pages nie są jeszcze zsynchronizowane z wersją Hotline; to następny krok.
- Research/spec: `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md` — zawiera źródła i ograniczenia; społecznościowe posty są jakościowymi anegdotami, nie reprezentatywną ankietą.
- Wprowadzono tryb śmiertelny: jedno życie gracza; zwykły wróg ginie od dowolnego trafienia; boss jest wyjątkiem; kamienie blokują pociski i LOS; strzały przyciągają wrogów w pobliżu; wrogowie dystansowi strzelają tylko przy widoczności.
- Zaktualizowano testy ruchu, aby nie wpadały na losowo wygenerowaną osłonę. Nowe testy sprawdzają one-hit, LOS/osłonę i hałas.
- Następny krok: zsynchronizuj main do mirrora, sprawdź CI mirrora i Pages deployment. Potem wykonaj ręczny playtest: czy wrogowie obchodzą kamienie, czy pociski zatrzymują się na osłonie, czy hałas przyciąga ich zrozumiale, czy R jest natychmiastowy i czy śmierć jest sprawiedliwa.
- Jeśli prototyp jest gorszy, wróć do backupu przez PR z gałęzi `backup/pre-hotline-miami-2026-10-22`; nie przepisuj go ręcznie i nie nadpisuj backupu.
- Nie deklaruj, że wykonano ręczny playtest — dotąd go nie wykonano.

- W aktualnej wersji działa szybki restart R z zachowaniem broni/ruchu oraz ekonomia jednego życia: pierwszy pickup serca daje amulet ratunkowy, kolejne monety, sklep sprzedaje ratunek zamiast +HP. Ręczny playtest nadal nie został wykonany.
- Gotowy prompt dla kolejnego czatu znajduje się w `NEXT_CHAT_PROMPT.md`; nie wystarczy sam prompt — nowy czat ma najpierw przeczytać handoff/status/research w repo.


## Stan przekazania — sprawdzone ponownie 2026-10-22 17:50
- Aktualny HEAD w chwili aktualizacji: `a7058f1cce32185d9f99e3a511c7e65770b1c8ea` (commit dokumentacyjny po merge Hotline). Sprawdź ponownie przed dalszą pracą, bo HEAD może się zmienić.
- PR #52 scalony. Kodowy commit `21b828777bd42ecd344cd15b9700445651162ff3` ma zielony CI: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39805994523.
- Najnowszy run dla dokumentacyjnego HEAD jest anulowany: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39806564672. Nie traktuj tego jako testu kodu, ale zweryfikuj aktualny CI i nie twierdź, że dokładny HEAD jest zielony, dopóki nie sprawdzisz.
- Backup nadal istnieje: `backup/pre-hotline-miami-2026-10-22` → `b26b5d913fb06d0f124d92a9a17d24ae031df91c`. To punkt powrotu do wersji 10-pokojowej przed HLM. Nie zmieniaj jego refa.
- Mirror/Pages w poprzednim odczycie nie były zsynchronizowane z Hotline. Zweryfikuj teraz na żywo; synchronizuj pliki z main, porównaj SHA, sprawdź CI mirrora i deployment Pages.
- PR #45 (wcześniejsza próba implementacji 10 pokojów) został zamknięty bez merge. Nie bazuj na jego gałęzi. Kod HLM w main to obecny eksperyment; 10-pokojowa wersja jest zachowana w backupie.
- Brak ręcznego playtestu. Po synchronizacji mirror/Pages wykonaj testy z `MANUAL_PLAYTEST_CHECKLIST.md` i zapisz tylko obserwacje faktycznie sprawdzone.
- Gotowy prompt do wklejenia w nowym czacie: `NEXT_CHAT_PROMPT.md`. Prompt instruuje nowy czat, by przeczytał dokumenty, sprawdził aktualny stan repo/CI i kontynuował `OK, rob` bez pytania „co dalej?”.


## MAX MARATON — Hotline research and live-state verification (2026-10-22 17:48 UTC+2)
- Main HEAD zweryfikowany: `6ae4fb9630dfb90f43c260eaeb6743a8f703676b`. Dokładny HEAD ma zielone CI: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39808650676 — zarówno `Verify source invariants`, jak i `Test game in Chromium` zakończone sukcesem.
- PR #52 (prototyp walki Hotline) i PR #53 (handoff/checklista) są scalone.
- Backup sprawdzony na żywo: `backup/pre-hotline-miami-2026-10-22` → `b26b5d913fb06d0f124d92a9a17d24ae031df91c`. Nie przesuwać ani nie nadpisywać.
- SHA wszystkich kluczowych plików — kod, testy, research, prompt, handoff, status, decyzje, balans i checklista — są identyczne między main i publicznym mirrorem. Mirror workflow zakończony sukcesem: https://github.com/Klawiaturanumeryczna/rypt-crawler-game/actions/runs/39806755919.
- Research został rozszerzony o dodatkowe recenzje i jakościowe dyskusje społecznościowe; plik `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md` jest dokumentem źródłowym dla wniosków.
- Najważniejszy otwarty punkt: brak ręcznego playtestu. CI nie potwierdza, że AI umie obchodzić kamienie ani że śmierci są odczuwane jako sprawiedliwe. Użyj `MANUAL_PLAYTEST_CHECKLIST.md` i nie wymyślaj wyników.
- Gotowy prompt dla nowego czatu: `NEXT_CHAT_PROMPT.md`. Przed dalszą pracą nowy czat ma przeczytać pliki, sprawdzić live HEAD/CI/mirror i kontynuować `OK, rob`.

## Audyt nowej sesji — 2026-10-22 18:10 UTC+2
- Live main HEAD: `a497bc64f85bc1eb593a069eb0cdc08b52ebca75` (merge PR #54 z research/handoff). Otwarte PR-y w głównym repo: brak.
- Live backup potwierdzony: `backup/pre-hotline-miami-2026-10-22` → `b26b5d913fb06d0f124d92a9a17d24ae031df91c`; nie ruszać.
- Dokładny HEAD `a497bc64...` miał run `39809523092` anulowany podczas kroku Chromium (krok statycznej weryfikacji przeszedł). Poprzedni kodowy commit `6ae4fb9630dfb90f43c260eaeb6743a8f703676b` ma zielone Chromium CI w runie `39808650676`. Ponowiono anulowany job dla bieżącego HEAD przez GitHub Actions; sprawdź rezultat przed jakimkolwiek merge.
- Mirror main HEAD to `da343edaeedd6bb6c35ea8265ac6c8190bf580e0`. Pliki współdzielone sprawdzone blob SHA i tekstowo: `NEXT_CHAT_HANDOFF.md`, `PROJECT_STATUS.md`, `DECISION_LOG.md`, `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md`, `BALANCE_NOTES.md`, `MANUAL_PLAYTEST_CHECKLIST.md`, `verify.py`, `tests/browser_smoke.py` — każdy ma identyczny SHA po obu stronach. Mirror Browser smoke oraz Pages build/deployment mają zielone runy na mirror HEAD `da343eda...` (`39809737282`, `39809736901`).
- Uwaga: tytuł gry w checkliście ma historyczny URL `https://klawiaturanumeryczna.github.io/rypt-crawler/`, natomiast właściwy Pages URL wskazany w repo to `https://klawiaturanumeryczna.github.io/rypt-crawler-game/`. Sprawdź/ujednolić w osobnej poprawce dokumentacyjnej.
- Ręczny playtest nadal niewykonany. CI potwierdza tylko kontrole statyczne/Chromium; zachowanie AI przy osłonach, czytelność zagrożeń i sprawiedliwość zgonów pozostają niezweryfikowane.
- Następny ruch: sprawdź wynik ponowionego joba dla `a497bc64...`; potem wykonaj kolejny pakiet autonomiczny z priorytetem na poprawność/checklistę, ale żadnej oceny grywalności bez człowieka. Nie zmieniaj reguł projektu ani backupu.

## Audyt publikacji — synchronizacja dokumentacji, 2026-10-22 18:12 UTC+2
- Po ostatniej aktualizacji dokumentów synchronizowano do mirrora `PROJECT_STATUS.md`, `DECISION_LOG.md`, `MANUAL_PLAYTEST_CHECKLIST.md` i `NEXT_CHAT_HANDOFF.md`; ich blob SHA jest identyczne z głównym repo.
- Aktualny main HEAD zmienia się na skutek oddzielnych commitów dokumentacji. Sprawdź ponownie CI i mirror po zakończeniu bieżących workflow; nie opieraj się na wcześniejszym SHA sprzed aktualizacji.
- Wcześniejszy błąd URL w checklistcie został poprawiony: prawidłowy publiczny Pages URL to https://klawiaturanumeryczna.github.io/rypt-crawler-game/.
- Nie wykonano ręcznego playtestu. Kolejny czat ma nadal wymagać rzeczywistej sesji przed uznaniem AI/pathfindingu/fairness za zatwierdzone.

## MAX MARATON — pakiet mapy i czytelności walki (2026-10-22)
- Gałąź robocza: `marathon/map-ai-readability-2026-10-22` (na bazie live main `c84b6f977386d8d1c0c4ca313ecd87a6079ebcae`).
- Runda 1: wyśrodkowano pełną mapę piętra i poprawiono podpis minimapy, aby M nie sugerowało błędnie mapy aktualnego pokoju.
- Runda 2: dodano heurystyczne omijanie kamieni dla wrogów, gdy bezpośrednia trasa do celu jest zablokowana. To nie jest pełny pathfinding i wymaga ręcznej oceny przy wielu osłonach.
- Runda 3: strzelcy dystansowi/boss pokazują linię celowania i odczekują 10/16 klatek przed strzałem; windup anuluje się, gdy cel traci czystą linię widzenia.
- Dodano regresje Chromium dla ruchu wokół kamienia i opóźnionego strzału oraz kontrole źródła. Przed merge sprawdź CI dla najnowszego SHA gałęzi i popraw wszelkie czerwone wyniki. Nie scalaj przy czerwonym/pending.
- Zmienione pliki: `index.html`, `tests/browser_smoke.py`, `verify.py`, `PROJECT_STATUS.md`, `DECISION_LOG.md`, `BALANCE_NOTES.md`, `MANUAL_PLAYTEST_CHECKLIST.md`, ten handoff.
- Po zielonym CI: review diffu, otwórz PR; nie scalaj samodzielnie, dopóki wszystkie workflowy nie będą zielone. Po merge synchronizuj dokładnie zmienione pliki do mirrora, sprawdź zgodność SHA, Browser smoke i Pages deployment.
- Użytkownik ma później wykonać playtest. Do tego czasu pathfinding i fairness ataków są niepotwierdzone; nie twierdzić, że ręcznie sprawdzono grę.


## MAX MARATON — windup z możliwością uniku (2026-10-22)
- Gałąź robocza: `fix/telegraph-locked-aim-2026-10-22`, utworzona z main `51572207218eac2b49645fa4b1a38008c58e2bb8`.
- Eksperyment: zwykły strzelec 18 klatek, boss 24 klatki ostrzeżenia; kierunek zapisany przy rozpoczęciu windup, pocisk nie śledzi gracza. Ostrzeżenie anuluje się, gdy zapisany tor zostaje zasłonięty kamieniem lub wróg traci czystą linię wzroku.
- Zmieniono `index.html`, `tests/browser_smoke.py` i `verify.py`; test Chromium przesuwa gracza w trakcie windup i sprawdza, że pocisk nadal leci w poprzedni kierunek.
- Zaktualizowano `BALANCE_NOTES.md`, `DECISION_LOG.md`, `MANUAL_PLAYTEST_CHECKLIST.md` i `PROJECT_STATUS.md`. To eksperyment oczekujący na CI/PR; nie twierdzić, że został scalony ani wdrożony.
- Dla uniknięcia powolnego pobierania pakietów APT w CI zmieniono `.github/workflows/browser-smoke.yml` z `playwright install --with-deps chromium` na `playwright install chromium`; na GitHub-hosted runnerze test przechodzi bez ponownego instalowania systemowych zależności. Główny CI run `39824282975` dla main zakończył się sukcesem.
- Mirror zsynchronizowano w commicie `783814e3caa553dea01e121628cf86644ca53a86`; wszystkie 9 współdzielonych plików ma identyczny blob SHA i treść w SSOT/mirror. Mirror browser smoke `39824422931` jest zielony. Pages build/deploy dla SHA `783814e...` wymaga jeszcze potwierdzenia zakończenia.
- Brak ręcznego playtestu. Nie zmieniać gałęzi backupowej.


## MAX MARATON — test dwóch kolejnych osłon (2026-10-22)
- PR #57 scalono jako `a0c98e496b676429b9e04535a0d0ada6a86f2531`; run Chromium `39824808999` dla SHA `2971632cc3669e88578f1a42cbe3a50d15a6a494` jest zielony.
- Rozszerzono `window.__testEnemyCoverNavigation()` o dwa kamienie na bezpośredniej trasie. Po 180 klatkach wróg osiągnął cel (dystans 1,79 px), odszedł od linii środkowej o 51,56 px i nie nachodził na żadną skałę (odległości 168,40 i 98,40 px przy wymaganych 42 px).
- To potwierdza wyłącznie deterministyczny scenariusz dwóch ustawionych w linii kamieni; nie dowodzi, że AI zawsze znajdzie drogę w ciasnych pokojach lub przy losowych układach.
- Kolejny krok: po synchronizacji mirrora i potwierdzeniu Pages użytkownik ma wykonać ręczny playtest. Nie dodawaj pełnego A* bez dowodu z testu, że obecna heurystyka zawodzi.


## MAX MARATON — użyteczność leczenia w one-hit (2026-10-22)
- Audyt wykrył, że Mała/Wielka Apteczka i Nagolenniki Witalności/Nagolenniki Życia zachowywały leczenie/bonus HP mimo śmiertelności jednego trafienia.
- Gałąź `fix/hotline-health-item-utility-2026-10-22` zmienia te cztery przedmioty w amulet ratunkowy, jeśli nie ma go w ekwipunku, lub monety w przypadku duplikatu. W trybie standardowym ich stare efekty pozostają bez zmian.
- PR #59 scalono jako `05aa3c9e70da03d96d826493392e4ae45f7b109a`; CI main run `39826837619` jest zielony. Po synchronizacji mirror Browser smoke `39826896790` i Pages deployment `39826897083` również przeszły. Test ręczny ekonomii nie został wykonany.

## Zmiana sposobu pracy — 2026-10-22
Po informacji zwrotnej użytkownika obowiązuje protokół z sekcji „4A. Protokół efektywnej pracy” w `NEXT_CHAT_PROMPT.md`. Priorytetem jest namacalny postęp gameplayowy. Ogranicz powtarzane odczyty GitHub/CI, grupuj powiązane zmiany, dobieraj testy do ryzyka i nie traktuj zielonego smoke testu jako dowodu dobrej rozgrywki. Ręczny playtest osłon/AI pozostaje niewykonany i nie wolno go raportować jako zaliczonego. Nie zmieniaj ani nie przesuwaj backupu.

## Current gameplay state after PR #70 — 2026-10-22

- PR #61 (work protocol) and gameplay PRs #63–#70 are merged into `main`.
- PR #63: two varied cover formations attempted per Hotline room; cover radius 14; unsafe fallback removed. Browser smoke run `39837922682` passed.
- PR #64: player weapon selection is Precyzyjny/Klasyk/Salwa only; cooldowns 48/22/150 frames, Classic projectile life 77 frames. Browser smoke run `39838967501` passed.
- PR #65: only Drifter and Skoczek selectable; Drifter inertia adjusted; Skoczek leap is 10 frames at 3× with randomized start interval 20–26 frames. Browser smoke run `39839665500` passed.
- PR #66: enemy pool is Drifter, Skoczek, Taran, Biegacz plus separate boss; Taran base HP is 7. Browser smoke run `39840886624` passed.
- PR #67: safe entry-side spawn and removal of the repelling vent. Browser smoke run `39841816581` passed.
- PR #68: refreshed status/handoff. Browser smoke run `39842542681` passed.
- PR #69: corrected in-game help from the retired 30-room/6×5 layout to the active 10-room/5×2 floor. Source browser smoke run `39843505951` passed.
- PR #70: live Pages smoke script retries while Pages propagates a new deployment. Source CI run `39844176973` passed.
- Mirror PR #1 synced the corrected help and added live smoke; PR #2 fixed the trigger to run on main pushes and on demand. Both mirror PRs passed browser smoke.
- GitHub Pages deployment run `39844418787` succeeded for mirror commit `b46abc1767db7305a914c9cfd11e904ab8b804e3`.
- **Published-page browser smoke passed:** run `39844419662` loaded `https://klawiaturanumeryczna.github.io/rypt-crawler-game/`, confirmed HTTP 200 and the new 10-room help marker, selected Precyzyjny and Drifter, entered gameplay at floor 1 / room 1, and reported no uncaught JavaScript errors.
- The mirror now runs the published-page smoke automatically on pushes to `main`, waiting up to 180 seconds for the deployed build; it can also be run manually with `workflow_dispatch`.
- **Manual gameplay playtest has not been performed.** Automated smoke verifies loading and startup only; it does not establish subjective game feel, fairness, enemy behavior under live play, or balance.
- **Checklist audit (2026-10-22):** player movement choices are only Drifter and Skoczek; player firing choices are Precyzyjny, Klasyk and Salwa. Updated `MANUAL_PLAYTEST_CHECKLIST.md` to avoid treating legacy movement/weapon archetypes as selectable player options.
- Backup `backup/pre-hotline-miami-2026-10-22` remains untouched.
- Next: human playtest using `MANUAL_PLAYTEST_CHECKLIST.md`; use observations to identify concrete fixes, not speculative new mechanics.
