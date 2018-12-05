

imie= input(' Dzień dobry,\nJak masz na imię? ')
imie=imie.strip(' ')   #strip usuwa wybrane znaki w tym przypadku spacja
print('Dzień dobry '+imie.capitalize()+'\n:)')  #pierwsza liczba się zawiera a ostatnia nie
ilosc_liter=len(imie)
ostatnia_litera=imie[ilosc_liter-1]  #liczy od zera !!!!!!!!!!!!!!!!!!!!!

if (str(ostatnia_litera) == str('a')):
    print('jestes kobietą')
else:
    print(' jestes facetem')fdsf