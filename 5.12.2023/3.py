dt = {1:"ABC", 2:"DEF", 3:"GHI", 4:"JKL", 5:"MNO"}
for i in range(1, len(dt), 2):
   dt[i], dt[i+1] = dt[i+1], dt[i]
print(dt)