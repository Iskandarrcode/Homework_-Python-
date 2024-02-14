arr = [10,2,5,3]
def checkIfExist(arr):
        l = len(arr)
        for i in range(0, l):
            for j in range(i+1, l):
                if arr[i] == 2 * arr[j]:
                    return True

        for i in range(l-1, 0, -1):
            for j in range(i-1, -1, -1):
                if arr[i] == 2 * arr[j]:
                    return True
        return False
    
print(checkIfExist(arr))