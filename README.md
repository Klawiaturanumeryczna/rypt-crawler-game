# Crypt Crawler — prototyp 0.4.0

Przeglądarkowy prototyp roguelike'a z widokiem z góry. Gra działa z jednego pliku `index.html` i nie wymaga silnika, instalacji pakietów ani zewnętrznych grafik.

## Uruchomienie

Otwórz `index.html` w nowoczesnej przeglądarce i kliknij **ROZPOCZNIJ RUN**.

## Sterowanie

- **WASD** — poruszanie się.
- **Strzałki** — strzelanie w 8 kierunkach; można łączyć klawisze.
- **Mysz + przytrzymany LPM** — strzelanie w stronę kursora.
- **P** — pauza / powrót.
- **R** — rozpoczęcie nowego runu.
- **M** — ponowny wybór stylu ruchu.
- **Shift** — sus stylu „Skoczek”.
- **Spacja** — użycie wybranego przedmiotu aktywnego; w tym prototypie jego efekt nadal jest placeholderem.

## Aktualnie zaimplementowane systemy

### Walka i przeciwnicy

- Walka czasu rzeczywistego, pociski gracza i wrogów, obrażenia, krótkie okno niewrażliwości po trafieniu, cząsteczki i potrząsanie ekranem.
- Pięć archetypów przeciwników: Chaser, Spitter, Brute, Dasher i Hexer.
- Skład puli wrogów i ich statystyki skalują się z piętrem. Szczegóły są w [ENEMY_PROGRESSION.md](ENEMY_PROGRESSION.md).
- Pokój zostaje oczyszczony, kiedy wszyscy wrogowie zostaną pokonani.

### Drzwi i trudność

Każdy pokój ma cztery drzwi standardowe: **szare — łatwe**, **złote — średnie**, **czerwone — trudne**. Każde losowanie zaczyna się od równej szansy na trzy poziomy. Jeśli wszystkie cztery drzwi wylosują ten sam poziom, jedno z nich jest losowane ponownie, więc maksymalnie trzy drzwi mogą mieć ten sam kolor.

Po wejściu przez drzwi wybrany poziom wpływa na następny pokój:

| Poziom | Liczba wrogów | Szybkość wrogów | Mnożnik szansy na łup |
|---|---:|---:|---:|
| Szary — łatwy | ×0,75 | ×0,92 | ×0,75 |
| Złoty — średni | ×1,00 | ×1,00 | ×1,00 |
| Czerwony — trudny | ×1,25, z limitem piętra | ×1,08 | ×1,50 |

To mnożniki prototypowe, nie ostateczny balans. Moneta i serce mają obecnie bazową szansę 0,5% na zabitego wroga przed zastosowaniem mnożnika trudności. Wyższe zagrożenie zwiększa szansę na łup, ale nie gwarantuje konkretnej nagrody.

Po oczyszczeniu pokoju pojawia się możliwość przejścia na kolejne piętro z szansą zależną od numeru pokoju (numer pokoju ÷ 10). Oznaczone przejście ma napis **PIĘTRO +1**. Przejście na piętro leczy maksymalnie 2 punkty zdrowia i otwiera wybór stylu ruchu.

### Style ruchu

Na początku runu i każdego piętra można wybrać jeden z sześciu stylów: Podstawowe bieganie, Szybki ślizg, Skoczek, Rozpęd, Zwinny i Ciężki krok. Klawisz **M** pozwala zmienić styl podczas gry. Komunikat podaje poprzedni i nowy styl oraz zmianę prędkości bazowej.

### Seria zabójstw i komunikaty

- Zabójstwo zwiększa licznik serii. Kolejne zabójstwo musi nastąpić w ciągu 3 sekund, aby seria była kontynuowana.
- Każde 5 kolejnych zabójstw w serii daje **+1 monetę**.
- HUD pokazuje liczbę punktów zdrowia, w tym połówki serc, a także poziom zagrożenia i serię zabójstw.
- Dziennik rozgrywki przechowuje pięć ostatnich komunikatów. Zmiany zdrowia, monet, zabójstw, serii i ruchu podają wartości przed i po zmianie, gdy dana wartość ulega zmianie.

## Ograniczenia, o których trzeba pamiętać

- **30 przedmiotów na ziemi to obecnie placeholdery.** Podniesienie zwiększa licznik posiadanych przedmiotów, ale ich efekty nie są jeszcze zaprogramowane. Spacja również nie aktywuje jeszcze realnej mocy przedmiotu.
- Kolory fioletowy i tęczowy są zarezerwowane pod przyszłe mechaniki specjalne; nie stanowią dodatkowych zwykłych poziomów trudności.
- Nie ma jeszcze bossa końcowego, trwałego odblokowywania zawartości, zapisu postępu między runami, proceduralnego grafu pomieszczeń ani pełnego systemu synergii przedmiotów.
- Parametry trudności i szans dropów wymagają testów rozgrywki i dalszego balansu.

## Weryfikacja

Po ostatnich zmianach sprawdzono składnię JavaScript oraz identyczność plików `index.html` w obu repozytoriach. Losowanie składu czterech drzwi przetestowano w 100 000 symulowanych próbach, a granice skalowania liczby przeciwników zweryfikowano statycznie. **Nie wykonano jeszcze interaktywnego testu w przeglądarce**, więc powyższe kontrole nie zastępują testów podczas gry.
