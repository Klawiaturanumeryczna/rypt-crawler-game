# Crypt Crawler — handoff dla kolejnego czatu
**Aktualizacja:** 2026-10-21  
**Ten plik jest punktem startowym dla nowej sesji.** Najpierw przeczytaj go, następnie `PROJECT_STATUS.md`, `DECISION_LOG.md`, `BALANCE_NOTES.md` oraz `verify.py` i `tests/browser_smoke.py`. Nie opieraj się wyłącznie na podsumowaniu rozmowy — sprawdź bieżący stan repozytorium.

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
- Piętro ma 30 pokojów na siatce 6×5. Generowany graf najpierw tworzy połączone drzewo, potem dodaje niewiele pętli. Drzwi i mapa muszą korzystać z dokładnie tego samego grafu.
- Pokój ma stan zachowywany przy powrocie: drzwi, dropy, teren, wrogów i pociski. Oczyszczone pokoje nie powinny resetować się losowo.
- Mapa piętra jest pod `M`. Zmiana stylu ruchu jest pod `V`, wybór broni pod `B`; ruch `WASD`, strzałki strzelają kierunkowo, LPM strzela do kursora. Sprawdź rzeczywisty kod i instrukcje przed zmianą mapowania; nie przywracaj `Shift` jako uniku.
- Wyjście na następne piętro zależy od liczby unikalnych oczyszczonych pokojów, a nie numeru ID. Wylosowane wyjście ma stałą lokalizację podczas backtrackingu; wyjście bossa i graniczne wyjścia pokoju 30 również mają być trwałe.
- Sklep jest jednorazowy na piętro; powrót nie może odświeżać ofert.
- Dodano przeszkody terenowe (kamienie, doły, okresowe podmuchy), kilka autorskich motywów pięter i autorskie sylwetki fantasy rysowane w Canvas. Grafika jest nadal prototypowa.
- Testy automatyczne nie zastępują ręcznego testu płynności i przyjemności rozgrywki.

## Najważniejszy aktywny zakres pracy
Użytkownik zlecił „mikro rewolucję graficzną” i zgłosił, że ruch/strzelanie nadal są słabe, a generowanie i prezentacja mapy nie są czytelne. Kolejna sesja ma zacząć od audytu aktualnego kodu, a potem realizować poprawki etapami:

1. **Grafika gry:** znacznie bardziej przypominająca ukończoną grę RPG/top-down niż proste kształty. Inspiracje ogólne: estetyka klasycznych RPG typu Margonem oraz użycie map, potworów i itemów w stylu RPG Maker — tylko jako kierunek gatunkowy. Wszystkie grafiki muszą być autorskie, bez kopiowania konkretnych postaci, sprite'ów, map, ikon czy assetów chronionych prawem autorskim.
2. **Autorskie potwory/easter eggi:** magiczne, czytelne sylwetki i rozpoznawalne animowane/rysowane archetypy: wampir, wilkołak, wiedźma, mumia, ogr, smok, krasnolud i komiczna krowa oraz inne własne stworki. Nie zmieniaj mechanicznych archetypów AI przypadkiem — najpierw powiąż nową oprawę z istniejącymi typami wrogów i testami.
3. **Mapa i generowanie:** użytkownik uważa, że generowanie poziomów nadal jest „z pizdy” i mapa nie pokazuje się dobrze. Zbadaj rzeczywisty generator, graf połączeń, pozycjonowanie drzwi, rysowanie minimapy i pełnej mapy, legendę, kamerę/układ pomieszczeń oraz czy pokazane korytarze odpowiadają przejściom. Dodaj testy topologii i czytelności/kontraktów mapy. Nie zmieniaj reguły 30 pokojów bez zgody.
4. **Sterowanie ruchem:** `M` ma być mapą i nie może być jednocześnie zmianą ruchu. Zachowaj osobny, wolny klawisz dla zmiany stylu ruchu (aktualne mapowanie to `V`; sprawdź i ujednolić kod, HUD i instrukcję). Nie psuj obsługi strzałek jako strzelania kierunkowego.
5. **Ruch i strzelanie:** opinia graczy: broń jest zbyt trudna w użyciu; ogólnie ruch i strzelanie nadal są „chujowe”. Nie ograniczaj się do kosmetycznych zmian liczb. Zmierz i popraw sterowanie: responsywność, przyspieszanie/hamowanie, skręcanie, kolizje, celowanie, prędkość i żywotność pocisków, hitboxy, rozrzut oraz feedback trafień. Każdy styl ruchu i każda broń powinny mieć **wyraźnie większą zaletę i większą wadę**, ale podstawowe trafianie ma być wybaczające i satysfakcjonujące. Zrób macierz parametrów oraz testy TTK/obrażeń na bliskim i dalekim dystansie, grupie i linii celów. Nie twierdź, że „przyjemnie się gra”, dopóki nie ma ręcznego playtestu.
6. **Wizualny polish:** itemy i dropy powinny być rozpoznawalnymi ikonami/obiektami, a nie samymi kolorowymi plamami; podłoże i przeszkody muszą odróżniać się od dekoracji i mieć spójne kontrasty. Zadbaj o czytelność w trakcie walki.
7. **Testy i publikacja:** najpierw prywatne SSOT, testy (w tym Chromium jeśli dostępne), review diffu i CI; dopiero potem merge. Następnie zsynchronizuj publiczny mirror i zweryfikuj Pages. Na końcu podaj link do gry, PR, co się zmieniło, wyniki testów oraz co pozostaje niezweryfikowane.

## Następny ruch dla nowego czatu
Nie pytaj użytkownika, od czego zacząć. Zrób aktualny audyt kodu i CI. Wybierz spójny pierwszy pakiet: **mapa/generowanie + kontrole sterowania**, a następnie osobny pakiet grafiki i osobny pakiet balansu ruchu/broni, chyba że audyt ujawni krytyczny błąd blokujący. Przed kodowaniem przejrzyj dokładnie aktualny `index.html` i testy. Każda zmiana ma mieć test regresyjny i aktualizację dokumentacji.


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
