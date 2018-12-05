# slownik= {"imie": ["lukasz", "ala", "ola"], "nazwiska":['kowalski',"iksinski", "malinowska"]}
#
# print(type(slownik))
# print(slownik)
# #
# # for klucz, wartosc in slownik.items():
# #     print(klucz)
# #     print(wartosc)


# for klucz, wartosc in slownik.items():
#     print(klucz)
#     # print(wartosc)
#     for dana in  enumerate(wartosc):
#         print("\t -> " +dana)
#
# print('*' *50)
#
# nazwiska= slownik["nazwiska"]
# for dana in nazwiska:

'''To jest "baza danych" '''


slownik= {
    "imiona": [
        "lukasz", "ala", "ola",
    ],
    "nazwiska":[
        'kowalski',"iksinski", "malinowska", "ygrek"
    ]
}
miasta ={ "miasta":["Warszawa", "Gdańsk", "Sopot", "Kraków"]}
slownik.update(miasta)

# print(type(slownik))
# print(slownik)
# dict.update()
#

# PROGRAM WYPISUJE Mam na imie XXXX nazwisko YYYY i mieszkam w ZZZZ
for index, imie in  enumerate(slownik["imiona"]):
    nazwisko= slownik["nazwiska"] [index]
    miasto= slownik["miasta"][index]
    print("Mam na imie:{} nazwisko {} i mieszkam w {}".format(imie, nazwisko, miasto))

