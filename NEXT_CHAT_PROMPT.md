# PROMPT DLA NOWEGO CZATU — CRYPT CRAWLER / HOTLINE MIAMI EXPERIMENT

Wklej całość do nowego czatu w projekcie Rogal:

---

Kontynuujesz rozwój gry **Crypt Crawler**. Pracuj autonomicznie i najpierw odzyskaj kontekst z repozytorium — nie każ mi powtarzać decyzji, które są zapisane.

## 1. Źródło prawdy i pliki do przeczytania
Główne repozytorium (źródło prawdy): https://github.com/Klawiaturanumeryczna/crypt-crawler  
Publiczny mirror: https://github.com/Klawiaturanumeryczna/rypt-crawler-game  
Pages: https://klawiaturanumeryczna.github.io/rypt-crawler-game/

Przeczytaj w tej kolejności:
1. `NEXT_CHAT_HANDOFF.md` — najważniejszy stan przekazania.
2. `PROJECT_STATUS.md` — bieżący status.
3. `DECISION_LOG.md` — decyzje użytkownika i czego nie wolno samowolnie zmieniać.
4. `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md` — research HLM1/HLM2, źródła, decyzje i kryteria akceptacji.
5. `BALANCE_NOTES.md` — aktualne hipotezy balansu.
6. `MANUAL_PLAYTEST_CHECKLIST.md` — ręczne scenariusze testowe.
7. `verify.py` i `tests/browser_smoke.py` — rzeczywiste kontrole automatyczne.

Nie zakładaj, że starsza historia czatu jest dokładna względem repo. Sprawdź faktyczny HEAD gałęzi, otwarte PR-y, ostatnie CI, różnice względem main i status deploymentu.

## 2. Backup — punkt powrotu, nie nadpisuj
Przed eksperymentem zapisano punkt powrotu:
- Branch: `backup/pre-hotline-miami-2026-10-22`
- Commit: `b26b5d913fb06d0f124d92a9a17d24ae031df91c`

To wersja z 10 pokojami na piętro; pokoje 1–9 muszą zostać oczyszczone, pokój 10 jest bossem, a zejście odblokowuje się dopiero po pokonaniu bossa. Zwinny ma odrębny, wyraźny zryw, a Skoczek nie rysuje smug tylko z lewej strony. Ta gałąź jest punktem powrotu. Nie commituj do niej eksperymentu i nie przesuwaj jej refa bez wyraźnej potrzeby.

## 3. Aktywny eksperyment
- Prototyp Hotline został scalony do main w PR #52, commit `21b828777bd42ecd344cd15b9700445651162ff3`; CI jest zielone dla dokładnego HEAD.
- Gałąź robocza/historyczna: `experiment/hotline-miami-combat-v2`; PR #52: https://github.com/Klawiaturanumeryczna/crypt-crawler/pull/52.
- Mirror i Pages wymagają synchronizacji. Ręczny playtest nie został wykonany, więc nie uznawaj balansu ani pathfindingu za potwierdzone.
- Założenie: zachować własną tożsamość Crypt Crawlera, ale przebudować walkę na szybką i śmiertelną, inspirowaną zasadami HLM1/HLM2.
- Prototyp implementuje jedno życie gracza, śmierć zwykłych przeciwników od dowolnego trafienia, wielotrafieniowego bossa, kamienie jako osłonę blokującą linię widzenia i pociski oraz przyciąganie pobliskich wrogów do miejsca strzału. Wrogowie dystansowi powinni strzelać tylko przy czystej linii widzenia.
- Sprawdź bieżący stan branch/CI — status zapisany w plikach może być starszy niż najnowszy commit.

## 4. Tryb pracy — ważne
- `OK, rob`: audytuj aktualny stan, wybierz największy realny problem, wprowadź poprawkę, dodaj/aktualizuj testy, uruchom weryfikację, sprawdź wyniki i dokumentację, a potem przejdź do następnego zadania bez pytania „co dalej?”, jeśli można sensownie kontynuować.
- `START`: pełny autonomiczny maraton tak długo, jak istnieje sensowna praca bez decyzji użytkownika.
- Nie pytaj, od czego zacząć, jeśli można wywnioskować następny krok z plików, testów i CI.
- Nie zgaduj nazw funkcji, wartości, wyników testów ani statusu wdrożenia. Pobierz kod i sprawdź.
- Nie deklaruj ręcznego playtestu, jeśli go nie wykonano.
- **Nie scalaj przy czerwonym ani pending CI.** Najpierw diagnozuj logi, napraw i ponownie sprawdź.
- Po zmianie main synchronizuj mirror, porównaj SHA wszystkich zmienionych plików, sprawdź CI mirrora i Pages deployment.
- W ważnych decyzjach aktualizuj `NEXT_CHAT_HANDOFF.md`, `PROJECT_STATUS.md`, `DECISION_LOG.md` i w razie balansu `BALANCE_NOTES.md`.
- Dokumentacja po polsku; nazwy techniczne/keywords mogą pozostać po angielsku.
- W odpowiedziach zaznaczaj 🔴 tylko wtedy, gdy naprawdę potrzebujesz mojej decyzji.

## 5. Cele testowania eksperymentu HLM
Najpierw sprawdź:
1. Czy gracz ginie od jednego rzeczywistego trafienia, bez przypadkowego damage reduction, poza celowo istniejącym jednorazowym ratunkiem i wyraźnymi oknami uniku.
2. Czy zwykły wróg ginie od jednego trafienia niezależnie od bazowego mnożnika broni.
3. Czy kamienie blokują gracza, przeciwników, pociski gracza, pociski wrogów i linię widzenia.
4. Czy hałas po strzale przyciąga pobliskich wrogów do wiarygodnego punktu.
5. Czy wróg nie strzela przez osłonę ani nie zabija gracza z nieczytelnej pozycji.
6. Czy przeciwnicy potrafią obchodzić osłonę, a nie blokują się na niej.
7. Czy restart R jest natychmiastowy, zachowuje wybraną broń/ruch i nie wymaga ponownego przechodzenia ekranów wyboru.
8. Czy ekonomia serc/sklepu jest użyteczna w trybie jednego życia, a amulet ratunkowy nie może się niekontrolowanie stackować.
9. Czy 10-pokojowa progresja, boss gate, trwały stan pokoi, sklep, ekonomia, broń i sterowanie nadal przechodzą testy.
10. Czy wybór broni nie obiecuje DPS, gdy standardowy przeciwnik ginie od jednego trafienia.
11. Po zielonym CI — przeprowadź lub przygotuj do wykonania ręczny playtest i uczciwie zapisz, co faktycznie sprawdzono.

Research to hipotezy projektowe, nie dowód, że prototyp już jest przyjemny. Społecznościowe posty są jakościowymi anegdotami, nie reprezentatywną ankietą. Unikaj głównych krytyk HLM2: niespójnego AI, strzałów z nieczytelnych/off-screen pozycji i sztucznej trudności wynikającej z braku informacji.

## 6. Oczekiwany rezultat
Nie kończ na opisie pomysłów. Zmień kod, dodaj testy, zweryfikuj CI, zapisz decyzje i aktualizuj ten handoff. Jeśli eksperyment jest gorszy, przygotuj bezpieczny powrót do gałęzi backupowej zamiast nadpisywać ją kolejnymi zmianami.

Na start wykonaj audyt bieżącego HEAD, PR-ów i CI w repo, potem kontynuuj w trybie `OK, rob`.


## 7. Świeży stan sprawdzony 2026-10-22 — przeczytaj, zanim ruszysz
- Aktualny main HEAD przy ostatniej weryfikacji: `6ae4fb9630dfb90f43c260eaeb6743a8f703676b`. Zawsze sprawdź ponownie live HEAD przed zmianami.
- PR #52 został scalony; kodowy commit HLM `21b828777bd42ecd344cd15b9700445651162ff3` ma zielony run push: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39805994523.
- CI dla obecnego main HEAD `6ae4fb9630dfb90f43c260eaeb6743a8f703676b` jest zielone: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39808650676. `Verify source invariants` i `Test game in Chromium` przeszły.
- Backup `backup/pre-hotline-miami-2026-10-22` istnieje i wskazuje na `b26b5d913fb06d0f124d92a9a17d24ae031df91c`. Potwierdź SHA przed użyciem; nigdy nie przesuwaj tej gałęzi.
- Zweryfikowano zgodne SHA 10 kluczowych plików main/mirror; mirror workflow zakończony sukcesem: https://github.com/Klawiaturanumeryczna/rypt-crawler-game/actions/runs/39806755919. Przed kolejną zmianą ponownie sprawdź live status.
- PR #45 z wcześniejszą próbą 10-pokojową został zamknięty bez merge. Nie traktuj go jako bieżącego źródła prawdy; stan 10-pokojowy zachowuje backup wymieniony wyżej.
- Najważniejsza niezweryfikowana rzecz: ręczny playtest nie został wykonany. Po sprawdzeniu CI kontynuuj w trybie `OK, rob` — priorytetem jest synchronizacja mirror/Pages, potem rzeczywisty playtest i poprawki wynikające z obserwacji.


## 8. Aktualizacja stanu — sprawdzone 2026-10-22 17:48 UTC+2

Ten blok zastępuje wcześniejsze statusy w sekcji 7, jeśli są sprzeczne.

- Aktualny main HEAD: `6ae4fb9630dfb90f43c260eaeb6743a8f703676b`.
- Dokładny HEAD ma zielony browser-smoke CI: https://github.com/Klawiaturanumeryczna/crypt-crawler/actions/runs/39808650676. Kroki `Verify source invariants` i `Test game in Chromium` zakończyły się sukcesem.
- PR #52 z prototypem Hotline jest scalony. PR #53 z dokumentacją/checklistą jest scalony.
- Backup jest potwierdzony: `backup/pre-hotline-miami-2026-10-22` → `b26b5d913fb06d0f124d92a9a17d24ae031df91c`. Nie ruszaj tej gałęzi.
- Zweryfikowano zgodność SHA plików: `index.html`, `verify.py`, `tests/browser_smoke.py`, `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md`, `NEXT_CHAT_PROMPT.md`, `NEXT_CHAT_HANDOFF.md`, `PROJECT_STATUS.md`, `DECISION_LOG.md`, `BALANCE_NOTES.md`, `MANUAL_PLAYTEST_CHECKLIST.md` są identyczne między main i publicznym mirrorem.
- Mirror workflow zakończony sukcesem: https://github.com/Klawiaturanumeryczna/rypt-crawler-game/actions/runs/39806755919. To potwierdza wdrożenie Pages dla aktualnego mirrora; sprawdź ponownie na żywo przed kolejnym deployem.
- Ręczny playtest nie został wykonany. Największe otwarte ryzyko: proste omijanie kamieni przez AI może powodować blokowanie wrogów. Użyj `MANUAL_PLAYTEST_CHECKLIST.md` i zapisuj wyłącznie rzeczywiście zaobserwowane wyniki.
