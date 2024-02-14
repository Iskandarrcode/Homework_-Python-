import mysql.connector as myc
import os

class Database:
    def create_database(self, database_name):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        kursor = con.cursor()
        kursor.execute(f"Create database if not exists {database_name}")
        con.commit()
        
    def create_table(self, tb_name = "ovqat", db_name = "MILLIY_TAOMLAR"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        surov = f"""Create table if not exists {tb_name} (id int primary key auto_increment, Taom_nomi varchar(60) NOT NULL, Taom_masalliqlari varchar(60))"""
        kursor.execute(surov)
        con.commit()
        
    def insert_into(self, Taom_nomi, Taom_masalliqlari):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "MILLIY_TAOMLAR")
        kursor = con.cursor()
        sql = """Insert into ovqat (Taom_nomi, Taom_masalliqlari)  Values(%s,%s)"""
        value = (Taom_nomi, Taom_masalliqlari)
        kursor.execute(sql, value)
        con.commit()
    
    def view_data(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "MILLIY_TAOMLAR")
        kursor = con.cursor()
        sql = "SELECT * from ovqat where Taom_nomi like 'a%'  "
        kursor.execute(sql)
        data = kursor.fetchall()
        
        for x in data:
            print(f"id:    {x[0]}\n")
            print(f"Taom_nomi:     {x[1]}\n")
            print(f"Taom_masalliqlari:     {x[2]}")
            print("__"*25)
            print("\n")
            
    def view_data2(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "MILLIY_TAOMLAR")
        kursor = con.cursor()
        sql = f"SELECT * from ovqat where Taom_masalliqlari like '%guruch%' "
        kursor.execute(sql)
        data = kursor.fetchall()
        
        for x in data:
            print(f"id:    {x[0]}\n")
            print(f"Taom_nomi:     {x[1]}\n")
            print(f"Taom_masalliqlari:     {x[2]}")
            print("__"*25)
            
        
    
        
        
        
db = Database()
# db.create_database("MILLIY_TAOMLAR")
# db.create_table("ovqat")
# db.insert_into("osh", "Guruch, Yog', Gosht, Sabzi, Sarimsoq")
# db.insert_into("aralashma", "Guruch, Yog', Gosht, Sabzi")
# db.insert_into("shashlik", "Gosht, non, piyoz, sarimsoq")
# db.insert_into("somsa", "Un, Yog', Gosht, piyoz")
# db.insert_into("manti", "Un, Yog', Gosht, kartoshka")
# db.insert_into("barak", "Un, Gosht, piyoz, ayron")
# db.insert_into("free", "Kartoshka, Yog', Gosht")
# db.insert_into("shorva", "Yog', Gosht, Sabzi, kartoshka, piyoz, pamidor")
# db.insert_into("kabob", "Yog', Gosht, tuz")
# db.insert_into("mastava", "Guruch, Yog', Gosht, Sabzi")
db.view_data()
db.view_data2()