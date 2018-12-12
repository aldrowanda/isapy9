# 2. Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)
f = input(komunikat.replace('Celcjusza', 'Farenheita'))
c = 9*(32+float(f))/5
c = round(c, 1)
print('Zgodnie z formułą C= 9*(F+32)/5 temperatura wynosi '+str(c)+' stopni Celcjusza')