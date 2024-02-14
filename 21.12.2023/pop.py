class Mylist(list):
    def __init__(self, ls):
        super().__init__(ls)
        
    def pop(self, i):
        v = l[i]
        
        while v in l:
            l.remove(v)
            

l = Mylist([1, 2, 3, 4, 5, 1,  6, 7])

l.pop(0)
print(l)