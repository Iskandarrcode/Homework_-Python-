ls = ["s", "t", "r", "i", "n", "g", "w"]
st = "string"

for i in ls.copy():
    if i in st:
        ls.remove(i)

print(ls)
