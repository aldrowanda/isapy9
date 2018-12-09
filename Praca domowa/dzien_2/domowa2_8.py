# 8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
liczba_podana = input('Podaj liczbe: ')
liczba = int(liczba_podana)  # czy to jest nowa zmienna??
if liczba % 3 == 0 or liczba % 5 == 0 or liczba % 7 == 0:
    print('liczba jest podzielna przez 3 lub 5 lub 7.')
else:
    print('liczba nie jest podzielna przez 3 lub 5 lub 7')

# 9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
liczba_podana = input('Podaj liczbe: ')
liczba = int(liczba_podana)  # czy to jest nowa zmienna??
if liczba % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0:
    print('liczba jest podzielna przez 3 i 5 i 7.')
else:
    print('liczba nie jest podzielna przez 3 i 5 i 7')
