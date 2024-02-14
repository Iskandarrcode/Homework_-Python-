import mysql.connector as myc
import os

class Database:
    def create_database(self, name_database):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        cursor = con.cursor()
        cursor.execute(f"Create database if not exists {name_database}")
        con.commit()
        
    def create_table(self, tb_name = "Product", db_name = "PRODUCT"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        cursor = con.cursor()
        surov = f"""Create table if not exists {tb_name} (id int primary key auto_increment, Maker varchar(30), Model int, Type varchar(60))"""
        cursor.execute(surov)
        con.commit()
        
    def insert_into(self, Maker, Model, Type):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "PRODUCT")
        cursor = con.cursor()
        sql = """Insert into Product (Maker, Model, Type) values (%s, %s, %s)"""
        values = (Maker, Model, Type)
        cursor.execute(sql, values)
        con.commit()
    
    def oxshash(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "PRODUCT")
        cursor = con.cursor()
        sql = "Select * from Product"
        cursor.execute(sql)
        data = cursor.fetchall()
        
        print("\n________1 - SHART_______\n")
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if data[i][1] == data[j][1]:
                    if data[i][3] == data[j][3]:
                        print(data[i])
                        print("_"*30)
                        
        con.commit()
    
    def unikal(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "PRODUCT")
        cursor = con.cursor()
        sql = "Select * from Product ORDER BY Type"
        cursor.execute(sql)
        data = cursor.fetchall()
        
        print("\n\n\n________2 - SHART_______\n")
        
        for i in range(len(data)):
            ln = str(data[i][2])
            ln2 = set(ln)
            if len(ln2) == len(ln):
                print(data[i])
                print("_"*30)
        
        con.commit()


db = Database()
db.create_database("PRODUCT")
db.create_table("Product")
db.oxshash()
db.unikal()

# db.insert_into("HP", 12318, "Kompyuter")
# db.insert_into("Acer", 1010, "Noutbuk")
# db.insert_into("Asus", 1378, "Noutbuk")
# db.insert_into("Lenovo", 6711, "Kompyuter")
# db.insert_into("HP", 182198, "Printer")
# db.insert_into("Canon", 6789, "Printer")
# db.insert_into("HP", 1478963, "Printer")
# db.insert_into("LG", 125478, "Kompyuter")
# db.insert_into("Lenovo", 362145, "Noutbuk")
# db.insert_into("Xiaomi", 98763, "Noutbuk")
