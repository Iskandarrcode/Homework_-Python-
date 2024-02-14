def birthday():
    name = input("What is your name?: ")
    age = input("What is your age?: ")
    f = open("Tort.txt", "w")
    ln1 = len(name)
    ln2 = len(age)
    
    if int(age) % 2 == 0:
        f.write("#"*(ln1+ln2+13))
        f.write(f"\n# {age} Happy Birthday {name}! {age}  #\n")
        f.write("#"*(ln1+ln2+13))
        f.write("\n")
    else:
        f.write("*"*(ln1+ln2+21))
        f.write(f"\n* {age} Happy Birthday {name}! {age}  *\n")
        f.write("*"*(ln1+ln2+21))
    f.close()
        
birthday()