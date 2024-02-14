ls = []
for i in range(3):
    a = input("Kiriting: ")
    ls.append(a)

res = [[]]
ls2 = []


for i in range(len(ls)):
    res.append(ls[i])
    res.append([ls[i], ls[i-1]])
    ls2.append(ls[i])
res.append(ls2)
    
print(res)