import colorama
from colorama import Fore

class Mylist(list):
    def __init__(self, ls):
        super().__init__(ls)
    
    def append(self, item):
        if item not in self:
            super().append(item)
        else:
            raise Exception(Fore.RED + "ElementDuplicationError:")

l = Mylist([1, 2, 3, 4, 5, 1,  6, 7])
l.append(1)
print(l)