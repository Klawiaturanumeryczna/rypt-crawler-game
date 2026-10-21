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

## Empiryczny test czasu zadawania obrażeń — 2026-10-20

Dodano test Chromium, który strzela przez rzeczywistą pętlę gry do nieruchomego celu i mierzy liczbę klatek potrzebnych do zadania co najmniej 5 obrażeń. Każdy z siedmiu stylów broni jest badany z bliska (40 px) i z dystansu (180 px). Test wymaga, by każdy styl rzeczywiście trafiał cel, oraz sprawdza, czy Rozrzut i Salwa działają szybciej z bliska niż z daleka. Wynik uwzględnia czas dolotu, szybkostrzelność, rozrzut i kolizje — nie tylko teoretyczny DPS.

To test regresyjny w kontrolowanych warunkach, nie dowód na ostateczny balans: nie modeluje poruszających się przeciwników, uników gracza, presji kilku wrogów ani pełnej walki. Nie zmienia parametrów produkcyjnych. Po uruchomieniu CI należy zachować rzeczywiste wyniki przed rozważaniem kolejnych zmian balansu.


### Wynik pomiaru Chromium (2026-10-20)

Czas do co najmniej 5 obrażeń, w klatkach gry (nieruchomy cel, rzeczywiste pociski i kolizje):

| Broń | 40 px | 180 px |
|---|---:|---:|
| Precyzyjny | 64 | 81 |
| Klasyczny | 70 | 89 |
| Rozrzut | 95 | 321 |
| Szybkostrzelny | 90 | 106 |
| Salwa | 94 | 526 |
| Przebijający | 117 | 134 |
| Wybuchowy | 146 | 169 |

Wynik potwierdza mocną zależność Rozrzutu i Salwy od dystansu. Precyzyjny wypada szybciej niż Klasyczny w tym kontrolowanym teście; Szybkostrzelny nie jest tu najszybszy mimo krótkiego interwału, ponieważ zadaje mniejsze obrażenia na trafienie. Przebijający i Wybuchowy wypadają wolniej przeciw pojedynczemu celowi, co pasuje do ich ról przeciw grupom. To tylko punkt odniesienia: test nie modeluje poruszających się wrogów, wielu celów, presji walki ani błędów celowania. Nie zmieniono statystyk broni na podstawie samego tego pomiaru.


## Test ról broni przeciw grupie — 2026-10-20

Rozszerzono test Chromium o stały scenariusz 180 klatek z trzema nieruchomymi celami: w skupisku (różnica pionowa 32 px) oraz ustawionymi w linii (odstęp poziomy 25 px). Test ma sprawdzać, czy Rozrzut, Salwa i Wybuchowy rzeczywiście trafiają cele poza osią środkowego strzału, a Przebijający może zadawać obrażenia trzem celom ustawionym w jednej linii. Klasyczny służy jako kontrola, która nie powinna trafiać celów poza linią ani za pierwszym celem. To test rzeczywistych pocisków i kolizji, bez zmiany statystyk broni; wyniki są zależne od ograniczonego scenariusza i nie zastępują walki z poruszającymi się wrogami.


### Wynik testu grupowego Chromium (2026-10-20)

Łączne obrażenia po 180 klatkach; trzy cele nieruchome z 130 px dystansu. „Skupisko” oznacza cele na tej samej osi poziomej i ±32 px pionowo; „linia” oznacza cele w jednej linii, oddalone poziomo o 25 px.

| Broń | Skupisko | Linia |
|---|---:|---:|
| Precyzyjny | 11,25 | 11,25 |
| Klasyczny | 10,00 | 10,00 |
| Rozrzut | 8,64 | 2,88 |
| Szybkostrzelny | 9,92 | 9,92 |
| Salwa | 8,80 | 5,28 |
| Przebijający | 6,80 | 20,40 |
| Wybuchowy | 12,32 | 12,32 |

Wyniki potwierdzają odrębne zachowanie: Przebijający zadał 6,8 obrażeń każdemu z trzech celów w linii, a Wybuchowy zadał obrażenia wszystkim celom dzięki odłamkom. Rozrzut i Salwa trafiają cele poza osią przy skupisku, lecz ich łączne obrażenia w tym scenariuszu są niższe niż Klasycznego. To może być właściwa cena za pokrycie obszaru, ale wymaga oceny podczas gry.

Sygnał do dalszej analizy: Precyzyjny zadał 11,25 wobec 10,00 obrażeń Klasycznego w tym samym oknie 180 klatek przeciw jednemu celowi i utrzymuje większe obrażenia pojedynczego trafienia. Nie zmieniono parametrów; sprawdzić podczas ręcznego playtestu, czy większy pocisk i szybszy lot uzasadniają tę przewagę, czy należy skorygować jeden z tych parametrów.


## Ryzyko dostępności zakupów w pierwszym sklepie — 2026-10-20

Sklep jest dostępny przez drzwi z pokoju 2. Gracz zaczyna z 0 monetami, ale pokój startowy zawiera dwa dropy monet (po ich zebraniu ma 2); pasywny przedmiot kosztuje 4, aktywny 5, serce 2. Bazowa szansa na monetę z pokonanego wroga wynosi 8% (mnożona przez trudność pokoju), a nagroda za serię to 1 moneta co 5 kolejnych zabójstw. Poniższe szacunki zakładają 8% dla każdego zabitego wroga, podniesienie wszystkich dropów i brak innych źródeł monet:

| Zabójstwa przed sklepem | Pasywny za 4 — seria utrzymana | Aktywny za 5 — seria utrzymana | Pasywny — bez premii za serię | Aktywny — bez premii za serię |
|---:|---:|---:|---:|---:|
| 4 | 3,44% | 0,19% | 3,44% | 0,19% |
| 5 | 34,09% | 5,44% | 5,44% | 0,45% |
| 6 | 39,36% | 7,73% | 7,73% | 0,85% |

To model matematyczny niezależnych dropów, nie pomiar z długiego runu. Rzeczywista szansa zależy od trudności drzwi, liczby zabójstw, przerwania serii i tego, czy gracz zbierze monety. Sygnał: w pierwszym sklepie serce jest zwykle dostępne, ale zakup przedmiotu może być rzadki, szczególnie aktywnego. Ceny pozostają prototypowe — nie zmieniono ich bez szerszej oceny tempa ekonomii i długości runu.


## Test poprawności zakupów w sklepie — 2026-10-20

Dodano test Chromium dla obu ofert przedmiotów. Przedmiot pasywny ma pozostać na miejscu przy 3 monetach i zostać kupiony przy 4; aktywny ma pozostać na miejscu przy 4 i zostać kupiony przy 5. Test sprawdza rzeczywistą kolizję, zmianę salda i dodanie przedmiotu do ekwipunku. Nie zmienia cen ani zachowania gry; chroni przed przypadkowym zakupem bez środków i regresją warunków zakupu.


## Symulacja dropów ekonomii sklepu przez rzeczywistą logikę zabójstwa — 2026-10-20

Dodano test Chromium, który wywołuje produkcyjną funkcję `damageEnemy()` dla 10 000 zabójstw na każdym poziomie trudności pokoju (łatwy, średni, trudny), z deterministycznym generatorem liczb losowych. Mierzy rzeczywiste dropy monet i serc oraz premię za serię zabójstw. Test sprawdza, czy zaobserwowane częstości mieszczą się w szerokich granicach tolerancji względem skonfigurowanych szans; nie zmienia mechanik gry.

To izolowana symulacja dropów, a nie pełny run: nie symuluje przemieszczania się, podnoszenia dropów, rzeczywistej liczby wrogów w kolejnych pokojach, przeżywalności ani decyzji gracza. Zatem nie mówi bezpośrednio, jaki procent graczy kupi przedmiot za 4/5 monet przed pierwszym sklepem. Wyniki służą do potwierdzenia działania mnożników dropu i premii za serię; ceny pozostają bez zmian do czasu pomiaru pełnego przebiegu ekonomii.


### Wyniki testu ekonomii (Chromium, 2026-10-20)
10 000 prób na poziom trudności: łatwe — 5,67% monet i 2,09% serc; średnie — 7,75% monet i 2,57% serc; trudne — 12,07% monet i 3,75% serc. Premia za serię: 2000 monet na 10 000 kolejnych prób. To izolowany pomiar dropów, nie pełny run ani prognoza zakupów w pierwszym sklepie. Ceny pozostają bez zmian.


## Przeciwnicy — rozróżnienie ruchu i czytelność sklepu (2026-10-21)
Wdrożono prototypowe role ruchu: chaser ściga bezpośrednio; spitter krąży wokół gracza i próbuje utrzymywać dystans; brute porusza się ciężko, z cyklem wolnego marszu i przyspieszenia; dasher wykonuje szarże; hexer manewruje bokiem; boss porusza się zygzakiem i okresowo szarżuje. Różnice sprawdza automatyczny test pojedynczego kroku rzeczywistej pętli gry. To test techniczny rozróżnienia zachowania, nie dowód na końcowy balans.


## Balans ruchu, broni i nagroda bossa — 2026-10-21

- **Ruch:** Drifter i Rozpęd mają wyraźnie wyższy potencjał prędkości, ale zachowują bezwładność; Skoczek i Zwinny są wolni między automatycznymi zrywami; Taran porusza się wolno, lecz redukuje obrażenia o 40%. Biegacz pozostaje najbardziej przewidywalny i precyzyjny.
- **Broń:** Precyzyjny ma mocne trafienie, ale długi odstęp; Szybkostrzelny ma słabe pociski i bardzo krótki odstęp; Rozrzut i Salwa zachowują ograniczenia DPS pojedynczego celu; Przebijający premiuje ustawienie w linii; Wybuchowy zyskuje obrażenia obszarowe kosztem prędkości i tempa.
- **Nagroda bossa:** gwarantowany losowy przedmiot z puli nóg/strzelania, bez dropu monet i serc. Boss otwiera pojedyncze specjalne złote drzwi do następnego piętra; gracz musi do nich dojść. Informacja o nowym piętrze i celu bossa jest widoczna w logu.
- **Przedmiot środowiskowy:** Stalowe Obcasy zwiększają obrażenia i pozostawiają krótkotrwałe pola zadające obrażenia przeciwnikom. Pocisk Oblężniczy nadal zwiększa rozmiar pocisku o 2 kosztem jego prędkości.
- **Czytelność sklepu:** etykiety ofert powiększono do 16 px, opisy i koszt do 15 px; ramka dopasowuje wysokość do zawartości.

Wartości są prototypem do dalszego testowania. Automatyczne testy kontrolują reguły i kontrakty; nadal potrzebny jest ręczny playtest, by ocenić odczucie ruchu i czytelność w trakcie walki.


### Pomiar po wzmocnieniu ról broni — Chromium CI 2026-10-21

Czas eliminacji (klatki; mniej = szybciej) dla pojedynczego celu, bez ruchu przeciwnika:

| Broń | Blisko | Daleko |
|---|---:|---:|
| Precyzyjny | 55 | 72 |
| Klasyczny | 70 | 89 |
| Rozrzut | 80 | 256 |
| Szybkostrzelny | 90 | 106 |
| Salwa | 86 | 440 |
| Przebijający | 152 | 169 |
| Wybuchowy | 147 | 170 |

Test grupowy przez 180 klatek potwierdza role: Rozrzut zadał 3,5 obrażeń każdemu z trzech bliskich celów; Salwa 5,76 celowi centralnemu i 1,92 każdemu z dwóch bocznych; Przebijający 5,25 każdemu z trzech celów w linii; Wybuchowy 5,4 celowi bezpośrednio trafionemu i 3,24 każdemu pobliskiemu celowi. To pomiar kontrolowany, nie ostateczny balans z ruchomymi przeciwnikami.


## 2026-10-21 — układ piętra i przeszkody
- Zmieniono przechodzenie między pokojami na kierunkowe przejścia po stałej siatce 6×5. Każde pole ma sąsiadów zgodnych z położeniem; nie ma losowego teleportowania między niepowiązanymi pokojami.
- Pokój 30 znajduje się w prawym dolnym rogu siatki; gwarantowane zejście znajduje się na jej zewnętrznej krawędzi.
- M otwiera/zamyka dużą mapę piętra. Mały minimap pokoju pozostaje widoczny.
- Kamienie są kolizyjne, dziury ograniczają prędkość i zadają 0,5 obrażenia co 90 klatek, a wentylatory odpychają gracza przez 38 z każdych 180 klatek, gdy gracz jest blisko.
- Ruch po pokoju oczyszczonym nie losuje ponownie przeciwników. Elementy specjalne piasek/lód/ogień pozostają osobną mechaniką.


## 2026-10-21 — korekta losowania zejścia
- Szansa na zejście rośnie o 5 punktów procentowych za każdy unikalny oczyszczony pokój na bieżącym piętrze, a nie za numer pola w siatce.
- Powrót do wysokiego ID (np. pokój 25) nie daje już sztucznie wysokiej szansy, jeśli gracz oczyścił mało pokojów; ponowne czyszczenie odwiedzonego pokoju nie zwiększa licznika.
- Testy Chromium obejmują rozbieżność między ID pokoju a liczbą unikalnych oczyszczonych pokojów.


## 2026-10-21 — trwałość zejścia
- Po wylosowaniu zejście ma przypisany konkretny pokój i stronę drzwi; ponowne wejście odtwarza to samo wyjście zamiast losować inne drzwi.
- Oczekiwanie na zejście nie jest zużywane przez powrót do już odwiedzonego pokoju. Sklep nie dziedziczy oznaczenia zejścia z pokoju, z którego do niego wejść.
- Wyjście bossa i gwarantowane wyjścia z pokoju 30 również zachowują swoją pozycję w obrębie piętra.


## 2026-10-21 — poprawka wyjścia po bossie
- Audyt backtrackingu wykrył osobną ścieżkę: po pokonaniu bossa drzwi były oznaczane jako zejście, ale nie zapisywano ich pokoju i strony. Po powrocie mogło więc pojawić się zejście przy innych drzwiach.
- Pokonanie bossa zapisuje teraz lokalizację wyjścia tak samo jak pozostałe ścieżki. Dodano test Chromium sprawdzający rzeczywistą funkcję obrażeń bossa i zgodność zapisanego kierunku z oznaczonymi drzwiami.


## 2026-10-21 — trwałość stanu pokojów
- Przy wyjściu z pokoju zapisywane są drzwi i ich typy, sklep/zejście, pozostawione dropy, teren specjalny, pola terenu, źródła ognia, przeszkody oraz stan wrogów i pocisków wroga.
- Powrót odtwarza zapisany stan zamiast losować nowy układ drzwi, inne przeszkody lub nowy teren. Pozostawione monety/przedmioty nie znikają tylko dlatego, że gracz zajrzał do sklepu albo wrócił do poprzedniego pokoju.
- Test Chromium sprawdza odtworzenie drzwi, dropu, HP wroga, pocisku, terenu i przeszkody. To test techniczny trwałości stanu, nie ręczny playtest.


## 2026-10-21 — progresja trudności zgodna z mapą
- Liczba potencjalnych wrogów nie używa już numeru pola (`roomNo`), który jest identyfikatorem wierszowym, a nie miarą drogi od startu.
- Progresja wykorzystuje pasmo głębokości oparte na odległości Manhattan (x+y) w siatce 6×5. Dalekie pokoje są trudniejsze, a sąsiednie pola nie dostają skoku trudności tylko dlatego, że zmienił się numer ID.
- Test Chromium sprawdza kilka punktów mapy, w tym kontrast między pokojem 6 i 7.


## 2026-10-21 — zachowanie trudności po powrocie
- Migawka pokoju zapisuje również poziom trudności drzwi. Powrót z fizycznego sklepu nie zmienia już trudnego/łatwego pokoju na średni w HUD ani w logice dropów.
- Test Chromium sprawdza, że pokój zapisany na poziomie trudnym pozostaje na tym samym poziomie po odtworzeniu.


## 2026-10-21 — ekonomia sklepu: blokada przerzucania ofert
- Sklep jest jednorazowy na piętro: po powrocie do pokoju wejściowego jego drzwi nie otwierają ponownie sklepu. Zapobiega to nieograniczonemu odświeżaniu losowych przedmiotów.
- Nie zmieniono cen ani dropów; zmiana zamyka lukę w ekonomii.
