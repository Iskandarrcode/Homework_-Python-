tpl = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
arr = []
for i in range(0, len(tpl)):
   if len(tpl[i]) != 0:
       arr.append(tpl[i])
print(arr)