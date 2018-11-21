imie= input(' Dzień dobry,\nJak masz na imię? ')
imie=imie.strip(' ')
print('Dzień dobry '+imie.capitalize()+'\n:)')  #pierwsza liczba się zawiera a ostatnia nie
ilosc_liter=len(imie)
ostatnia_litera=imie[ilosc_liter-1]
print('Twoje imie ma ' + str(ostatnia_litera) + ' liter')
print( 'Ostatnia litera Twojego imienia to  ' + str(ostatnia_litera))
print('ostatnia litera to ' +str(imie[-1:]))  # ostatnią litere można zrobić tez tak"""
