######wypisywanie zdania w kolumnie na wszystkie sposoby

'''liczby=range(0,50)
for liczba in liczby: #można for range(0,50)
    if (liczna % 2!=0):
        continue
    print('koniec')


tekst="ala ma kota"
for litera in tekst:
    print (litera)'''

'''lista_imion = ['ola', 'Ala', 'tomek', 'jan']
for i, imie in  enumerate(lista_imion):
    print("Na pozycji: {} jest imie {}".format(i, imie))'''

'''kolekcja_a= ['ola', 'Ala', 'tomek', 'jan']
kolecja_b= ['kowal', 'nowak,', 'igrek']
for element_a, element_b in zip(kolekcja_a, kolecja_b):
    print (element_a,element_b)'''

'''zmienna referecyjna oznacza że zmienna i jej kopia np zmienna2=zmianna jeśli któras z nich jest zmieniona to zmieniamy wszystkie 
jeśli zmienna nie jest referyncyjna to jest zapamiętywana i zapycha RAM'''
'''copy kopuje tablice a jej zmienne w tablice są refercjami a deep copy to wszysko jest niereferencyjne '''

'''lista = ['aaa', 'bbb', 'ccc', 'dddd']
przypisanie= lista
lista[0]='XXX'
print(lista)
print(przypisanie)'''

'''import copy
lista = ['aaa', 'bbb', 'ccc', 'dddd']
przypisanie= lista

kopia_zindeksami= lista[:]
kopia_konstruktorem= list(lista)
kopia_metoda= lista.copy()
kopia_biblioteka= copy.copy(lista)

# lista[0]='XXX'
# print(lista)
# print(przypisanie)
# print(kopia_biblioteka)
# print(kopia_konstruktorem)
# print(kopia_metoda)
# print(kopia_zindeksami)

kopia_biblioteka[0]='YYYY'
print(kopia_biblioteka)

# typ refencyjny odwołuje sie do adresu w pamięci a nie do samych danych!!!!!!!!!!!!!!!!!!!!!!!!!!!!1'''

def policz_literke( tekst,litera="a"):
    if (tekst[0:]==str(litera)):
        x += 1
        return x

policz_literke('ala ma kota')