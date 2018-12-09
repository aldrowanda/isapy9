# 1.. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
komunikat = 'Podaj temperature w stopniach Celcjusza '
c = input(komunikat)
f = round(5*float(c)/9-32, 1)
print('Zgodnie z formułą F=C*5/9 - 32 temperatura wynosi '+str(f)+' stopni Farenheita')


# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
f = input(komunikat.replace('Celcjusza', 'Farenheita'))
c = 9*(32+float(f))/5
c = round(c, 1)
print('Zgodnie z formułą C= 9*(F+32)/5 temperatura wynosi '+str(c)+' stopni Celcjusza')
