arr = [3,5,1, 7, 11]

def progressiya(arr):
    arr.sort()
    d = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != d:
            return False
    return True

print(progressiya(arr))