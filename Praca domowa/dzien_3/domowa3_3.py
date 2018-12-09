# 3) Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####
ilosc=input("Podaj ilosc poziomów piramidy")
liczba=int(ilosc)

for poziom in range(1,liczba+1):
    print(" "*(liczba-poziom) + '#'*(2*poziom-1) )