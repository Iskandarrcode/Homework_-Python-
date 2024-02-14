ls = ['S001', 'S002', 'S003', 'S004']
ls2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
ls3 = [85, 98, 89, 92]
dt = {}
for i in range(len(ls)):
    # dt.update({ls[i]:{ls2[i]:ls3[i]}})
    dt[ls[i]] = {ls2[i]:ls3[i]}
print(dt)