list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)

for x in range(1, 11):
    for y in range(1, 11):
        print (f'%d * %d = %d' % (x, y, x*y))

zdanie = "encyklopedia"
print(zdanie[4])
zdanie[-3]
zdanie[2:8]
zdanie[:7]
zdanie[8:]
zdanie[1:7:2]
zdanie[::-1]