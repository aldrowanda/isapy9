# 2) Program przyjmuje kwotę w parametrze
#  wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.
# rozwiązanie algorytmiczne 1

kwota = float(input('podaj swoją kwotę do rozmienienia: '))
bilon = (5, 2, 1, 0.5, 0.2, 0.1)
bilon_str = ('5zł', '2zł', '1zł', '0.5zł', '0.2zł', '0.1zł')
print("Dostaniesz:")

for moneta, moneta_str in zip(bilon, bilon_str):
    liczba_monet = int(kwota // moneta)
    kwota = round(kwota % moneta, 1)
    print('{} razy {}'.format(liczba_monet, moneta_str))
