# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)

import math
message = 'Podaj promień koła: '
r = input(message)
area = math.pi*float(r)**2
result = 'Dla promienia wynoszącego {}, powierzchnia wynosi {:f.2}'.format(r, round(area, 3))
print(result)
print(f'Dla promienia wynoszącego {r}, powierzchnia wynosi {area}')
'''czy aby obciąć zbędne cyfry w drugim princie
 mogę zrobic tylko tak??: '''
disp_area = round(area, 2)
print(f'Dla promienia wynoszącego {r}, powierzchnia wynosi {disp_area}')
# czy zmienna disp_area jest nową zmienną czy ma ten sam adres w pamięci z area
# stringi i int jest niereferencyjne i tworzy się jego nowa kopia
print(area)
