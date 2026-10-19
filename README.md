# Crypt Crawler — prototyp 0.4.0

Crypt Crawler to przeglądarkowy roguelike z widokiem z góry. Gra korzysta z Canvas i jednego pliku `index.html`; nie wymaga instalowania silnika ani zewnętrznych grafik.

## Uruchomienie

Otwórz `index.html` w nowoczesnej przeglądarce i kliknij **ROZPOCZNIJ RUN**.

## Sterowanie

- **WASD** — ruch.
- **Strzałki** — strzelanie w ośmiu kierunkach.
- **Mysz + przytrzymany LPM** — strzelanie w stronę kursora.
- **E** — podniesienie przedmiotu po podejściu do niego.
- **Spacja** — użycie aktywnego przedmiotu; aktywny przedmiot zostaje zużyty.
- **P** — pauza / powrót do gry.
- **R** — rozpoczęcie nowego runu.
- **Shift** — krótki sus w stylu ruchu „Skoczek”.
- Nie ma już menu ani klawisza M do wybierania stylu ruchu — styl wybiera się przez podniesienie przedmiotu.

## Pętla rozgrywki

Każde piętro ma maksymalnie **30 pokoi**. Na piętrze 1 nie ma bossa; od piętra 2 boss pojawia się na początku piętra, w pokoju 1. Po pokonaniu bossa przechodzisz do pokoju 2 tego samego piętra. Po oczyszczeniu zwykłych pokoi rośnie szansa pojawienia się przejścia: próg wynosi 5% w pokoju 1, 10% w pokoju 2 i tak dalej. W pokoju 20 przejście jest gwarantowane, ale można je zignorować i eksplorować do pokoju 30. Oczyszczenie pokoju 30 gwarantuje przejście i daje bonusowy przedmiot. Szansa jest skumulowanym progiem losowanym na początku piętra, a nie nowym niezależnym losowaniem w każdym pokoju.

Tylko na początku pierwszego piętra pojawiają się zapasy startowe: 3 serca do podniesienia, 2 monety oraz oferty przedmiotów. Kolejne piętra nie przyznają ponownie zestawu startowego. Przedmioty trzeba podnosić klawiszem **E**.

## Style ruchu i przedmioty

Dostępnych jest sześć stylów ruchu: Podstawowe bieganie, Szybki ślizg, Skoczek, Rozpęd, Zwinny i Ciężki krok. Podniesienie kolejnego przedmiotu ruchu zastępuje obecny styl.

Przedmioty aktywne są używane Spacją. Przedmioty na nogi i do strzelania modyfikują statystyki przy podniesieniu. Nie ma obecnie systemu synergii. Część aktywnych efektów zadaje obrażenia, ale nie może bezpośrednio dobić wroga — to znane ograniczenie prototypu.

## Drzwi, zagrożenie i sklep

- **Szare drzwi — łatwe:** liczba wrogów ×0,75; szybkość ×0,92; szansa na łup ×0,75.
- **Złote drzwi — średnie:** mnożniki ×1,00.
- **Czerwone drzwi — trudne:** liczba wrogów ×1,25 (z limitem pokoju); szybkość ×1,08; szansa na łup ×1,50.
- Trudne drzwi zwiększają także udział cięższych archetypów w puli przeciwników.
- Fioletowe drzwi prowadzą do sklepu. Sklep jest gwarantowany w pokoju 2, o ile gracz wybierze dalszą drogę zamiast wcześniejszego przejścia na kolejne piętro. Można go odwiedzić raz na piętro.
- Serce w sklepie kosztuje **2 monety** i przywraca **2 HP**. Zakup jest wyłączony przy pełnym zdrowiu lub braku monet.
- Moneta wypada z bazową szansą 8%, serce z bazową szansą 2,5% za pokonanego wroga, przed mnożnikiem trudności drzwi. Serce na ziemi nie znika przy pełnym zdrowiu.
- Każde 5 zabójstw w serii podtrzymywanej przez kolejne zabójstwo w ciągu 3 sekund daje dodatkową monetę.
- Przejście na piętro leczy do 2 HP.

## Wrogowie i boss

Pula przeciwników zmienia się wraz z piętrem. Zwykłe HP rośnie o 14% na piętro, szybkość o 3,5% na piętro z limitem premii 30%. Boss pojawia się na początku każdego piętra od piętra 2 i ma `45 + 12 × numer piętra` HP; strzela wachlarzem trzech pocisków. Szczegóły znajdują się w [ENEMY_PROGRESSION.md](ENEMY_PROGRESSION.md) oraz [BALANCE_NOTES.md](BALANCE_NOTES.md).

## Znane ograniczenia i testy

- To nadal prototyp: brakuje zapisu postępu między runami, trwałych odblokowań, rozbudowanego grafu pokoi i pełnego systemu synergii.
- Parametry balansu wymagają testów rozgrywki; testy automatyczne nie zastępują wielokrotnego przejścia piętra.
- `python verify.py` — statyczne sprawdzenie źródła.
- `python tests/browser_smoke.py` — test dymny Playwright; wymaga pakietu Playwright i przeglądarki Chromium.
