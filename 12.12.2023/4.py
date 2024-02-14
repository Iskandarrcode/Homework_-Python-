import os
os.system("clear")

file = open("raqamlar.txt", "r")

st = set()
ls = list()

for i in file.readlines():
    i = i.split(" ")
    if i[1] == '33':
        st.add("Humans")
    if i[1] == '62':
        st.add("Xorazim GR")
    if i[1] == '55':
        st.add("Ucell")
    if i[1] == '90':
        st.add("Mobiuz")
    if i[1] == '88':
        st.add("Mobiuz")
    if i[1] == '71':
        st.add("Toshkent shaxar GR")
    if i[1] == '61':
        st.add("Qoraqalpog'iston GR")
    if i[1] == '98':
        st.add("Perfectom")
print(st)
file.seek(0)
for i in file.readlines():
    i = i.split(" ")
    ls.append(i[2] + i[3] + i[4][:-1])
    print(i[2] + i[3] + i[4][:-1])
    
for i in ls:
   son = ls.count(i)
   if son == 1:
       print(i)
       
file.close()