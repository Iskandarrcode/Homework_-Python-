n = 5
start = 0

def lis(n, start):
    ls = list()
    son = start
    for i in range(n):
        son = start + i * 2
        ls.append(son)
        
    result = 0
    for num in ls:
        result ^= num 

    return result

print(lis(n, start))