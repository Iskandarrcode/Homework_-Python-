ls = [(1, 2), (2, 3), (3, 4)]
ls2 = []
sum = 0
for i in ls:
    sum = i[0] + i[1]
    ls2.append(sum)
    sum = 0
print(ls2)