# Crypt Crawler — prototyp Hotline Miami

Crypt Crawler to przeglądarkowy top-down roguelike w jednym pliku `index.html`, renderowany przez Canvas. Aktualny build eksperymentuje z szybką, śmiertelną walką inspirowaną Hotline Miami. To nadal prototyp; zielone testy automatyczne nie zastępują ręcznego playtestu.

## Uruchomienie

Otwórz `index.html` w nowoczesnej przeglądarce albo zagraj w [publiczny build GitHub Pages](https://klawiaturanumeryczna.github.io/rypt-crawler-game/).

## Sterowanie

- **WASD** — ruch.
- **Strzałki** — strzelanie kierunkowe; można łączyć osie.
- **Mysz + LPM** — strzał w kierunku kursora.
- **M** — mapa całego piętra; ponowne M zamyka mapę.
- **V** — wybór stylu ruchu.
- **B** — wybór stylu strzelania.
- **Spacja** — użycie aktywnego przedmiotu.
- **P** — pauza / powrót do gry.
- **R** — natychmiastowy restart runu, zachowujący wybrany styl ruchu i strzelania.

Style ruchu i strzelania wybiera się na początku runu. W aktualnym prototypie style ruchu różnią się szybkością, bezwładnością, sposobem skręcania lub krótkim oknem uniku. Nie używaj starszych instrukcji mówiących, że M zmienia ruch albo Shift jest ogólnym przyciskiem uniku — nie opisują bieżącego mapowania.

## Pętla rozgrywki

- Każde piętro ma **10 pokojów** na siatce **5×2**. Pokój 10 jest bossem.
- Aby otworzyć drogę do bossa, trzeba oczyścić wszystkie dziewięć pozostałych pokojów. Samo wejście do pokoju bossa nie kończy piętra.
- Po pokonaniu bossa otwiera się przejście na kolejne piętro.
- Graf połączeń jest generowany dla każdego piętra. Drzwi i mapa muszą opierać się na tym samym grafie, a powrót do odwiedzonego pokoju ma zachowywać jego stan.
- Sklep jest dostępny najwyżej raz na piętro; powrót nie powinien losować od nowa wykorzystanych ofert.

## Zasady walki — bieżący eksperyment

- **Gracz ginie od jednego rzeczywistego trafienia.** Krótkie okna uniku oraz istniejący jednorazowy amulet ratunkowy są wyjątkami wynikającymi z mechaniki, nie dodatkowym standardowym HP.
- **Zwykli przeciwnicy giną od jednego bezpośredniego trafienia.** Boss jest wyjątkiem i wymaga wielu trafień.
- Kamienie pełnią funkcję osłony: blokują ruch, pociski i linię widzenia. Strzał gracza tworzy krótkotrwałe źródło hałasu, które przyciąga pobliskich wrogów do ostatniej znanej pozycji.
- Strzelec musi mieć czystą linię widzenia. Przed strzałem pokazuje linię ostrzegawczą; obecny eksperyment używa 18 klatek przygotowania dla zwykłego strzelca i 24 dla bossa. Kierunek celowania jest blokowany na początku ostrzeżenia.
- Przeciwnicy próbują obchodzić kamienie. Testy automatyczne obejmują pojedynczą osłonę i jeden scenariusz z dwoma kamieniami, ale nie dowodzą poprawnego zachowania w każdym układzie.
- Ręczny test nadal musi ocenić czytelność ostrzeżeń, uczciwość śmierci, płynność ruchu i ogólną frajdę.

## Przedmioty i trwałe dane

Przedmioty aktywne używa się Spacją. Pasywne mogą zmieniać ruch, strzelanie, statystyki lub zapewniać jednorazowy ratunek. Odkrycia i rekordy profilu są zapisywane lokalnie w przeglądarce; ekwipunek i waluta bieżącego runu nie przechodzą do następnego.

## Testy deweloperskie

Wymagane środowisko: Python, zależności testowe z plików projektu oraz Playwright Chromium.

```bash
python verify.py
python -m pytest tests/browser_smoke.py -q
```

Testy sprawdzają kontrakty źródła i wybrane scenariusze w prawdziwej pętli gry. Nie są automatycznym dowodem balansu ani jakości ręcznego sterowania.

## Źródło prawdy i dokumentacja

- Główne repozytorium (SSOT): https://github.com/Klawiaturanumeryczna/crypt-crawler
- Publiczny mirror: https://github.com/Klawiaturanumeryczna/rypt-crawler-game
- Aktualny status: `PROJECT_STATUS.md`
- Decyzje: `DECISION_LOG.md`
- Hipotezy balansu: `BALANCE_NOTES.md`
- Research: `HOTLINE_MIAMI_RESEARCH_AND_DESIGN.md`
- Scenariusze ręcznego testu: `MANUAL_PLAYTEST_CHECKLIST.md`

Starsze sekcje dokumentacji mogą opisywać poprzednie warianty prototypu. Gdy dokumentacja przeczy bieżącemu kodowi `index.html`, sprawdź kod i aktualne testy, a następnie popraw rozbieżność — nie zakładaj, że historyczny opis jest aktualny.
