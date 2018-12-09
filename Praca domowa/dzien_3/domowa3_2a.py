# 2) Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety:
#  5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.
# rozwiązanie łopatologiczne

kwota_str = input('podaj swoją kwotę rozmienienia: ')

kwota = float(kwota_str)
piatki = int(kwota // 5)
kwota = round(kwota % 5, 1)

dwojki = int(kwota // 2)
kwota = round(kwota % 2, 1)

zlotowki = int(kwota // 1)
kwota = round(kwota % 1, 1)

piecdziesiatki = int(kwota // 0.5)
kwota = round(kwota % 0.5, 1)

dwudziestki = int(kwota//0.2)
kwota = round(kwota % 0.2, 1)

dziesiatki = int(kwota // 0.1)
kwota = round(kwota % 0.1, 1)

print(" Wydam Ci: \n" + str(piatki) + " piątek, ")
print(str(dwojki) + " dwojek,")
print(str(zlotowki) + " złotówek,")
print(str(piecdziesiatki) + " pięćdziesięciogroszówek,")
print(str(dwudziestki) + " dwudziestogroszówek,")
print('oraz ' + str(dziesiatki) + " dziesięciogroszówek,")
