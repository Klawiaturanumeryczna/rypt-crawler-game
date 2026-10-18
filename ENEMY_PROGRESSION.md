# Progresja przeciwników — Crypt Crawler

## Zasady projektowe
- Piętra mają stałą długość 20 pokoi.
- Kolejne piętra zwiększają wytrzymałość i szybkość wrogów oraz zmieniają pulę archetypów.
- Przeciwnicy nie powinni wymagać konkretnego przedmiotu do pokonania.
- Wartości poniżej są prototypowe i wymagają testów rozgrywki.

## Liczba wrogów w pokoju

Limit bazowej liczby wrogów wynosi:

`min(8, 2 + numer piętra + floor(numer pokoju / 5))`

Gra losuje od 1 do tego limitu, a następnie stosuje mnożnik wybranych drzwi i zaokrągla wynik. Pokój sklepu i pokój bossa nie tworzą zwykłej grupy wrogów. Mnożnik trudnych drzwi nie może przekroczyć limitu pokoju.

## Skład puli wrogów według piętra

Podane wartości to względne wagi losowania, a nie gwarantowane procenty:
- Piętro 1: Chaser 76, Spitter 24.
- Piętro 2: Chaser 42, Spitter 23, Brute 35.
- Piętro 3: Chaser 12, Spitter 13, Brute 40, Dasher 35.
- Piętro 4 i kolejne: Brute 25, Dasher 40, Hexer 35.

Na trudnych drzwiach dodatkowo zwiększane są wagi cięższych archetypów: Brute +42, Dasher +18, a od piętra 2 Hexer +12. Wagi są następnie normalizowane przez losowanie.

## Archetypy

- **Chaser:** podstawowy przeciwnik, podąża bezpośrednio za graczem.
- **Spitter:** przeciwnik dystansowy, utrzymuje dystans i strzela pociskami.
- **Brute:** większy i wytrzymalszy przeciwnik, który naciera na gracza.
- **Dasher:** wykonuje krótkie, szybkie szarże.
- **Hexer:** przeciwnik dystansowy z szybszym pociskiem niż Spitter.
- **Boss piętra:** pojawia się w pokoju 20; ma `45 + 12 × numer piętra` HP i strzela wachlarzem trzech pocisków co 55–75 klatek.

## Skalowanie statystyk

- HP zwykłych wrogów rośnie o 14% na każde piętro powyżej pierwszego, z zaokrągleniem do najbliższej liczby całkowitej.
- Szybkość rośnie o 3,5% na piętro, maksymalnie o 30% premii, a potem stosowany jest mnożnik trudności drzwi.
- Łatwe drzwi mnożą szybkość przez 0,92; średnie przez 1,00; trudne przez 1,08.
- Poziom trudności resetuje się przy wejściu do każdego pokoju, więc modyfikatory nie kumulują się przez kolejne drzwi.

## Do dopracowania

1. Przetestować, czy liczebność i skalowanie nie robią późniejszych pięter zbyt łatwymi albo frustrującymi.
2. Dodać nowe archetypy dopiero po ustaleniu ich wyraźnej i czytelnej roli.
3. Zdecydować, czy od piętra 5 wprowadzać elitarne warianty, czy nowe zachowania istniejących typów.
4. Utrzymać czytelność ataków i zapewnić, że każdy przeciwnik jest możliwy do pokonania podstawowym zestawem gracza.
