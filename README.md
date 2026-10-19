# Crypt Crawler — prototyp 0.4.0

Crypt Crawler to przeglądarkowy roguelike z widokiem z góry. Gra korzysta z Canvas i jednego pliku `index.html`; nie wymaga instalowania silnika ani zewnętrznych grafik.

## Uruchomienie

Otwórz `index.html` w nowoczesnej przeglądarce i kliknij **ROZPOCZNIJ RUN**.

## Sterowanie

- **WASD** — ruch.
- **Strzałki** — strzelanie w ośmiu kierunkach.
- **Mysz + przytrzymany LPM** — strzelanie w stronę kursora.
- **Wejście w przedmiot** — automatyczne podniesienie po fizycznym kontakcie; nie trzeba naciskać E.
- **M** — otwiera wybór stylu ruchu podczas runu.
- **Spacja** — użycie aktywnego przedmiotu; aktywny przedmiot zostaje zużyty.
- **P** — pauza / powrót do gry.
- **R** — rozpoczęcie nowego runu.
- **Shift** — krótki sus w stylu ruchu „Skoczek”.
- Style ruchu różnią się prowadzeniem i wyglądem postaci: poślizg, rozpęd, uniki, sus i ciężka sylwetka są widoczne podczas gry.

## Pętla rozgrywki

Każde piętro ma maksymalnie **30 pokoi**. Na piętrze 1 nie ma bossa; od piętra 2 boss pojawia się na początku piętra, w pokoju 1. Po pokonaniu bossa przechodzisz do pokoju 2 tego samego piętra. Po oczyszczeniu zwykłego pokoju losowana jest szansa zejścia: 5% w pokoju 1, 10% w pokoju 2 i tak dalej. Jeśli los się powiedzie, przejście pojawia się w następnym pokoju, który trzeba oczyścić przed zejściem. Po oczyszczeniu pokoju 20 szansa wynosi 100%, więc zejście pojawi się w pokoju 21; można z niego skorzystać albo kontynuować eksplorację. W pokoju 30 przejście jest gwarantowane i pojawia się bonusowy przedmiot.

Tylko w pierwszym pokoju pierwszego piętra pojawiają się 3 serca i 2 monety. Nie ma tam ofert ani pickupów przedmiotów. Kolejne piętra nie przyznają ponownie zestawu startowego. Serca i monety zbiera się przez kontakt; przedmioty również podnoszą się automatycznie po wejściu w ich obszar.

## Style ruchu i przedmioty

Dostępnych jest sześć stylów ruchu: Podstawowe bieganie (natychmiastowe sterowanie), Szybki ślizg (bezwładność), Skoczek (mocny sus na Shift), Rozpęd (płynne przyspieszenie), Zwinny (krótki, częsty unik na Shift) i Ciężki krok (opancerzona sylwetka). Każdy ma inny kolor/kształt postaci. Cztery style strzelania również są widoczne od razu: Precyzyjny (duży złoty pocisk), Klasyczny, Rozrzut (wachlarz trzech różowych pocisków) i Szybkostrzelny (małe, szybkie turkusowe pociski).

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
