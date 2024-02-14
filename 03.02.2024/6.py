import os

os.system("cls")

ls = list(map(int, input().split(" ")))

sorov = list()

for i in range(ls[2]):
    tem = list(map(int, input().split()))
    sorov.append(tem)

num = ls[1]
list = list()

os.system("cls")
for i in sorov:
    for j in range(0, i[0] + 1):
        while j in list:
            list.remove(j)
            num += 1
    if num > 0:
        list.append(i[1])
        num -= 1
        print(1)
    else:
        print(0)
