# 13:00
def colors():
    col = input("Ranglarni kiriting: ")
    color = col.split(" ")
    print(color)
    count = 2
        
    for j in range(1, len(color)):
        if color[j] == color[j - 1]:
            count += 2
        else:
            count += 3
    print(count)
    
colors()