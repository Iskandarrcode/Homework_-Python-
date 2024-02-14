class Froction:
    def __init__(self, Nomeration, Denomeration):
        self.Numeration = Nomeration
        self.Denomeration = Denomeration
        
    def qoshish(self, surat2, maxraj2):
        if self.Denomeration == 0:
            print("Denomeration != 0: ")
            return
        if self.Denomeration != maxraj2:
            sum = (self.Numeration * maxraj2) + (surat2 * self.Denomeration)
            mah = maxraj2 * self.Denomeration
            print(f"\nYig'indi:  {sum} / {mah}\n")
        else:
            sum = self.Numeration + surat2
            mah = maxraj2
            print(f"Yig'indi: {sum} / {mah}\n")
                
    def ayirish(self, surat2, maxraj2):
        if self.Denomeration == 0:
            print("Denomeration != 0: ")
            return
        if self.Denomeration != maxraj2:
            sum = (self.Numeration * maxraj2) - (surat2 * self.Denomeration)
            mah = maxraj2 * self.Denomeration
            print(f"Ayirma:  {sum} / {mah}\n")
        else:
            sum = self.Numeration - surat2
            mah = maxraj2
            print(f"Yig'indi: {sum} / {mah}\n")
    
    def kopaytr(self, surat2, maxraj2):
        if self.Denomeration == 0:
            print("Denomeration != 0: ")
            return
        sum = (self.Numeration) * (surat2)
        mah = maxraj2 * self.Denomeration
        print(f"Ko'paytma:  {sum} / {mah}\n")
    
    def bolish(self, surat2, maxraj2):
        if self.Denomeration == 0:
            print("Denomeration != 0: ")
            return
        sum = (self.Numeration) * (maxraj2)
        mah = surat2 * self.Denomeration
        print(f"Bo'linma:  {sum} / {mah}\n")
    
surat1 = int(input("Surat 1 ni kiriting: "))
maxraj1 = int(input("Maxraj 1 ni kiriting: "))

surat2 = int(input("Surat maxraj2 ni kiriting: "))
maxraj2 = int(input("Maxraj maxraj2 ni kiriting: "))


ab1 = Froction(surat1, maxraj1)
ab2 = Froction(surat2, maxraj2)
ab1.qoshish(surat2, maxraj2)
ab1.ayirish(surat2, maxraj2)
ab1.kopaytr(surat2, maxraj2)
ab1.bolish(surat2, maxraj2)