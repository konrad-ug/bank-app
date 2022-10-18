# bank-app

Jesteś programistą odpowiedzialnym/programistką odpowiedzialną za stworzenie corowej funckjonalności aplikacji bankowej.
Pierwszym zadaniem jest stworzenie funkcjonalości zakładania konta bankowego. W celu zoptymalizowania procesu developmentu wybierasz metodologie TDD.

Zaimplementuj ponisze funcjonalości uywając TDD. 
Feature 1:
System powinien umoliwiać stworzenie osoistego konta bankowego.
Konto powinno posiadać następujące parametry:
- imię i nazwisko właściciela (podawane w trakcie tworzenia konta, dane obowiązkowe)
- saldo (początkowe saldo dla wszystki kont wynosi 0)
- unikatowe ID

Feature 2:
Okazalo się imię i nazwisko nie są unikatowymi wartociami pozwalającymi zidentyfikować właściciela konta.
Musimy dodać jeszcze jedną zmienną wejściową niezbędą do tworzenia konta - numer PESEL.

Feature 3:
Nasi uytkownicy podawali niepełne numery PESEL. 
Musimy dodać warunek który nie pozwoli na stworzenie konta jezeli  podany PESEL jest krótszy niz 11 znaków.

Feature 4:
By zwiększyć sprzedaz zakładanych kont zespół sprzedazy rozpoczął akcje promocyjną.
Jezeli przy zakladaniu konta uzytkownik poda kod rabatowy w postaci PROM_XYZ (gdzie XYZ to dowlne losowe liczby) do nowo utworzonego konta dodajemy 50zł. 