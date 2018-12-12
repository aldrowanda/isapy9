# 1.. Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)
komunikat = 'Podaj temperature w stopniach Celcjusza '
c = input(komunikat)
f = round(5*float(c)/9-32, 1)
print('Zgodnie z formułą F=C*5/9 - 32 temperatura wynosi '+str(f)+' stopni Farenheita')
