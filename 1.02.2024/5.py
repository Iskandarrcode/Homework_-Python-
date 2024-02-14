import mysql.connector as myc
import os

class Database:
    def create_database(self, database_name):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        cursor = con.cursor()
        cursor.execute(f"Create database if not exists {database_name}")
        con.commit()
    
    def create_table(self, tb_name = "User", db_name = "USER"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        cursor = con.cursor()
        value = f"""Create table if not exists {tb_name} (id int primary key auto_increment, name varchar(60), surname varchar(60), age int, address varchar(300))"""
        cursor.execute(value)
        con.commit()
    
    def insert_into(self, name, surname, age, address):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "USER")
        cursor = con.cursor()
        sql = """Insert into User (name, surname, age, address) value (%s, %s, %s, %s)"""
        value = (name, surname, age, address)
        cursor.execute(sql, value)
        con.commit()
        
    def top1(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "USER")
        cursor = con.cursor()
        sql = """Select * from User"""
        cursor.execute(sql)
        data = cursor.fetchall()
        
        print("\n________1 - SHART_______\n")
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if data[i][4] == data[j][4]:
                    print(data[i])
                    print("_"*30)
                    print(data[j])
                    print("_"*30)
                    
        
        print("\n\n________2 - SHART_______\n")
        for i in range(len(data)):
            t = True
            for j in range(i+1, len(data)):
                if data[i][4] == data[j][4]:
                    t = False
                    
            if t:
                print(data[i])
                print("_"*30)

                  



db = Database()
db.create_database("USER")
db.create_table("User")
db.top1()

# db.insert_into("Abdulla", "Abdullayev", 25, "Toshkent.sh, M.Ulug'bek tumani, Bobur ko'chasi 5-uy")

# db.insert_into("Nodira", "Abdullayeva", 22, "Toshkent.sh, M.Ulug'bek tumani, Bobur ko'chasi 5-uy")

# db.insert_into("Shoxrux", "Rustamov", 20, "Toshkent.sh, .Chilonzor tumani, Namatak ko'chasi 1-uy 25-honadon")

# db.insert_into("Hilola", "Rasulova", 21, "Toshkent.sh, Chilonzor tumani, Jalilov ko'chasi 5-uy 2-honadon")

# db.insert_into("Jalil", "Rasulova", 18, "Toshkent.sh, Chilonzor tumani, Jalilov ko'chasi 5-uy 2-honadon")

# db.insert_into("Temur", "Qodirov", 23, "Toshkent.sh, Yunusobod tumani, Safiya ko'chasi 25-uy")

# db.insert_into("Sardor", "Kamolov", 20, "Toshkent.sh, Yunusobod tumani, 2-kvartal, 4-uy 75-honadon")

# db.insert_into("Botir", "Malikov", 19, "Toshkent.sh, Mirobod tumani, Temuriylar ko'chasi 12-uy")

# db.insert_into("Lola", "Kamolova", 24, "Toshkent.sh, Yunusobod tumani, 2-kvartal, 4-uy 75-honadon")

# db.insert_into("Maftuna", "Farruxova", 19, "Toshkent.sh, Olmazor tumani, Amri Temu ko'chasi, 4-uy 63-honadon")