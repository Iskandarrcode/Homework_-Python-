n = int(input("n ga qiymat kiriting: "))
f1 = 0
f2 = 1
while f1 < n:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f1, end=" ")