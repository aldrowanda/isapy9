# 5. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)

szer=input("Podaj szerokość prostokąta")
wys=input("Podaj wysokość prostokąta")
print('+'+"-"*int(szer)+'+')
print((('|'+" "*int(szer)+'|'+'\n')*int(wys)),end='')
print('+'+"-"*int(szer)+'+')

