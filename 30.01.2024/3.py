def takror(st):
    st2 = str()
    countt = 0
    
    for i in range(0, len(st)):
        st2 += st[i]
        countt = st[:i].count(st[i])
        if countt > 0:
            st2 += ( "_" + str(countt))
    print(st2)

st = input("string kiriting: ")
takror(st)