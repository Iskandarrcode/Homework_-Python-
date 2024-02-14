arr = [2,3,4,7,11]
k = 5

def kam_son(arr, k):
    ls = list()
    count = 0
    for i in range(1,len(arr) + k + 1):
        if i not in arr:
            count += 1
            ls.append(i)
    return ls[k - 1]

print(kam_son(arr, k))