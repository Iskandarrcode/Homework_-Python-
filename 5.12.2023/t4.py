n = int(input("Dictonaryga elementlari sonini kiriting: "))
dt  = {}

for i in range(n):
    son = int(input("Dictionaryga qiymat bering: "))
    dt.update({i: son})
print(dt)

for j in range(3):
    mx = max(dt.values())
    for i, val in dt.items():
        if val == mx:
            dt.pop(i)
            print(i, end=" ")
            break