import os
os.system("claer")

son = int(input("Son kiriting: "))
i = son
sum = 0
while i != 0:
    sum += i % 10
    i = i // 10
print(sum)

if son % sum == 0:
    print("True")
else:
    print("False")