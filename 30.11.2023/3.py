arr = [7, 8, 1, 3, 4, 6, 7, 5]
arr2 = arr.copy()
arr2 = [arr2[i] ** 2 if i % 2 == 0 else arr2[i] ** 3 for i in range(len(arr))]
print(arr2)