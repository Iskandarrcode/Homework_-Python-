import os
os.system("clear")
ls = [1, 45, "Hi", False, True]
# [int, str, bool, list, tuple, dictionary]

def typs(ls):
    a = 0
    st = 0
    b = 0
    l = 0
    tp = 0
    dc = 0
    for i in ls:
        if type(i) == int:
            a += 1
        if type(i) == str:
            st += 1
        if type(i) == bool:
            b += 1
        if type(i) == list:
            l += 1
        if type(i) == tuple:
            tp += 1
        if type(i) == dict:
            dc += 1
    tip = [a, st, b, l, tp, dc]
    return tip
print(typs(ls))