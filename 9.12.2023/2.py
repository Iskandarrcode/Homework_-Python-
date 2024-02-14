tp = [[1, 1], [2, 2], [1, 1], [2, 2]]
st = "ABAB"

def tengmi(tp, st):
    st2 = []
    for i in range(len(st)):
        st2.append(st[i])
    for i in range(0, len(tp)):
        for j in range(i+1, len(tp)):
            if tp[i] == tp[j]:
                if st2[i] != st2[j]:
                    return False
    return True
print(tengmi(tp, st))