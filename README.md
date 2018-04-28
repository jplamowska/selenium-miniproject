## Automatyzacja przypadku testowego przy pomocy Selenium Webdriver

### Przypadek testowy
##### ID: 001
##### Tytuł: Rejestracja wniosku o konto bankowe przez nowego użytkownika używając nieprawidłowej wielkości pliku jpg
##### Środowisko: Chrome wersja 56.0.2897.0, CentOS Linux release 7.2.1511
##### Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie  jest zalogowany.

### Kroki:
1. Wejdź na stronę ”https://www.eurobank.pl/”
2. Kliknij ”otwórz konto”
3. Wybierz jako formę zawarcia umowy ”on-line przelew z innego banku”
4. Kliknij ”przejdź dalej”
5. Wybierz konto ”na co dzień”
6. Wybierz jako formę odbioru wyciągów miesięcznych ”odbiór osobisty w placówce”
7. Upewnij się, że operacje w Bankowości Internetowej będą potwierdzane ”hasłami SMS”
8. Zaznacz jako kartę do konta ”Visa Electron”
9. Zaakceptuj korzystanie z aplikacji mobilnej eurobanku na swoim telefonie i zaznacz ”TAK”
10. Kliknij ”dalej”
11. Wpisz imię
12. Wpisz nazwisko
13. Wpisz PESEL
14. Wpisz imię matki
15. Wpisz imię ojca
16. Wpisz nazwisko rodowe matki
17. Wpisz miejsce urodzenia
18. Wybierz kraj urodzenia
19. Sprawdź czy pole obywatelstwo jest uzupełnione
20. Sprawdź czy kraj zamieszkania jest uzupełniony
21. Wybierz źródło dochodów
22. Odpowiedz, ze jesteś rezydentem podatkowym w Polsce i wybierz „TAK”
23. Odpowiedz, ze nie jesteś  rezydentem podatkowym w innym kraju niż Polska i wybierz „NIE”
24. Odpowiedz, że nie jesteś obywatelem USA i wybierz ”NIE”
25. Wprowadź  numer  telefonu komórkowego
26. Wprowadź  adres e-mail
27. Wpisz nazwę ulicy
28. Wprowadź numer budynku
29. Wprowadź numer mieszkania
30. Wprowadź kod pocztowy
31. Wpisz miasto
32. Wybierz województwo
33. Sprawdź czy zaznaczona jest opcja adres korespondencyjny ”Taki sam jak adres zamieszkania”
34. Zaakceptuj  otrzymywanie informacji handlowej za pomocą środków komunikacji elektronicznej
35. Kliknij ”dalej”
36. Wybierz jako rodzaj głównego dokumentu tożsamości  ”Dowód osobisty”
37. Wprowadź serię i numer głównego dokumentu tożsamości
38. Wybierz datę ważności głównego dokumentu tożsamości
39. Załącz zdjęcie strony dokumentu ze zdjęciem
40. Załącz zdjęcie strony dokumentu bez zdjęcia
41. Kliknij ”dalej”

### Uruchomienie
```
$ python miniprojekt_justynaplamowska.py
test_invalid_email (__main__.EurobankRegistration) ...
Plik jest zbyt duży.
Plik jest zbyt duży.
ok

----------------------------------------------------------------------
Ran 1 test in 37.968s

OK
```

### Oczekiwany rezultat:
Rejestracja nie powodzi się
Użytkownik dostaje informację, że plik jest zbyt duży.

### Uwagi końcowe
Automatyzacja przypadku testowego (test funkcjonalny) powiodła się. Test może być wrażliwy na zmianę struktury strony z powodu konieczności stosowania długich ścieżek w lokalizatorach XPATH i CSS Selector.
