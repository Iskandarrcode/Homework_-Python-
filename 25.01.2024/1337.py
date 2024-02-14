mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

k = 3

def sorts(mat, k):
    strength = [(sum(row), i) for i, row in enumerate(mat)]
    
    result = [i for _, i in sorted(strength)[:k]]
    
    print(result)

sorts(mat, k)
