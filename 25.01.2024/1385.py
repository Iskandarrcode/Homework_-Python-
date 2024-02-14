arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
c = 0

for i in arr1:
    vaild = True
    for j in arr2:
        d2 = abs(i - j)
        if d2 <= d:
            vaild = False
            break
    if vaild:
        c += 1
print(c)