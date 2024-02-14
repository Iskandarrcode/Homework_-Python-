import os

os.system("clear")

file = open("nums.txt", "r")
file1 = open("juft.txt", "w")
file2 = open("toq.txt", "w")

ls = file.readline()
ls = ls.split(" ")
for i in range(0, len(ls)):
    if int(ls[i]) % 2 == 0:
        file1.write(ls[i] + " ")
    else:
        file2.write(ls[i] + " ")
        
file.close()
file1.close()
file2.close()