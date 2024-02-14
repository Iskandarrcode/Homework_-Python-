ls = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]
for i in ls:
    if i == 0:
        ls.remove(i)
        ls.append(0)
print(ls)
        