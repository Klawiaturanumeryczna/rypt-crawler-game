# Progresja przeciwników — Crypt Crawler

## Zasady projektowe
- Każde kolejne piętro ma przeciętnie mniej przeciwników, ale przeciwnicy są mocniejsi.
- Nowe piętra wprowadzają nowe archetypy i stopniowo ograniczają obecność starych.
- Przeciwnicy z wcześniejszych pięter mogą wracać jako część składu mieszanego.
- Wrogowie nie wymagają konkretnego przedmiotu ani konkretnego typu broni do pokonania.
- Parametry balansu poniżej są prototypowe. Docelowe HP, szybkość, częstotliwość ataków i liczebność ustalimy po testach.

## Aktualna implementacja prototypu
Liczba wrogów w pokoju jest losowana od 1 do limitu piętra:
- Piętro 1: maks. 20.
- Piętro 2: maks. 16.
- Piętro 3: maks. 12.
- Piętro 4: maks. 8.
- Piętro 5 i kolejne: maks. 6.

To limity, nie gwarantowana liczba. Wyniki poszczególnych pokoi mogą się nakładać; średnia liczba wrogów maleje wraz z piętrem.

### Skład wrogów według piętra
Podane wartości to względne wagi losowania, nie gwarantowane procenty po zaokrągleniu:
- Piętro 1: Chaser 76, Spitter 24.
- Piętro 2: Chaser 42, Spitter 23, Brute 35.
- Piętro 3: Chaser 12, Spitter 13, Brute 40, Dasher 35.
- Piętro 4+: Brute 25, Dasher 40, Hexer 35.

Od piętra 4 z puli znikają podstawowi Chaser i Spitter. Na późniejszych piętrach obecny prototyp korzysta z puli piętra 4, a wzrost statystyk nadal postępuje. Nowe archetypy można dodawać w jednym miejscu w konfiguracji `PROGRESJA_WROGOW`.

## Archetypy
- **Chaser (tier 1):** podstawowy wróg, podąża bezpośrednio za graczem.
- **Spitter (tier 1):** utrzymuje dystans i strzela pociskami.
- **Brute (tier 2):** większy i wytrzymalszy wróg, który naciera na gracza.
- **Dasher (tier 3):** wykonuje krótkie, szybkie szarże, więc gracz musi obserwować jego ruch.
- **Hexer (tier 4):** wróg dystansowy z szybszym pociskiem niż Spitter.

## Tymczasowe skalowanie
- HP rośnie obecnie o 14% na każde piętro powyżej pierwszego, zaokrąglane do najbliższej liczby całkowitej.
- Szybkość rośnie o 3,5% na piętro, z limitem 30% premii.
- To wartości startowe do testów, nie ostateczny balans. Później trzeba przetestować tempo walki, czytelność ataków oraz czas czyszczenia pokoju.

## Do dopracowania
1. Przetestować, czy liczebność i skalowanie nie robią późniejszych pięter zbyt łatwymi albo frustrującymi.
2. Dodać nowe archetypy dopiero po ustaleniu ich wyraźnej, czytelnej roli.
3. Zdecydować, czy od piętra 5 wprowadzać kolejne typy, warianty elitarnych wrogów, czy nowe zachowania istniejących typów.
4. Utrzymać czytelność ataków i zapewnić, że każdy przeciwnik jest możliwy do pokonania podstawowym zestawem gracza.
