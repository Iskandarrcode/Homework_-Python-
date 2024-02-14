import os

os.system("clear")

file = open("email.txt", "r")

for i in file.readlines():
    i = i.split("@")
    print(i[-1], end="")
    
file.close()