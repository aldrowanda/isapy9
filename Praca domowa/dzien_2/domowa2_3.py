# 4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
num = input('Podaj swoja liczbę')
first = num[0]
last = num[-1]
print('Pierwsza cyfra to {}, druga liczba to {}'.format(first, last))
print(f'Pierwsza cyfra to {first}, druga liczba to {last}')
print('Pierwsza cyfra to {pierwsza}, druga liczba to {druga}'.format(pierwsza=first, druga=last))
