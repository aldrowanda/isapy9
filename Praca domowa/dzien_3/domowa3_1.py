# 1. Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
# a)
# Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość,
# tekst wyrównany do lewej.
# b)
# Maksymalna szerokość kolumny np 30znaków
# jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
# c)
# A jeszcze większym atutem będzie
#  gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)

# col_1=str(input("Podaj tekst kolumny nr 1 "))
# col_2=str(input("Podaj tekst kolumny nr 2 "))
# col_3=str(input("Podaj tekst kolumny nr 3 "))

lista= ['c', 'co', "col"]

print("+", end="")
for element in (lista):
    for litera in element:
        print("-", sep="s", end="")
    print("+", end="")
print()

print("|", end="")
for element in (lista):
    print( element, end="")
    print("|", end="")
print()

print("+", end="")
for element in (lista):
    for litera in element:
        print("-", end="")
    print("+", end="")
print()
