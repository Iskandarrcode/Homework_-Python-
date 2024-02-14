import os


class Product:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name


class Book(Product):
    def __init__(self, ID, name, author, count, price):
        Product.__init__(self, ID, name)
        self.author = author
        self.count = count
        self.price = price
        self.file = None
        self.f = None

    def DecreaseOne(self):
        ls = list()
        self.file = open("Malumotlar.txt", "r+")
        ls = self.file.readlines()
        for i in range(len(ls)):
            if ls[i].startswith(self.ID):
                ls[i] = ls[i].split(",")
                ls[i][-2] = str(int(ls[i][-2]) - 1)
                ls[i] = ",".join(ls[i])
        self.file.seek(0)
        self.file.writelines(ls)
        self.file.close()

    def delete(self):
        self.file = open("Malumotlar.txt", "r")
        ls2 = list()
        ls2 = self.file.readlines()
        ls3 = list()

        for i in ls2:
            if not i.startswith(self.ID):
                ls3.append(i)
                
        self.file.close()
        
        os.remove("Malumotlar.txt")
        self.f = open("Malumotlar.txt", "w")
        self.f.seek(0)
        self.f.writelines(ls3)


book1 = Book("1234", "Mehrobdan chayon", "Abdulla Oripov", 12, 30000)
book1.DecreaseOne()

book1.delete()
