import mysql.connector as myc
import os

class Database:
    def create_database(self, database_name):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        kursor = con.cursor()
        kursor.execute(f"Create database if not exists {database_name}")
        con.commit()
        
    def create_table(self, tb_name = "meva", db_name = "BOZOR"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        surov = f"""Create table if not exists {tb_name} (id int primary key auto_increment, Meva_nomi varchar(60) NOT NULL, Meva_narxi int, Meva_turi varchar(60))"""
        kursor.execute(surov)
        con.commit()
        
    def insert_into(self, Meva_nomi, Meva_narxi, Meva_turi):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "BOZOR")
        kursor = con.cursor()
        sql = """Insert into meva (Meva_nomi, Meva_narxi, Meva_turi)  Values(%s,%s,%s)"""
        value = (Meva_nomi, Meva_narxi, Meva_turi)
        kursor.execute(sql, value)
        con.commit()
        
    def view_data(self):
        con = myc.connect(host="localhost", username="root", password="root", database="BOZOR")
        kursor = con.cursor()

        sql = """DELETE n1 FROM meva n1, meva n2 WHERE n1.id > n2.id and 
            n1.Meva_nomi = n2.Meva_nomi and n1.Meva_narxi = n2.Meva_narxi 
            and n1.Meva_turi = n2.Meva_turi"""
        kursor.execute(sql)
        
        sql = """SELECT * FROM meva"""
        kursor.execute(sql)
        data = kursor.fetchall()

        for x in data:
            print(f"id:    {x[0]}\n")
            print(f"Meva_nomi:     {x[1]}\n")
            print(f"Meva_narxi:     {x[2]}")
            print(f"Meva_turi:      {x[3]}")
            print("__" * 25)
            print("\n")

        con.commit()
        con.close()
    
    
    def qimmat(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "BOZOR")
        kursor = con.cursor()
        
        sql = """SELECT * FROM meva ORDER BY Meva_narxi"""
        kursor.execute(sql)
        data = kursor.fetchmany(5)
        data = kursor.fetchall()
        
        for x in data:
            print(f"id:    {x[0]}\n")
            print(f"Meva_nomi:     {x[1]}\n")
            print(f"Meva_narxi:     {x[2]}")
            print(f"Meva_turi:      {x[3]}")
            print("__" * 25)
            print("\n")
        
        con.commit()

        
        
        
db = Database()

# db.create_database("BOZOR")
# db.create_table("meva")
# db.insert_into("Olma", 10000, "Rosales")
# db.insert_into("Anor", 20000, "Red")
# db.insert_into("Olma", 10000, "Rosales")
# db.insert_into("Shaftoli", 40000, "Red")
# db.insert_into("Banan", 10000, "Yellow")
# db.insert_into("Uzum", 6000, "Rosales")
# db.insert_into("Anjir", 35000, "Yellow")
# db.insert_into("Gilos", 45000, "Red")
# db.insert_into("Uzum", 6000, "Rosales")
# db.insert_into("Banan", 10000, "Yellow")

db.view_data()
db.qimmat()