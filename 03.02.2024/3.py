def typing():
    f = open("Istalgan.txt", "r")
    right = "YHNUJMIK.OLP:,/(-+=<>?'}{[]^&*67890"
    left = "QAZWSXEDGRFVTGB!@#$% 12345"
    n_r = 0
    n_l = 0
    for i in f.read():
        if str(i).upper() in right:
            n_r += 1
        if str(i).upper() in left:
            n_l += 1
    print(f"Left: {n_l}\nRight: {n_r}")
            
            
    

typing()