# import sys
# import os
# import send2trash
#
# send2trash.send2trash('skasowac.txt')
#
# print(sys.path)
# print(os.getcwd())

'''Program do prowadzenia pamiętnika'''


import pickle

def otworz_dziennik(plik_dz):
    dziennik= open(plik_dziennika, "rb+")
    return dziennik

def zamknij_dziennik(plik_dz):
    plik_dz.close()

def dodaj_wpis(plik_dz ): # lista ze słownikami
    data= input('podaj datę')
    tresc=input('podaj tresc')
    nowy_wpis= {"data": data, "tresc": tresc}
    stare_wpisy= przeczytaj_plik(plik_dz)
    lista=[]
    lista.append(stare_wpisy)
    lista.append(nowy_wpis)
    pickle.dump(wpis,plik_dz)

def wyswietl_menu():
    print("Moj dziennik v0.1 alpha"                         # uzupełnij menu
          "tutaj bedzie moje menu "
          "1.Przegladaj\n"
          "2.dodawanie\n"
          "3.usuwanie\n"
          "4.szukanie\n"
          "5.wyjscie\n")

def przeczytaj_plik(plik_dz):
    try:
        dane= pickle.load(plik_dz)
        print(dane)
        return dane
    except:
        print("błąd")

def zapytaj():
    decyzja = input("Co wybierasz")
    if decyzja=="1":
        print ("Oto Twoje wpisy")
        plik_dz = otworz_dziennik(plik_dziennika)
        przeczytaj_plik(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja=="2":
        print ("dodawanie wpisu")
        plik_dz = otworz_dziennik(plik_dziennika)
        dodaj_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    elif decyzja=="5":
        exit()


plik_dziennika="dziennik.dz"
wyswietl_menu()
zapytaj()
# while True:
#     pass

