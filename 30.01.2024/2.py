ls = ["AEIOULNSTR", "DG", "BCMP", "FGWVY", "K", "JX", "QZ"]
st = input("Katta harflarni kiriting: ")

def Scrabble(ls, st):
    st = list(st)
    ball = 0
    for i in range(len(st)):
        for j in range(len(ls)):
            if i == 0:
                if st[i] in ls[j]:
                    ball += 1
                    break
            elif i == 1:
                if st[i] in ls[j]:
                    ball += 2
                    break
            elif i == 2:
                if st[i] in ls[j]:
                    ball += 3
                    break
            elif i == 3:
                if st[i] in ls[j]:
                    ball += 4
                    break
            elif i == 4:
                if st[i] in ls[j]:
                    ball += 5
                    break
            elif i == 5:
                if st[i] in ls[j]:
                    ball += 8
                    break
            elif i == 6:
                if st[i] in ls[j]:
                    ball += 10
                    break
    print(ball)
  
Scrabble(ls, st)