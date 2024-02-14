tp = (["at", "be", "th", "au"], ["beautiful", "the", "hat"])
tp = list(tp)

def top(tp):
    for i in tp[0]:
        count = 0
        for j in tp[1]:
            if i in j:
                count += 1
        if count == 0:
            return False
    return True

print(top(tp))