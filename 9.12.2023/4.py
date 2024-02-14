from math import *
son = input("son kiriting: ")

sum = 0
a = 1
print(son)
for i in range(0, len(son)):
    sum += pow(int(son[i]), a)
    a += 1
if sum == int(son):
    print("True")
else:
    print("False")