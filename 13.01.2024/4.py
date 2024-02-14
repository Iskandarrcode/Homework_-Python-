import mysql.connector as myc
import os

class Database:
    def create_database(self, database_name):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        kursor = con.cursor()
        kursor.execute(f"create database if not exists {database_name}")
        con.commit()
        
    def create_table(self, tb_name = "Meva", db_name = "MEVA"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        sorov = """Create table if not exists Meva (id Integer primary key auto_increment, nomi varchar(60), narxi int, navi varchar(60))"""
        kursor.execute(sorov)
        con.commit()
        
    def insert_into(self, nomi, narxi, navi):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "MEVA")
        kursor = con.cursor()
        sql = """Insert into Meva (nomi, narxi, navi) Values (%s, %s, %s)"""
        value = (nomi, narxi, navi)
        kursor.execute(sql, value)
        con.commit()
        
    def view_data(self):
        con = myc.connect(host = 'localhost', username = "root", password = "root", database = "MEVA")
        kursor = con.cursor()
        sql = """Select * from Meva"""
        kursor.execute(sql)
        data = kursor.fetchall()
        
        for row in data:
            ls = int(row[2])
            if ls > 10000 and ls < 50000:
                print(row)
        con.commit()
        
        
        
        
        
db = Database()

# db.create_database("MEVA")
# db.create_table("Meva")
# db.insert_into("Olma", 10000, "Rosales")
# db.insert_into("Anor", 20000, "Red")
# db.insert_into("Olma", 10000, "Rosales")
# db.insert_into("Shaftoli", 40000, "Red")
# db.insert_into("Banan", 50000, "Yellow")
# db.insert_into("Uzum", 60000, "Rosales")
# db.insert_into("Anjir", 350000, "Yellow")
# db.insert_into("Gilos", 45000, "Red")
# db.insert_into("Uzum", 60000, "Rosales")
# db.insert_into("Banan", 30000, "Yellow")

db.view_data()