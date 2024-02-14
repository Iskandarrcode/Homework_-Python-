ls = [    
    [2, 15, 4],
    [19, 24, 11],
    [7, 9, 5],
    [10, 3, 1]
    ]
for i in range(len(ls)):
    for j in range(3):
        if j % 2 != 0:
            ls[i][j] *= ls[i][j]
print(ls)