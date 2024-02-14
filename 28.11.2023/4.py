for i in range(100, 999):
    if i // 100 == i % 100 // 10  or i // 100 == i % 10:
        if not i // 100 == i % 100 // 10 == i % 10:
            print(i, end=",")