# Crypt Crawler — notatki balansu

Stan po wdrożeniu mechanik z 2026-10-18. To wartości startowe do testów, nie wynik testów z udziałem graczy.

## Długość piętra i boss

- Limit piętra 1: 20 pokoi. Każde kolejne piętro dodaje 2 pokoje: 22, 24, 26…
- Boss pojawia się w ostatnim pokoju aktualnego piętra.
- HP bossa: `45 + 12 × numer piętra` (57 HP na piętrze 1, 69 na piętrze 2, 81 na piętrze 3).
- Boss strzela wachlarzem trzech pocisków; odstęp ataków wynosi 55–75 klatek.
- Szansa pojawienia się przejścia w zwykłym pokoju wynosi `(numer pokoju / limit pokoi)^30`. Krzywa jest celowo nieliniowa: liniowe 5%, 10%, 15%… powodowało, że niezależne losowania niemal zawsze kończyły piętro przed bossem.
- Na piętrze 1 szansa wynosi ok. 0,02% w pokoju 15, 0,8% w pokoju 17, 4,2% w pokoju 18, 21,5% w pokoju 19 i 100% w pokoju 20. Szansa rośnie wyraźniej pod koniec, żeby boss nie był pomijany w większości runów.
- Przy tej krzywej szacunkowo ok. 74,5% runów piętra 1 dociera do bossa bez wcześniejszego przejścia. To nadal oznacza, że wcześniejsze wyjście może ominąć bossa; jeśli boss ma być obowiązkowy, trzeba usunąć wcześniejsze wyjścia albo zmienić ich znaczenie.
- Po pokonaniu bossa wszystkie drzwi prowadzą dalej, więc na ostatnim pokoju nie ma pechowego losowania.

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
- Sklep ma 8% szansy pojawienia się jako specjalne wejście w kwalifikującym się pokoju; po wejściu do sklepu nie pojawia się ponownie na tym samym piętrze.
- W sklepie zawsze jest serce za 2 monety. Zakup leczy 2 HP; przy pełnym zdrowiu lub braku monet przycisk zakupu jest nieaktywny.
- Ocena wstępna: 0,5% na monetę było zbyt niskie, by sensownie finansować zakupy. 8% powinno dać walutę na przestrzeni dłuższego piętra, a premia za serię nagradza agresywną grę. Trzeba obserwować, czy łączna liczba monet nie robi leczenia zbyt łatwym.

## Przedmioty

- Na pierwszym pokoju każdego piętra pojawiają się trzy losowe oferty: jeden aktywny przedmiot, jeden przedmiot nóg i jeden strzelecki, zamiast wszystkich 30 naraz.
- Podejście na odległość 100 jednostek pokazuje nazwę, efekt i instrukcję `E — PODNIEŚ`. Przedmiot nie podnosi się automatycznie.
- Przedmioty nóg i strzeleckie modyfikują statystyki przy podniesieniu i wypisują zmianę. Aktywne przedmioty są zużywane po użyciu Spacji.
- Część efektów aktywnych zadaje obrażenia, ale celowo nie dobija wrogów, aby nie omijać istniejącej ścieżki liczenia zabójstw i dropów.
- To nadal prototyp: przedmioty aktywne 3, 7 i 10 nie zabijają przeciwników bezpośrednio. W dalszej iteracji należy podłączyć ich obrażenia do wspólnej funkcji śmierci wroga, jeśli mają móc dobijać.

## Co testować w pierwszej kolejności

1. Czy gracz ma zwykle 2 monety na leczenie przed końcem piętra, ale nie kupuje serca po każdym pokoju.
2. Czy boss pierwszego piętra jest wymagający, lecz możliwy do pokonania bez konkretnego przedmiotu.
3. Czy 20 pokoi na pierwszym piętrze nie jest zbyt długie; jeśli tak, lepiej zmienić liczbę pokoi niż podbijać szybkość wrogów.
4. Czy trudne drzwi rzeczywiście czują się trudniejsze, a dodatkowy łup rekompensuje ryzyko.
5. Czy tooltip przedmiotu jest czytelny na różnych rozdzielczościach i nie zasłania istotnych pocisków.
6. Czy wcześniejsze pojawienie się przejścia nie sprawia, że boss jest zbyt często pomijany. Jeśli boss ma być obowiązkowy, przejście powinno pojawiać się dopiero po jego pokonaniu.
