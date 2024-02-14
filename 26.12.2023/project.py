import sys
import os
import re
import uuid
import time

class Dastur:
    def __init__(self):
        self.ind = None
        self.name = None
        self.surname = None
        self.number = None
        self.__email = None
        self.__password = None
        self.choose_keys = [1, 2, 3]
        self.operators = ["91", "90", "50", "93", "94", "97", "88", "99", "77", "85", "98", "33"]
        self.pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    @staticmethod
    def clear_terminal():
        if os.name == 'posix':  # Check if the operating system is POSIX (like macOS or Linux)
            os.system('clear')
        elif os.name == 'nt':  # Check if the operating system is Windows
            os.system('cls')

    def main_window(self):
        self.clear_terminal()
        print("""Assalomu alaykum tizimga xish kelibsiz!!!
                Login       [1]
                Registr     [2]
                Exit        [3]
        """)
        
        tanlov = int(input("Bo'limni tanlang: "))
        while not tanlov in self.choose_keys:
            self.clear_terminal()
            print("""Noto'g'ri bo'lim tanladingiz. 
                  Qaytadan urinib ko'ring
                            Login       [1]
                            Registr     [2]
                            Exit        [3]
                    """)

            tanlov = int(input("Bo'limni tanlang: "))

        if tanlov == self.choose_keys[0]:
            self.login()
        elif tanlov == self.choose_keys[1]:
            self.register()
        else:
            self.exit()

# LOGIN SECTIONS --------------------------------
    def login(self):
        self.clear_terminal()
        f = open("baza.txt", "r")
        
        print("             Login            ")
        self.__email = input("Emailingizni kiriting: ").strip()
        self.__password = input("parolingizni kiriting: ").strip()
        
        ls = f.readlines()
        s = 1
        for i in range(0, len(ls)):
            a = ls[i].split(',')
            
            if a[4] == self.__email and a[5] == self.__password:
                self.ind = i
                f.close()
                self.menu()
                s = 0
            if s:
                print("Error Login:")
                
    # MENU -------------------------------- 
    def menu(self):
        self.clear_terminal()
        
        print("        MENU         ")
        
        print("""
                
        change_phone_number            [1]
        change_email                   [2]
        change_password                [3]
        
        """)
        
        tanlov2 = int(input("Bo'limni tanlang: "))
        if tanlov2 == self.choose_keys[0]:
            self.change_phone_number()
        if tanlov2 == self.choose_keys[1]:
            self.change_email()
        if tanlov2 == self.choose_keys[2]:
            self.change_password()
        
    # CHANGE NUMBERS --------------------------------
    def change_phone_number(self):
        f = open("baza.txt", "r")
        
        self.number2 = input("Phone Number: (998) 93-758-55-90__")
        
        while not (self.number2[0:6] == "(998) " and self.number2[6:8] in self.operators and self.number2[8] == "-" and self.number2[9:12].isdigit() and self.number2[12] == "-" and self.number2[13:15].isdigit() and self.number2[15] == "-" and self.number2[16:19].isdigit()):
            print("Telefo'n raqam noto'g'ri kiritildi: ")
            self.number2 = input("Phone Number: (998) 93-758-55-90__")
            
        ls = f.readlines()
        f.close()
        f = open("baza.txt", "w")
        ls2 = ls[self.ind].split(",")
        ls2[3] = self.number2
        ls[self.ind] = ", ".join(ls2)
        f.writelines(ls)
        f.close()
        
    # CHANGE EMAIL ----------------------------------------------------------------
    def change_email(self):
        f = open("baza.txt", "r")
        
        self.email2 = input("Email Address kiriting: ")
        self.check_email()
        
        ls = f.readlines()
        f.close()
        
        f = open("baza.txt", "w")
        ls2 = ls[self.ind].split(",")
        ls2[4] = self.email2
        ls[self.ind]  = ", ".join(ls2)
        f.writelines(ls)
        f.close() 
                           
    # CHANGE PASSWORD ----------------------------------------------------------------  
    def change_password(self):
        f = open("baza.txt", "r")
        
        self.password2 = input("Password kiriting: ")
        while len(self.__password) <= 8:
            self.clear_terminal()
            self.__password = input("Parolingizni qaytadan kiriting: ").strip()
        
        ls = f.readlines()
        f.close()
        
        f = open("baza.txt", "w")
        ls2 = ls[self.ind].split(",")
        ls2[5] = self.password2
        ls[self.ind] = ",".join(ls2)
        f.writelines(ls)
        f.close()   
    # REGISTER ----------------------------------------------------------------
    def register(self):
        self.clear_terminal()
        print("             Register            ")
        self.name = input("Ismingizni kiriting: ").strip()
        self.surname = input("Familiyangizni kiriting: ").strip()
        self.number = input("Telefon raqamingizni kiriting: (998) 93-758-55-90").strip()
        self.__email = input("Emailingizni kiriting: ").strip()
        self.__password = input("parolingizni kiriting: ").strip()

        while not len(self.name) >= 3:
            self.clear_terminal()
            self.name = input("Ismingizni qaytadan kiriting: ").strip()

        while not len(self.surname) >= 3:
            self.clear_terminal()
            self.surname = input("Familiyangizni qaytadan kiriting: ").strip()
        
        while not (self.number[0:6] == "(998) " and self.number[6:8] in self.operators and self.number[8] == "-" and self.number[9:12].isdigit() and self.number[12] == "-" and self.number[13:15].isdigit() and self.number[15] == "-" and self.number[16:19].isdigit()):
            self.clear_terminal()
            self.number = input("Telefon raqamingizni qaytadan kiriting: ").strip()

        self.check_email()
        
        while len(self.__password) <= 8:
            self.clear_terminal()
            self.__password = input("Parolingizni qaytadan kiriting: ").strip()

        self.write_data()

    # Write data ----------------------------------------------------------------
    def write_data(self):
        if not os.path.exists("baza.txt"):
            f = open("baza.txt", "w")
            f.write("id,name,surname,number,email,password")
            f.close()
        f = open("baza.txt", "r+")

        ls = f.readlines()

        for i in ls:
            i = i.split(",")
            if i[4] == self.__email:
                self.check_email(2)

        current_time = time.localtime()  
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

        f.write(f"\n{uuid.uuid4()},{self.name},{self.surname},{self.number},{self.__email},{self.__password},{formatted_time}")
        f.close()

    #EXIT --------------------------------
    def exit(self):
        self.clear_terminal()
        print("""Siz dasturdan chiqdingiz""")
        sys.exit()

    #CHEK EMAIL -------------------------------
    def check_email(self, position=1):
        while not re.match(self.pattern, self.__email):
            self.clear_terminal()
            if position == 2:
                print("""Bu email allaqchon ro'yhatdan o'tgan. 
                      Boshqa emaildan foydalaning""")
            self.__email = input("Emailingizni qaytadan kiriting: ").strip()



dastur = Dastur()
dastur.main_window()