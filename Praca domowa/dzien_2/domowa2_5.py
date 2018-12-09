# 6. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc.

liczba = input("Podaj swoją sześciocyfrową liczbę binarną: ")

if len(liczba) == 6:
    cyfra0 = int(liczba[0])*32
    cyfra1 = int(liczba[1])*16
    cyfra2 = int(liczba[2])*8
    cyfra3 = int(liczba[3])*4
    cyfra4 = int(liczba[4])*2
    cyfra5 = int(liczba[5])*1
    wynik = cyfra0+cyfra1+cyfra2+cyfra3+cyfra4+cyfra5
    print("w zapisie dziesiętnym twoja liczba wynosi:"+str(wynik))
else:
    print("miała być szesciocyfrowa!!!")
