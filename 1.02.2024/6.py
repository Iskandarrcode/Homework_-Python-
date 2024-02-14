def animalss():
    animals = ["dog", "cat", "bat", "coock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat"]
    ls = list()
    
    st = input("Satirni kiriting: ")
    n = 0
    
    for i in range(0, len(animals)):
        a = str()
        b = 0
        a = animals[i]
        ln = len(a)
    
        for j in a:
            if j in st:
                b += 1
                if b == ln:
                    ls.append(a)
                    n += 1   
    print(n, ls)

animalss()
                