tpl = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

for i in range(0, len(tpl)):
    for j in range(i+1, len(tpl)):
        if float(tpl[i][1]) < float(tpl[j][1]):
            tpl[i], tpl[j] = tpl[j], tpl[i]
print(tpl)