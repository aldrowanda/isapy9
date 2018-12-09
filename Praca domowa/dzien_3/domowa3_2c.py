# 2) Program przyjmuje kwotę
#  w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.

# rozwiązanie algorytmiczne 2

kwota = float(input('podaj swoją kwotę do rozmienienia: '))
bilon = (5, 2, 1, 0.5, 0.2, 0.1)
bilon_str = ('5zł', '2zł', '1zł', '0.5zł', '0.2zł', '0.1zł')
i = 0
print("Dostaniesz:")

while i <= len(bilon)-1:
    liczba_monet = int(kwota // bilon[i])
    print('{} monety {}'.format(liczba_monet, bilon_str[i]))
    kwota = round(kwota % bilon[i], 1)
    i += 1
