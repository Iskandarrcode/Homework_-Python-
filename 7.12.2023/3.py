import os
os.system("clear")

nums = list(map(lambda a: int(a), input("Qiymat kiriting: ").split()))
juft = list(filter(lambda a: a % 2 == 0, nums))
print(juft)
toq = list(filter(lambda a: a % 2 != 0, nums))
print(toq)