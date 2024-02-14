ls = [123, 456, 789, 852, 12, 42, 61, 369]
for i in ls:
    i = str(i)
    if int(i[0]) % 2 == 0:
        print(i, end=" ")