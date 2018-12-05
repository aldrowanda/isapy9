'''zmienna_globalna='A'
def rodzic():
    #zmienna_lokalna='B'                 # lepiej globala nie używać zmiana zmiennej w funkcji może popsuć kod bo komuś
                                           #podmienimy zmienną lub sobie lepiej jest używać zmiennej wyjściowej z funkcj
                                           # i zmienić naszą zmienną
    global zmienna_globalna
    zmienna_globalna= 'A zmienione'
    print("Funkcja rodzic: " + zmienna_globalna)

print(zmienna_globalna)  # nomalna zmienna

rodzic()  # wywowałanie funkcji
print(zmienna_globalna) # funkcja zmienia zmienną globalną wiec wynik będzie
                        # A
                        # Funkcja rodzic: A zmienione
                        # A zmienione'''

'''from moduly import przywitanie

przywitanie.czesc("pawel")

# poczytaj co to jest main!!!!!!  '''

'''with open('adresy.csv','r+', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
    writer = csv.writer(csvfile)
    writer.writerow(['Jan', 'Kowalski', 'Sopot', '123-432-111'])'''

'''PRACA NA ćWiczeniach 
1. otwórz plik z danymi
2. przeiteruj każdy znak danych wejściowych
3. porównaj każdy znac do naszego znaku
4. zwiększ licznik dla danego znaku
5. zapisz licznik do pickle

'''

import string
from dzien4 import policz_literke

def otwórz_plik(plik):
    with open(plik) as dane:
        return dane.read()

znaki= string.ascii_letters
dane=otworz_plik('dane.txt')
for znak in znaki:
    ilosc=policz_literke(znak,dane)
    print(ilosc)