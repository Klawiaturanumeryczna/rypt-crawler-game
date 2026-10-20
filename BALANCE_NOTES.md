# Crypt Crawler — notatki balansu

Stan po wdrożeniu mechanik z 2026-10-18. To wartości startowe do testów, nie wynik testów z udziałem graczy.

## Długość piętra i boss

- Każde piętro ma maksymalnie 30 pokoi. Gracz może zejść wcześniej, gdy pojawi się przejście; po oczyszczeniu pokoju 20 przejście jest gwarantowane, a pokoje 21–30 są opcjonalną eksploracją.
- Na piętrze 1 nie ma bossa. Od piętra 2 boss pojawia się na początku piętra, w pokoju 1. Pokój bossa nie losuje wyjścia na kolejne piętro po jego oczyszczeniu — po zwycięstwie gracz przechodzi do pokoju 2 tego samego piętra.
- HP bossa: `45 + 12 × numer piętra` (57 HP na piętrze 1, 69 na piętrze 2, 81 na piętrze 3).
- Boss strzela wachlarzem trzech pocisków; odstęp ataków wynosi 55–75 klatek.
- Po oczyszczeniu zwykłego pokoju losujemy szansę zejścia równą `numer pokoju × 5 punktów procentowych`: pokój 1 — 5%, pokój 2 — 10% itd. To nowe losowanie po każdym pokoju, a nie jeden próg na całe piętro. Jeśli los się powiedzie, przejście pojawia się w następnym pokoju; ten pokój również trzeba oczyścić, zanim gracz będzie mógł zejść. Pokój bossa na piętrach 2+ nie wykonuje losowania zejścia.
- W pokoju 30 przejście na następne piętro jest gwarantowane, a wszystkie drzwi prowadzą dalej; w pokoju pojawia się też bonusowy przedmiot. Wcześniej zejście może pojawić się losowo, zgodnie z rosnącą szansą po oczyszczonych pokojach.

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
- W pokoju 1 piętra 1 pojawiają się 3 serca i 2 monety, ale nie ma tam ofert ani pickupów przedmiotów. Serca nie znikają przy pełnym zdrowiu; można je zebrać po otrzymaniu obrażeń.
- W sklepie zawsze jest serce za 2 monety. Zakup leczy 2 HP; przy pełnym zdrowiu lub braku monet przycisk zakupu jest nieaktywny.
- Ocena wstępna: 0,5% na monetę było zbyt niskie, by sensownie finansować zakupy. 8% powinno dać walutę na przestrzeni dłuższego piętra, a premia za serię nagradza agresywną grę. Trzeba obserwować, czy łączna liczba monet nie robi leczenia zbyt łatwym.

## Przedmioty

- Początkowe zapasy i oferty przedmiotów pojawiają się wyłącznie w pokoju 1 piętra 1. Kolejne piętra nie rozdają ponownie startowego zestawu. Nie ma jeszcze systemu synergii.
- Podejście na odległość 100 jednostek pokazuje nazwę i efekt. Pickup przedmiotu następuje automatycznie dopiero po wejściu w jego obszar kolizji; nie wymaga klawisza E.
- Przedmioty nóg i strzeleckie modyfikują statystyki przy podniesieniu i wypisują zmianę. Aktywne przedmioty są zużywane po użyciu Spacji.
- Style strzelania różnią się wzorcem, kolorem, rozmiarem i prędkością pocisków. Style ruchu różnią się prowadzeniem, unikiem/poślizgiem i sylwetką. To implementacja prototypowa; balans wymaga testów.
- Obrażenia aktywnych przedmiotów korzystają ze wspólnej funkcji obrażeń wroga; zabójstwa, serie i dropy naliczane są tak samo jak przy pociskach.
- Wszystkie 10 aktywnych przedmiotów ma testy przeglądarkowe efektów i zużycia: leczenie, monety, obrażenia, czyszczenie pocisków, nietykalność i rozrzut ośmiu pocisków. Testy sprawdzają też, że przedmiot 7 trafia wyłącznie najbliższego wroga, a przedmiot 10 jednocześnie rani wszystkich wrogów i usuwa ich pociski. Przedmioty 3, 7 i 10 korzystają ze wspólnej funkcji obrażeń i mogą zadać cios kończący.

## Co testować w pierwszej kolejności

1. Czy gracz ma zwykle 2 monety na leczenie przed końcem piętra, ale nie kupuje serca po każdym pokoju.
2. Czy boss na początku piętra 2+ jest wymagający, lecz możliwy do pokonania bez konkretnego przedmiotu.
3. Czy możliwość eksploracji do 30 pokoi nie wydłuża runu nadmiernie; obserwować, na których pokojach gracze zwykle znajdują i wybierają zejście.
4. Czy trudne drzwi rzeczywiście czują się trudniejsze, a dodatkowy łup rekompensuje ryzyko.
5. Czy tooltip przedmiotu jest czytelny na różnych rozdzielczościach i nie zasłania istotnych pocisków.
6. Czy start z bossem na piętrach 2+ jest czytelny i czy po jego pokonaniu gracz przechodzi do pokoju 2, a nie od razu na następne piętro.
7. Czy komunikat o losowaniu zejścia jasno mówi, że wyjście pojawi się w następnym pokoju i dopiero po oczyszczeniu tego pokoju będzie można z niego skorzystać.


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


## Regresja skalowania HP przeciwników — 2026-10-20

Dodano test przeglądarkowy wywołujący rzeczywistą funkcję `createEnemy()` z kontrolowanymi wartościami piętra i poziomu drzwi. Test zabezpiecza pięć punktów odniesienia: Chaser ma 2 HP na piętrze 1 i 3 HP na piętrze 3; Brute ma 4 HP na łatwych drzwiach i 8 HP na trudnych drzwiach piętra 1; boss piętra 2 ma 69 HP zgodnie z osobnym wzorem. Test nie zmienia balansu — chroni istniejące reguły przed przypadkową regresją. Nie zastępuje testów rozgrywki ani oceny odczuć gracza.


## Płynność sterowania — iteracja 2026-10-20

Bez zmian w animacjach i grafice. Wprowadzono niewielkie korekty wyłącznie fizyki ruchu: Drifter interpoluje prędkość z wagą 0,22 dla wejścia kierunkowego (wcześniej 0,18) i zachowuje 90% prędkości na klatkę po puszczeniu klawiszy; Momentum przyspiesza z wagą 0,14 zamiast 0,09. Celem jest skrócenie czasu dochodzenia do prędkości roboczej i wyraźniejsze rozdzielenie poślizgu od rozpędzania.

Dodano testy przeglądarkowe oparte na rzeczywistej pętli gry: czas dojścia do 95% prędkości, reakcja na zmianę kierunku, wytracanie pędu i prędkość po skosie. Testy chronią granice projektowe, nie zastępują subiektywnego playtestu. Wartości nadal wymagają oceny podczas gry.


Dodatkowy test regresyjny ruchu: dla Runner, Drifter i Momentum prędkość po skosie jest mierzona dopiero po ustaleniu prędkości i musi odpowiadać prędkości na wprost. To odróżnia prawidłową normalizację kierunku od początkowej fazy rozpędzania.


## Modyfikatory terenu — test regresyjny 2026-10-20
- Wartości pozostają bez zmian: piasek ×0,62, lód ×1,25.
- Dodano test przeglądarkowy oparty na rzeczywistej pętli `update()`, który sprawdza mnożniki i przywrócenie normalnego przesuwania po opuszczeniu pola terenu.
- To zabezpieczenie istniejących zasad, nie zmiana balansu. Nie daje też odpowiedzi na subiektywne pytanie, czy ruch po lodzie/piasku jest przyjemny — potrzebny jest ręczny playtest.


## Wstępny balans ról ruchu i broni — 2026-10-20

### Style ruchu
- Biegacz: 3,25 — natychmiastowe start/stop i skręt, bez specjalnej premii.
- Drifter: 3,80 — szybki z długim ślizgiem; trudniej go zatrzymać i zawrócić.
- Skoczek: 2,85 — wolniejszy pomiędzy automatycznymi susami.
- Rozpęd: 4,10 — wysoka prędkość maksymalna, ale stopniowe przyspieszanie.
- Zwinny: 2,90 — niska prędkość bazowa, rekompensowana krótkimi automatycznymi zrywami.
- Taran: 2,85 i 25% mniej obrażeń; wymiana szybkości na wytrzymałość jest teraz mechaniczna, nie tylko wizualna.
- Nie zmieniono interwałów susów (Skoczek: 26 klatek / 6 klatek zrywu; Zwinny: 38 / 4). Testy istniejących pętli ruchu muszą potwierdzić, że role są rozróżnialne i nie łamią normalizacji ruchu po skosie.

### Bronie startowe
- Precyzyjny: 1,25 obrażeń, interwał 21 klatek — mocniejszy strzał, wolniejszy rytm.
- Klasyczny: 1,00 / 17 — punkt odniesienia.
- Rozrzut: 0,36 na pocisk, 3 pociski, interwał 23 — najlepszy z bliska, słabszy z dystansu.
- Szybkostrzelny: 0,62 / 11 — szybkie poprawki celowania, słabszy pojedynczy pocisk.
- Salwa: 0,22 na pocisk, 5 pocisków, interwał 23 — potencjał przeciw grupie, słabe trafienie pojedyncze.
- Przebijający: 0,85 / 23 i do 3 celów — słabszy przeciw jednemu celowi, mocny w linii.
- Wybuchowy: 0,80 / 24 i 60% obrażeń odłamkowych w promieniu 72 px — niski DPS bezpośredni, rekompensowany obszarem.
- DPS na ekranie wyboru jest teoretyczny i zakłada trafienie wszystkich pocisków; rzeczywisty wynik zależy od celności, rozrzutu i ustawienia wrogów.
- Balans jest iteracją startową. Kolejny krok: testy walki w Chromium na równych scenariuszach oraz sprawdzenie czasu zabicia dla każdej broni na jednym i wielu celach.

### Sklep — fizyczne oferty
- Każdy sklep oferuje losowy przedmiot pasywny za 4 monety, losowy przedmiot aktywny za 5 monet i serce za 2 monety (+2 HP). Zakup następuje przez wejście w przedmiot; przy niewystarczającej liczbie monet oferta zostaje na podłodze.
- Ceny 4/5 są prototypowe. Trzeba sprawdzić w testach dłuższego runu, czy waluta wpada wystarczająco często, by sklep był decyzją taktyczną, a nie dekoracją.