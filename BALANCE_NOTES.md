# Crypt Crawler — notatki balansu

Stan po wdrożeniu mechanik z 2026-10-18. To wartości startowe do testów, nie wynik testów z udziałem graczy.

## Długość piętra i boss

- Każde piętro ma maksymalnie 30 pokoi. Gracz może zejść wcześniej, gdy pojawi się przejście; po oczyszczeniu pokoju 20 przejście jest gwarantowane, a pokoje 21–30 są opcjonalną eksploracją.
- Na piętrze 1 nie ma bossa. Od piętra 2 boss pojawia się na początku piętra, w pokoju 1. Pokój bossa nie losuje wyjścia na kolejne piętro po jego oczyszczeniu — po zwycięstwie gracz przechodzi do pokoju 2 tego samego piętra.
- HP bossa: `45 + 12 × numer piętra` (57 HP na piętrze 1, 69 na piętrze 2, 81 na piętrze 3).
- Boss strzela wachlarzem trzech pocisków; odstęp ataków wynosi 55–75 klatek.
- Na początku piętra losowany jest jeden próg przejścia. Po oczyszczeniu zwykłego pokoju porównujemy go z `numer pokoju × 5 punktów procentowych`: pokój 1 — 5%, pokój 2 — 10%, …, pokój 19 — 95%. To próg skumulowany, a nie nowe niezależne losowanie w każdym pokoju. Pokój bossa na piętrach 2+ nie zużywa tego progu.
- W pokoju 20 przejście na następne piętro jest gwarantowane. Jeśli gracz chce, może je zignorować i eksplorować do pokoju 30. Po oczyszczeniu pokoju 30 wszystkie drzwi prowadzą dalej, a na piętrze pojawia się bonusowy przedmiot.

## Liczba i siła zwykłych wrogów

- Bazowy limit losowanej liczby wrogów w pokoju: `min(8, 2 + piętro + floor(numer pokoju / 5))`; faktyczna liczba to losowanie od 1 do limitu, potem mnożnik drzwi i zaokrąglenie.
- Drzwi: łatwe ×0,75 liczby wrogów i ×0,92 szybkości; średnie ×1,00; trudne ×1,25 liczby i ×1,08 szybkości.
- Bazowe HP zwykłych wrogów rośnie o 14% na piętro (z zaokrągleniem); szybkość rośnie o 3,5% na piętro, maksymalnie o 30%, przed mnożnikiem trudności drzwi.
- Cel tej zmiany: uniknąć dawnego skoku do nawet 20 zwykłych wrogów w jednym pokoju oraz sytuacji, w której późniejsze piętra generowały mniej przeciwników niż pierwsze.
- Ryzyko do obserwacji: zaokrąglanie HP sprawia, że część przeciwników nagle wymaga dodatkowego trafienia na wybranych piętrach. Jeśli walka zacznie się przeciągać, lepiej obniżyć HP lub dodać warianty ataków, zamiast dalej zwiększać HP.

## Ekonomia i leczenie

- Moneta: 8% bazowej szansy na zabitego wroga. Serce wypada z bazową szansą 2,5%.
- Mnożnik łupu z drzwi: łatwe ×0,75, średnie ×1,00, trudne ×1,50. Na trudnych drzwiach daje to 12% na monetę i 3,75% na serce.
- Serce przywraca 2 HP. Serce leżące na ziemi nie znika, gdy gracz ma pełne zdrowie.
- Za serię pięciu zabójstw w oknie trzech sekund przyznawana jest dodatkowa moneta.
- Sklep jest gwarantowany w pokoju 2 jako fioletowe drzwi; po wejściu do sklepu nie pojawia się ponownie na tym samym piętrze.
- Tylko w pokoju 1 piętra 1 pojawiają się 3 serca do zebrania i 2 monety. Serca nie znikają przy pełnym zdrowiu; można je zebrać po otrzymaniu obrażeń.
- W sklepie zawsze jest serce za 2 monety. Zakup leczy 2 HP; przy pełnym zdrowiu lub braku monet przycisk zakupu jest nieaktywny.
- Ocena wstępna: 0,5% na monetę było zbyt niskie, by sensownie finansować zakupy. 8% powinno dać walutę na przestrzeni dłuższego piętra, a premia za serię nagradza agresywną grę. Trzeba obserwować, czy łączna liczba monet nie robi leczenia zbyt łatwym.

## Przedmioty

- Początkowe zapasy i oferty przedmiotów pojawiają się wyłącznie w pokoju 1 piętra 1. Kolejne piętra nie rozdają ponownie startowego zestawu. Nie ma jeszcze systemu synergii.
- Podejście na odległość 100 jednostek pokazuje nazwę, efekt i instrukcję `E — PODNIEŚ`. Przedmiot nie podnosi się automatycznie.
- Przedmioty nóg i strzeleckie modyfikują statystyki przy podniesieniu i wypisują zmianę. Aktywne przedmioty są zużywane po użyciu Spacji.
- Obrażenia aktywnych przedmiotów korzystają ze wspólnej funkcji obrażeń wroga; zabójstwa, serie i dropy naliczane są tak samo jak przy pociskach.
- To nadal prototyp: przedmioty aktywne 3, 7 i 10 nie zabijają przeciwników bezpośrednio. W dalszej iteracji należy podłączyć ich obrażenia do wspólnej funkcji śmierci wroga, jeśli mają móc dobijać.

## Co testować w pierwszej kolejności

1. Czy gracz ma zwykle 2 monety na leczenie przed końcem piętra, ale nie kupuje serca po każdym pokoju.
2. Czy boss na początku piętra 2+ jest wymagający, lecz możliwy do pokonania bez konkretnego przedmiotu.
3. Czy możliwość eksploracji do 30 pokoi nie wydłuża runu nadmiernie; obserwować, jak często gracze korzystają z wyjścia w pokoju 20.
4. Czy trudne drzwi rzeczywiście czują się trudniejsze, a dodatkowy łup rekompensuje ryzyko.
5. Czy tooltip przedmiotu jest czytelny na różnych rozdzielczościach i nie zasłania istotnych pocisków.
6. Czy start z bossem na piętrach 2+ jest czytelny i czy gracz rozumie, że po walce przechodzi do pokoju 2, a nie od razu na następne piętro.


## Ustalenia projektowe zapisane 2026-10-19

- Główny cel runu łączy przechodzenie pięter, budowanie silnego buildu i odkrywanie kombinacji.
- Meta-progresja ma przede wszystkim odblokowywać nowe możliwości; trwałe ulepszenia mogą istnieć, ale nie mogą automatycznie odbierać wyzwania.
- Synergie powinny dawać wyraźne przewagi, a wybrane zestawy mogą radykalnie zmieniać sposób gry.
- Eksploracja i szybkie przechodzenie są równorzędnymi strategiami. Dodatkowe ryzyko może dawać lepsze nagrody, lecz eksploracja nie może być obowiązkowym grindem.
- Familianci mają docelowo być pełnym systemem: unikalne zdolności, synergie z przedmiotami, ewolucje/formy i ograniczona liczba aktywnych miejsc. Szczegółowy limit i kompromisy pozostają do zaprojektowania.
- Piętra mają różnić się mechanikami, wydarzeniami, sekretami i nagrodami; bossowie mają obejmować różne poziomy złożoności, w tym opcjonalnych/ukrytych przeciwników.
- Trudność ma rosnąć przez nowe zagrożenia, zachowania i bossów, a nie głównie przez pompowanie HP.
- Rzadkość przedmiotu nie oznacza automatycznie większej siły; przedmioty mogą pełnić różne role, transformować postać i tworzyć wyjątkowe synergie.
- Pomysły poza aktualnym zakresem: (1) Sandbox/Kreator do ręcznego ustawiania mobów, przedmiotów i buildów oraz testowania synergii; (2) osobny tryb Auto-Battle/Menedżer, w którym postać sama się porusza i walczy, a gracz zarządza buildem, modyfikatorami i mnożnikami. Nie implementować tych trybów w obecnej iteracji.
