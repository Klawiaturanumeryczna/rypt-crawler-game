# Crypt Crawler — notatki balansu

Stan po wdrożeniu mechanik z 2026-10-18. To wartości startowe do testów, nie wynik testów z udziałem graczy.

## Długość piętra i boss

- Każde piętro ma dokładnie 20 pokoi. Długość nie rośnie wraz z numerem piętra.
- Boss pojawia się w ostatnim pokoju aktualnego piętra.
- HP bossa: `45 + 12 × numer piętra` (57 HP na piętrze 1, 69 na piętrze 2, 81 na piętrze 3).
- Boss strzela wachlarzem trzech pocisków; odstęp ataków wynosi 55–75 klatek.
- Na początku piętra losowany jest jeden próg przejścia. Po oczyszczeniu pokoju porównujemy go z `numer pokoju × 5 punktów procentowych`: pokój 1 — 5%, pokój 2 — 10%, …, pokój 19 — 95%. To szansa skumulowana, a nie nowe niezależne losowanie w każdym pokoju; dzięki temu około 5% podejść dociera do bossa w pokoju 20.
- W pokoju 20 przejście jest gwarantowane; po pokonaniu bossa wszystkie drzwi prowadzą dalej.

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
- W pokoju 1 pojawiają się 3 serca do zebrania i 2 monety. Serca nie znikają przy pełnym zdrowiu; można je zebrać po otrzymaniu obrażeń.
- W sklepie zawsze jest serce za 2 monety. Zakup leczy 2 HP; przy pełnym zdrowiu lub braku monet przycisk zakupu jest nieaktywny.
- Ocena wstępna: 0,5% na monetę było zbyt niskie, by sensownie finansować zakupy. 8% powinno dać walutę na przestrzeni dłuższego piętra, a premia za serię nagradza agresywną grę. Trzeba obserwować, czy łączna liczba monet nie robi leczenia zbyt łatwym.

## Przedmioty

- W pierwszym pokoju każdego piętra pojawia się 6 przedmiotów ruchu oraz po 2 losowe przedmioty aktywne, na nogi i do strzelania (łącznie 12 ofert). W obrębie każdej kategorii wybrane są dwa różne przedmioty. Nie ma systemu synergii.
- Podejście na odległość 100 jednostek pokazuje nazwę, efekt i instrukcję `E — PODNIEŚ`. Przedmiot nie podnosi się automatycznie.
- Przedmioty nóg i strzeleckie modyfikują statystyki przy podniesieniu i wypisują zmianę. Aktywne przedmioty są zużywane po użyciu Spacji.
- Część efektów aktywnych zadaje obrażenia, ale celowo nie dobija wrogów, aby nie omijać istniejącej ścieżki liczenia zabójstw i dropów.
- To nadal prototyp: przedmioty aktywne 3, 7 i 10 nie zabijają przeciwników bezpośrednio. W dalszej iteracji należy podłączyć ich obrażenia do wspólnej funkcji śmierci wroga, jeśli mają móc dobijać.

## Co testować w pierwszej kolejności

1. Czy gracz ma zwykle 2 monety na leczenie przed końcem piętra, ale nie kupuje serca po każdym pokoju.
2. Czy boss pierwszego piętra jest wymagający, lecz możliwy do pokonania bez konkretnego przedmiotu.
3. Czy stałe 20 pokoi na piętro nie jest zbyt długie; jeśli tak, rozważyć zmianę wspólnego limitu dla wszystkich pięter.
4. Czy trudne drzwi rzeczywiście czują się trudniejsze, a dodatkowy łup rekompensuje ryzyko.
5. Czy tooltip przedmiotu jest czytelny na różnych rozdzielczościach i nie zasłania istotnych pocisków.
6. Czy wcześniejsze pojawienie się przejścia nie sprawia, że boss jest zbyt często pomijany. Jeśli boss ma być obowiązkowy, przejście powinno pojawiać się dopiero po jego pokonaniu.
