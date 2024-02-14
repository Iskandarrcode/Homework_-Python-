x = int(input("1 - sonni kiriting: "))
y = int(input("2 - sonni kiriting: "))
z = int(input("3 - sonni kiriting: "))
ekub = 1
for i in range(1, 100):
    if x % i == 0 and y % i == 0 and z % i == 0:
        ekub = ekub * i
print(f"EKUB = {ekub}")