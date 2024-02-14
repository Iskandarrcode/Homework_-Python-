from math import *
son = int(input("Son kiriting: "))
sum = 1
for i in range(1, son+1):
    sum *= factorial(i)
    
print(sum)
        