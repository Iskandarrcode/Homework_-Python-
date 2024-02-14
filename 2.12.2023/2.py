lt = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(0, len(lt)):
    arr = list(lt[i])
    arr.pop(len(arr) - 1)
    arr.append(100)
    lt[i] = tuple(arr)
print(lt)