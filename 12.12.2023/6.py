import os
os.system("cls")

if os.path.exists("mashina.txt"):
    file = open("mashina.txt", "r")
    dic = dict()
    tem = file.readline()
    for i in file.readlines():
        i = i.replace('\n', '').split(",")
        if i[4] in dic.keys():
            dic[i[4]] += 1
        else:
            dic.update({i[4]: 1})

    Max = None
    sch = 0    
    for i in dic.items():
        if i[1] > sch:
            Max = i[0]
            sch = i[1]
    print(f"---{Max}--- brandi eng ko'q uchragan brend ekan")

    file.seek(0)
    tem = file.readline()

    country = dict()
    for i in file.readlines():
        i = i.replace('\n', '').split(",")
        if i[4] == Max:
            if i[-1] in country.keys():
                country[i[-1]] += 1
            else:
                country.update({i[-1]: 1})

    MaxInCountry = ""
    MaxCount = 0
    MinInCountry = ""
    MinCount = 0
    for i in country.items():  
        if i[1] > MaxCount:
            MaxInCountry = i[0]
            MaxCount = i[1]
        if i[1] < MinCount:
            MinInCountry = i[0]
            MinCount = i[1]
        if MinCount == 0:
                MinInCountry = i[0]
                MinCount = i[1]
    
    print(f"{MaxInCountry} davlatida {MaxCount} ta bor ekan")
    print(f"{MinInCountry} davlatida {MinCount} ta bor ekan")
    file.close()
else:
    raise Exception("Error: mashina.txt not found")