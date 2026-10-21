# PROMPT STARTOWY — Crypt Crawler (wklej do nowego czatu)

Jesteś kontynuacją pracy nad projektem **Crypt Crawler**. Najpierw przeczytaj plik `NEXT_CHAT_HANDOFF.md` w repozytorium głównym, a następnie `PROJECT_STATUS.md`, `DECISION_LOG.md`, `BALANCE_NOTES.md`, `verify.py` i `tests/browser_smoke.py`. Repo: https://github.com/Klawiaturanumeryczna/crypt-crawler. Publiczny mirror: https://github.com/Klawiaturanumeryczna/rypt-crawler-game. Aktualna gra: https://klawiaturanumeryczna.github.io/rypt-crawler-game/

**Tryb pracy:** gdy napiszę „OK, rob”, autonomicznie audytuj repo, wybierz największy sensowny problem, implementuj, testuj, weryfikuj, dokumentuj, otwieraj PR i przechodź do następnego zadania bez pytania „co dalej?”. Nie scalaj, jeśli CI jest czerwone. Nie udawaj ręcznego playtestu. Prywatne repo jest SSOT; po merge synchronizuj mirror i sprawdzaj zgodność plików oraz deployment. Prowadź dokumentację po polsku, aktualizuj pliki z decyzjami/stanem/balansem i aktualizuj `NEXT_CHAT_HANDOFF.md` przy istotnych zmianach, żeby następna sesja też miała wiedzę.

**Aktywne zlecenie użytkownika:**
- Mikro-rewolucja grafiki: zrobić z gry wizualnie pełnoprawniejszy top-down RPG; gatunkowe inspiracje Margonem/RPG Maker tylko jako kierunek dla map, potworów i itemów, bez kopiowania chronionych assetów/postaci.
- Własne magiczne stworki/easter eggi: wampiry, wilkołaki, wiedźmy, mumie, ogr, smok, krasnolud, krowa i inne oryginalne potwory.
- Mapa/generowanie poziomów nadal jest słabe i źle pokazane: zbadaj generator, rzeczywistą topologię, drzwi, połączenia i czytelność pełnej mapy.
- `M` = mapa piętra; zmiana stylu ruchu ma osobny wolny klawisz (dokumentacja wskazuje `Q`, sprawdź kod); `B` = broń; `WASD` = ruch; strzałki = kierunkowe strzelanie; LPM = strzelanie do kursora. Nie przywracaj Shift jako uniku.
- Ruch i strzelanie nadal są kiepskie, a broń za trudna w użyciu. Mocno zwiększ mocne strony i kompromisy obu systemów, popraw responsywność ruchu, celowanie, hitboxy, czas życia/prędkość pocisków i czytelność trafień. Używaj testów TTK i obrażeń na różnych dystansach oraz wobec grup/linii wrogów. Zmiany parametrów są prototypem do playtestu, nie deklaruj ich przyjemności bez testu ręcznego.
- Itemy, dropy, potwory i kafelki mają być rozpoznawalne i czytelne, nie tylko kolorowe plamy.
- Zachowaj 30 pokojów na piętro i obecne fundamentalne zasady, chyba że użytkownik zatwierdzi zmianę.

Najpierw sprawdź bieżący stan repo — nie zakładaj, że handoff opisuje każdy najnowszy commit. Następnie działaj. Zrób pierwszy audyt mapy/generowania i sterowania, zaproponuj/zaimplementuj spójny zestaw napraw, dodaj testy, zaktualizuj dokumentację, otwórz PR. Po każdym ważnym pakiecie dopisz stan do `NEXT_CHAT_HANDOFF.md`, a w odpowiedzi końcowej daj link do gry, PR, wyniki CI i jasno nazwij ograniczenia.
