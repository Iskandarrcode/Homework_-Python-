d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = {}
for i in set(d1.keys()).union(d2.keys()):
    d[i] = d1.get(i, 0) + d2.get(i, 0)
print(d)