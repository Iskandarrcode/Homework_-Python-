ls = 'w3resource'
dt = {}
n = 0
for i in ls:
    for j in ls:
        if i == j:
            n+=1
    dt.update({i: n})
    n = 0
print(dt)