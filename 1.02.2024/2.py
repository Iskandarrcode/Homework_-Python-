def teskari():
    n = input("Son kiriting: ")
    count = 0
    for i in range(len(n)):
        if n[i] == "0" or n[i] == "6" or n[i] == "9":
            count += 1
            if count == len(n):
                return True
        else:
            return False
        
print(teskari())