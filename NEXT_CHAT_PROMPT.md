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
