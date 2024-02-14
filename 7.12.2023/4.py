def necha(ls) -> int:
    count = 0
    
    for i in ls:
        if i == "0":
            count += 1
        elif i != "0":
            return count
    
ls = input("Son kiriting: ")
ls = list(ls)

print(necha(ls))    