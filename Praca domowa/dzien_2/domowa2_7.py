#10. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
liczba_podana=input('Podaj rok: ')
liczba=int(liczba_podana) # czy to jest nowa zmienna??
if (liczba%100!=0 and liczba%4==0):
    print('Rok przestępny.')
elif (liczba%100==0 and liczba%400==0):
    print('Rok przestępny.')
else:
    print('Rok nieprzestępny')