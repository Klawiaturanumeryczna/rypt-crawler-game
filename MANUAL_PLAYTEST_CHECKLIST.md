# Crypt Crawler — ręczna lista testów grywalności

**Cel:** sprawdzić rzeczy, których CI/Chromium nie potrafi wiarygodnie ocenić: czytelność podczas walki, odczucie sterowania i to, czy mapa pomaga orientować się w lochu.

**Zasada raportowania:** zaznaczaj wyłącznie faktycznie sprawdzone pozycje. Nie traktuj zielonego CI jako potwierdzenia przyjemności z gry. Nie oceniaj balansu na podstawie jednego podejścia.

Gra: https://klawiaturanumeryczna.github.io/rypt-crawler-game/

## 1. Start i skróty

- [ ] Rozpocznij nowy run i wybierz styl strzelania, a następnie styl ruchu.
- [ ] Przytrzymaj V przez chwilę: wybór ruchu nie powinien otwierać się wielokrotnie.
- [ ] Naciśnij V raz: wybór ruchu otwiera się; po wybraniu stylu wracasz do gry.
- [ ] Naciśnij M: mapa piętra otwiera się; ponowne M ją zamyka.
- [ ] Sprawdź, że M nie otwiera wyboru ruchu, a V nie przełącza mapy.
- [ ] Sprawdź P (pauza) i R (restart) oraz to, czy restart rozpoczyna nowy run zgodnie z zamiarem.

## 2. Ruch

Przetestuj każdy styl przez co najmniej 20–30 sekund w otwartej przestrzeni, a następnie w pobliżu ścian i pocisków.

- [ ] Biegacz — natychmiastowa reakcja na zmianę kierunku.
- [ ] Drifter — lekki poślizg, który nie utrudnia precyzyjnego omijania.
- [ ] Rozpęd — wyraźniejsze przyspieszanie i bezwładność, ale hamowanie nadal pod kontrolą.
- [ ] Skoczek — rytmiczny sus jest widoczny, ale nie myli się ze zwykłym ruchem.
- [ ] Zwinny — zryw występuje po ostrym skręcie, nie podczas trzymania jednego kierunku; sprawdź, czy smugi są czytelne.
- [ ] Taran — cięższy ruch i odporność są odczuwalne, bez utknięcia na przeszkodach.
- [ ] Ruch po przekątnej nie daje widocznej przewagi prędkości nad ruchem prostym.
- [ ] Po puszczeniu klawiszy postać nie ślizga się niekontrolowanie i nie pozostaje w ruchu dłużej, niż sugeruje wybrany styl.

## 3. Strzelanie

- [ ] Strzałki kierunkowe działają bez myszy.
- [ ] Mysz + LPM pozwala łatwo trafić w pojedynczego przeciwnika.
- [ ] Przetestuj walkę z bliska i z daleka: pociski nie znikają zbyt wcześnie i trafienia są czytelne.
- [ ] Przetestuj Rozrzut na bliskim dystansie oraz Salwę na średnim dystansie.
- [ ] Sprawdź, czy trafienie przeciwnika jest widoczne, a pociski przeciwników nie zlewają się z tłem.
- [ ] Sprawdź, czy ruch i celowanie jednocześnie nie powodują niechcianego przełączania stanów gry.

## 4. Mapa i orientacja

- [ ] Otwórz mapę piętra i sprawdź, czy korytarze zgadzają się z drzwiami widocznymi w pokojach.
- [ ] Odwiedź kilka pokojów, wróć do poprzedniego i potwierdź, że zawartość oraz połączenia nie zmieniły się.
- [ ] Po wejściu do pokoju ze sklepem sprawdź znacznik S i czytelność legendy.
- [ ] Po wykorzystaniu sklepu sprawdź, czy S znika.
- [ ] Na piętrze 2 lub kolejnym sprawdź znacznik B pokoju bossa.
- [ ] Sprawdź, czy aktualny pokój, pokoje oczyszczone, odwiedzone i nieodkryte dają się odróżnić bez długiego czytania legendy.
- [ ] Sprawdź, czy mapa pozostaje czytelna w zwykłym rozmiarze okna przeglądarki.

## 5. Dropy, sklep i przeszkody

- [ ] Moneta jest rozpoznawalna jako złoty żeton, a nie zwykły romb.
- [ ] Serce, przedmiot i oferta sklepu mają różne, łatwo rozpoznawalne symbole.
- [ ] Opis przedmiotu nie zasłania postaci ani ważnych pocisków podczas walki.
- [ ] Oferta sklepu jest czytelna, zakup działa przez podejście, a powrót nie odświeża ofert.
- [ ] Kamienie, doły, pola piasku/lodu i źródła ognia odróżniają się od dekoracji.
- [ ] Sprawdź, czy dekoracje nie wyglądają jak przedmioty do podniesienia lub aktywne zagrożenia.

## 6. Zapis wyniku

Dla każdej obserwacji zapisz:

- **Krok:** co dokładnie zrobiłeś.
- **Oczekiwane:** co powinno się wydarzyć.
- **Rzeczywiste:** co się wydarzyło.
- **Powtarzalność:** jednorazowo / 2–3 razy / za każdym razem.
- **Waga:** blokujące / irytujące / kosmetyczne.
- **Zrzut ekranu lub krótki klip:** jeśli pomaga odtworzyć problem.

### Wynik sesji

- Data i przeglądarka:
- Sprawdzone sekcje:
- Największy problem:
- Czy sterowanie było przewidywalne? (tak / częściowo / nie):
- Czy mapa pomagała się orientować? (tak / częściowo / nie):
- Czytelność pocisków i dropów (tak / częściowo / nie):
- Otwarte problemy:

## 7. Tymczasowa progresja 10-pokojowa

- [ ] Mapa pokazuje 10 pokojów w siatce 5×2.
- [ ] Pokój 10 jest ślepą odnogą prowadzącą wyłącznie z pokoju 9.
- [ ] Przed oczyszczeniem wszystkich dziewięciu zwykłych pokojów próba wejścia do bossa jest blokowana i wyjaśniona komunikatem.
- [ ] Po oczyszczeniu pokojów 1–9 można wejść do pokoju 10 i pojawia się boss.
- [ ] Samo wejście do pokoju 10 nie odblokowuje zejścia.
- [ ] Po pokonaniu bossa pojawia się jedno działające zejście; wejście w nie przenosi na kolejne piętro, ponownie do pokoju 1.
- [ ] Po powrocie do oczyszczonego pokoju bossa zejście nadal jest dostępne.


## 8. Hotline Miami — śmiertelna walka, osłona i szybki restart

- [ ] Gracz ginie od jednego rzeczywistego trafienia; sprawdź także krótki unik Skoczka/Zwinnego i jednorazowy amulet ratunkowy.
- [ ] Zwykły przeciwnik ginie od jednego trafienia każdą z siedmiu broni; boss pozostaje osobnym wyjątkiem wielotrafieniowym.
- [ ] Kamienie blokują ruch gracza, ruch wroga, pociski gracza, pociski wrogów i linię widzenia.
- [ ] Wróg próbuje obejść kamień, nie zapętla się na jego krawędzi i nie zostaje na zawsze w miejscu.
- [ ] Strzał przyciąga pobliskich wrogów do ostatniego miejsca hałasu; po utracie widoczności wróg nie strzela przez osłonę.
- [ ] Wróg nie zabija z nieczytelnej pozycji ani z drugiego końca pokoju bez ostrzeżenia.
- [ ] Wciśnięcie R w trakcie gry i po śmierci od razu zaczyna nową próbę, zachowuje wybraną broń/ruch i nie pokazuje ponownie ekranów wyboru.
- [ ] Pierwsze serce daje amulet ratunkowy, kolejne serca zamieniają się w monety; sklep sprzedaje amulet zamiast dodatkowego HP.
- [ ] Amulet ratunkowy nie może być kupowany/podnoszony w nieskończoność bez ograniczenia; jego zużycie jest czytelne.
- [ ] Wybór broni opisuje odstęp, prędkość i zachowanie pocisku; nie sugeruje, że DPS decyduje o zabiciu zwykłego wroga.
- [ ] Przejdź przez pokoje 1–9, odblokuj bossa w pokoju 10, pokonaj go i zejdź na następne piętro; stan pokojów i wyjścia musi przetrwać cofanie.
- [ ] Zapisz każde nieoczekiwane trafienie jako krok/oczekiwane/rzeczywiste/powtarzalność/waga. Nie uznawaj samej wysokiej trudności za dowód dobrej walki.

## Audyt CI i publikacji — 2026-10-22
- [ ] Przed wydaniem kolejnej wersji sprawdź ponowiony job Chromium dla `a497bc64f85bc1eb593a069eb0cdc08b52ebca75`.
- [ ] Przetestuj grę ręcznie na aktualnym Pages, nie tylko lokalny build; wpisz konkretną przeglądarkę i wyniki sekcji 8.
- [ ] W trakcie testu porównaj zachowanie wersji na Pages z SSOT, ponieważ historia Pages może być starsza niż main nawet po zielonym workflow.

## Nowa runda testów — omijanie osłon i czytelność strzałów (2026-10-22)
- [ ] W pokoju z kamieniem stań po przeciwnej stronie i oddaj strzał, aby wywołać hałas. Sprawdź, czy wróg obchodzi kamień zamiast napierać w niego lub drgać w miejscu.
- [ ] Powtórz z wrogiem dystansowym: sprawdź, czy omija kamień i nie strzela, dopóki linia widzenia nie jest czysta.
- [ ] Po wejściu w linię wzroku strzelca obserwuj ostrzegawczą linię. Sprawdź, czy widzisz ją przed pociskiem i możesz zareagować, a nie dopiero po wystrzale.
- [ ] Zasłoń linię kamieniem w trakcie starcia. Ostrzeżenie i strzał nie mogą przechodzić przez kamień; przy utracie widoczności windup powinien się anulować.
- [ ] Otwórz M: graf 5×2 powinien być wyśrodkowany, korytarze łączyć rzeczywiście połączone pokoje, a podpisy jasno rozróżniać START/BOSS/? oraz znaczniki sklepu/zejścia.
- [ ] Zapisz przeglądarkę, rozdzielczość, pokój, archetyp wroga i obserwację. Zgłoś osobno: „działa”, „nie działa”, „nie wiem”.


## Dodatkowy test — unik przed strzałem (2026-10-22)
- [ ] Stań w czystej linii widzenia strzelca i zaczekaj, aż pojawi się linia ostrzegawcza.
- [ ] Natychmiast przesuń się w bok. Sprawdź, czy linia pozostaje skierowana na poprzednią pozycję, a pocisk nie śledzi gracza po rozpoczęciu windup.
- [ ] Sprawdź, czy okno reakcji jest zauważalne i nie pozwala przeciwnikowi bezkarnie strzelać z bardzo bliska.
- [ ] W trakcie ostrzeżenia przesuń się za kamień. Windup powinien zostać anulowany, a pocisk nie może przejść przez kamień.
- [ ] Powtórz przeciw bossowi: trzy pociski wachlarza muszą zachować kierunek oparty na zapisanym celowaniu.
