import os
os.system("clear")

file = open("karta.txt", "r")

ls = list()
ls1 = list()
ls2 = list()
ls3 = list()
dt = dict()

for i in file.readlines():
    a = i.split(",")
    ls.append(a[-1])
    son = ls.count(a[-1])
    dt.update({a[-1]: son})
print(dt)

file.seek(0)
print("\n")

for i in file.readlines():
    b = i.split(",")
    if b[1] =="visa":
        ls2.append(b[-1])
print(sorted(ls2))
print("\n")

file.seek(0)

for i in file.readlines():
    ls1.append(i)

for i in ls1:
    c = i.split(",")

    chr = 1   
    for j in range(10):
        if str(j) not in c[0]:
            chr = 0
            break
    if chr:
        print(c[0] + "," + c[-1] + "," +  c[2] + "," + c[-2])
        
file.close()