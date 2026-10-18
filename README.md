# Crypt Crawler — prototyp 0.4.0

Crypt Crawler to przeglądarkowy roguelike z widokiem z góry. Prototyp korzysta z Canvas i jednego pliku `index.html`; nie wymaga instalowania silnika ani zewnętrznych grafik.

## Uruchomienie

Otwórz `index.html` w nowoczesnej przeglądarce, kliknij **ROZPOCZNIJ RUN**, a następnie wybierz styl ruchu.

## Sterowanie

- **WASD** — ruch.
- **Strzałki** — strzelanie w ośmiu kierunkach; można łączyć klawisze.
- **Mysz + przytrzymany LPM** — strzelanie w stronę kursora.
- **P** — pauza / powrót do gry.
- **R** — rozpoczęcie nowego runu.
- **M** — ponowny wybór stylu ruchu.
- **Shift** — krótki sus stylu „Skoczek”.
- **E** — podniesienie przedmiotu po podejściu do niego.
- **Spacja** — użycie aktywnego przedmiotu; przedmiot jest zużywany.

## Pętla rozgrywki

Każde piętro ma **20 pokoi na piętrze 1**, a każde następne piętro dodaje 2 pokoje. Ostatni pokój piętra jest walką z bossem. Po jego pokonaniu wszystkie drzwi prowadzą na następne piętro. Wcześniejsze przejście może pojawić się przed bossem, więc nie każdy run musi kończyć się walką z nim.

Pokoje korzystają z tego samego szablonu areny, ale rozmieszczenie i zestaw wrogów są losowe. W grze są Chaser, Spitter, Brute, Dasher, Hexer i boss piętra.

## Style ruchu

Na początku runu i każdego nowego piętra wybierasz jeden z sześciu stylów: Podstawowe bieganie, Szybki ślizg, Skoczek, Rozpęd, Zwinny lub Ciężki krok. **M** pozwala ponownie otworzyć wybór. Przedmioty pasywne mogą zmieniać statystyki; bonus prędkości z przedmiotów wpływa na faktyczny ruch, nie tylko na odczyt HUD.

## Drzwi i ryzyko/nagroda

Zwykłe drzwi mają trzy poziomy:
- **Szare — łatwe:** liczba wrogów ×0,75; szybkość wrogów ×0,92; bazowa szansa na łup ×0,75.
- **Złote — średnie:** mnożniki ×1,00.
- **Czerwone — trudne:** liczba wrogów ×1,25 (z limitem pokoju); szybkość wrogów ×1,08; bazowa szansa na łup ×1,50.

Cztery poziomy są losowane oddzielnie. Jeśli wszystkie cztery drzwi wylosują ten sam poziom, jedno losowe drzwi jest losowane ponownie, więc nigdy nie zostają cztery jednakowe. Po wejściu kolor wybranych drzwi określa trudność następnego pokoju. Specjalne obramowanie sklepu i oznaczenie przejścia na piętro są niezależne od bazowego koloru trudności.

Przejście na kolejne piętro może wylosować się w oczyszczonym pokoju według wzoru `(numer pokoju / limit pokoi)^30`. W ostatnim pokoju, po pokonaniu bossa, przejście jest gwarantowane. Szczegóły balansu opisuje [BALANCE_NOTES.md](BALANCE_NOTES.md).

## Przedmioty, monety i sklep

W pierwszym pokoju każdego piętra pojawiają się **trzy losowe oferty**: jeden aktywny przedmiot, jeden przedmiot nóg i jeden przedmiot strzelecki. Nazwa, opis działania i instrukcja podniesienia pojawiają się po zbliżeniu na odległość 100 jednostek; użyj **E**, aby go zebrać. Przedmioty pasywne zmieniają statystyki i raportują wartości przed/po. Aktywne przedmioty działają po naciśnięciu Spacji i są zużywane. Nazwy są na razie technicznymi etykietami „Item N”, ale efekty i opisy działania są zaimplementowane.

- **Moneta:** 8% bazowej szansy na pokonanego wroga.
- **Serce:** 2,5% bazowej szansy; przywraca 2 HP.
- Mnożnik szansy na łup zależy od trudności wybranych drzwi. Trudne drzwi dają 12% bazowej szansy na monetę i 3,75% na serce.
- **Seria zabójstw:** kolejne zabójstwo w ciągu 3 sekund podtrzymuje serię; każde 5 zabójstw w serii daje dodatkową monetę.
- **Sklep:** ma 8% szansy pojawienia się w kwalifikującym się pokoju i może zostać odwiedzony raz na piętro. Serce kosztuje 2 monety i przywraca 2 HP; przy pełnym zdrowiu albo zbyt małej liczbie monet zakup jest wyłączony.
- Serce na podłodze nie znika, gdy zdrowie jest pełne.

## Ograniczenia i decyzje projektowe

- Efekty aktywnych przedmiotów 3, 7 i 10 celowo zadają obrażenia nieśmiertelne, by nie omijać standardowego liczenia zabójstw i dropów.
- Sklep oferuje na razie tylko leczenie.
- Boss jest powtarzanym strażnikiem piętra, a nie odrębnym finałowym bossem kampanii.
- Brakuje zapisu postępu między runami, trwałych odblokowań, rozbudowanego grafu pomieszczeń, kilku typów pokoi i pełnego systemu synergii. Wartości liczbowe są prototypowe, nie są jeszcze potwierdzonym balansem po testach graczy.

## Dokumentacja i testy

- [BALANCE_NOTES.md](BALANCE_NOTES.md) — aktualne liczby, założenia i ryzyka balansu.
- [ENEMY_PROGRESSION.md](ENEMY_PROGRESSION.md) — progresja wrogów i bossów.
- `python verify.py` — statyczne sprawdzenie źródła.
- `python tests/browser_smoke.py` — test dymny Playwright wymagający zainstalowanego pakietu Playwright i przeglądarki Chromium. Można wskazać przeglądarkę przez zmienną `PLAYWRIGHT_CHROMIUM_EXECUTABLE`.

Testy statyczne nie zastępują pełnego testowania podczas rozgrywki ani strojenia balansu na podstawie wielu runów.
