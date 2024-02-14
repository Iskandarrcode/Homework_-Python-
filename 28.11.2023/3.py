son = int(input("Son kiriting: "))
count = 0
for i in range(1 ,son + 1):
    if son % i == 0:
        count+=1
if count == 2:
    print("Tub son")
else:
    print("Murakkab son")