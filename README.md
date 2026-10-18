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

Każde piętro ma dokładnie **20 pokoi**. Boss pojawia się w pokoju 20. Na początku piętra losowany jest próg przejścia: po oczyszczeniu pokoju 1 szansa wynosi 5%, pokoju 2 — 10%, i tak dalej do 95% w pokoju 19. To skumulowany próg, a nie niezależne losowanie w każdym pokoju; około 5% podejść dociera do bossa. W pokoju 20 przejście jest gwarantowane po oczyszczeniu pokoju.

Na początku pierwszego pokoju pojawiają się 3 serca do podniesienia, 2 monety, 6 przedmiotów ruchu oraz po 2 losowe przedmioty aktywne, na nogi i do strzelania. Przedmioty trzeba podnosić klawiszem **E**.

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

Pula przeciwników zmienia się wraz z piętrem. Zwykłe HP rośnie o 14% na piętro, szybkość o 3,5% na piętro z limitem premii 30%. Boss ma `45 + 12 × numer piętra` HP i strzela wachlarzem trzech pocisków. Szczegóły znajdują się w [ENEMY_PROGRESSION.md](ENEMY_PROGRESSION.md) oraz [BALANCE_NOTES.md](BALANCE_NOTES.md).

## Znane ograniczenia i testy

- To nadal prototyp: brakuje zapisu postępu między runami, trwałych odblokowań, rozbudowanego grafu pokoi i pełnego systemu synergii.
- Parametry balansu wymagają testów rozgrywki; testy automatyczne nie zastępują wielokrotnego przejścia piętra.
- `python verify.py` — statyczne sprawdzenie źródła.
- `python tests/browser_smoke.py` — test dymny Playwright; wymaga pakietu Playwright i przeglądarki Chromium.
