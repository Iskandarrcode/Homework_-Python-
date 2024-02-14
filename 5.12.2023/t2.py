n  = int(input("sonlarni kiriting: "))
dt = {}
for i in range(1, n):
    dt.update({i: i*i})
print(dt)