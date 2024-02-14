import os

os.system("clear")

file = open("sozlar.txt", "r")
file1 = open("toqq.txt", "w")
file2 = open("juftt.txt", "w")
st = file.read()
st = st.split(" ")
for i in st:
    if len(i) % 2 != 0 and i[0].isupper():
        file1.write(i + " ")
    elif len(i) % 2 == 0 and i[0].islower():
        file2.write(i + " ")

file.close()
file1.close()
file2.close()