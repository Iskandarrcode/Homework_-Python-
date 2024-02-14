def xavfli(f1, f2):
    st = f1.read()
    new = st.replace('\n', ' ')
    a = new.split(" ")
    
    new2 = f2.read().lower()
    
    for i in a:
        new2 = new2.replace(i, len(i) * "*")
        
    print(new2)
    
    f1.close()
    f2.close()

f1 = open("forbidden_words.txt", "r")
f2 = open("Matn.txt", "r")

xavfli(f1, f2)
