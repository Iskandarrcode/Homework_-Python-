import mysql.connector as myc
import os

class Database:
    def create_database(self, database_name):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        kursor = con.cursor()
        kursor.execute(f"Create database if not exists {database_name}")
        con.commit()
        
    def create_table(self, tb_name = "Aeroport", db_name = "AEROPORT"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        surov = f"""Create table if not exists {tb_name} (id int primary key auto_increment, Samoliyot_turi varchar(60) NOT NULL, Uchish_sanasi date, Uchish_shaxri varchar(60), Qonish_shaxri varchar(60), Uchish_vaqti varchar(60))"""
        kursor.execute(surov)
        con.commit()
        
    def insert_into(self, Samoliyot_turi, Uchish_sanasi, Uchish_shaxri, Qonish_shaxri, Uchish_vaqti):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "AEROPORT")
        kursor = con.cursor()
        sql = """Insert into Aeroport (Samoliyot_turi, Uchish_sanasi, Uchish_shaxri, Qonish_shaxri, Uchish_vaqti)  Values(%s, %s, %s, %s, %s)"""
        value = (Samoliyot_turi, Uchish_sanasi, Uchish_shaxri, Qonish_shaxri, Uchish_vaqti)
        
        kursor.execute(sql, value)
        con.commit()
        
    def view_date(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "AEROPORT")
        kursor = con.cursor()
        sql = """Select * from Aeroport """
        kursor.execute(sql)
        date = kursor.fetchall()
        for row in date:
            st = str(row[2])
            if st[6] == "3" or st[6] == "4" or st[6] == "5":
                print(row)
        con.commit()
        print("\n")
        
        
    def view_date2(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "AEROPORT")
        kursor = con.cursor()
        sql = """Select * from Aeroport """
        kursor.execute(sql)
        date = kursor.fetchall()
        for row in date:
            st = str(row[5])
            st2 = str(row[3])
            if (st[0] == "1" and st[1] == "4") or (st[0] == "1" and st[1] == "5") or (st[0] == "1" and st[1] == "6") or (st[0] == "1" and st[1] == "7") or (st[0] == "1" and st[1] == "8"):
                if st2 == "Toshkent":
                    # O'chirish o'hshamadi shuning uchun print qilib qo'ydim !
                    print(row)
                    
        con.commit()
        
    

        
        
        
db = Database()

# db.create_database("AEROPORT")
# db.create_table("Aeroport")
# db.insert_into("Boyel 100", "2023-3-20", "Uzbekiston", "Duby", "10:30")
# db.insert_into("Boyel 300", "2023-10-11", "Qozogiston", "RUS", "11:30")
# db.insert_into("UZ_Boyel", "2023-11-25", "Uzbekiston", "RUS", "12:00")
# db.insert_into("Boyel 200", "2023-5-5", "Turkiya", "Findlandia", "13:30")
# db.insert_into("Turky 050", "2023-10-28", "Uzbekiston", "Malasia", "12:30")
# db.insert_into("Boyel 500", "2023-10-11", "RUS", "Toshkent", "14:30")
# db.insert_into("Boyel 300", "2023-4-20", "Germanya", "Toshkent", "14:00")
# db.insert_into("New_Boyel", "2023-12-11", "Uzbekiston", "Dagistan", "15:30")
# db.insert_into("Boyel 80", "2023-3-25", "USA", "Toshkent", "16:00")
# db.insert_into("Boyel 100", "2023-10-7", "Uzbekiston", "USA", "17:30")

db.view_date()
db.view_date2()