import mysql.connector as myc
import os

class Database:
    def create_database(self, database_nama):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        kursor = con.cursor()
        kursor.execute(f"Create database if not exists {database_nama}")
        con.commit()
    
    def create_table1(self, tb_name = "Laptop", db_name = "Techno_db"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (id int primary key auto_increment, model varchar (50) NOT NULL, speed smallint NOT NULL, ram smallint NOT NULL, hd real NOT NULL, price decimal(12,2) NULL, screen smallint NOT NULL)"""
        kursor.execute(sorov)
        con.commit()
    
    def create_table2(self, tb_name = "PC", db_name = "Techno_db"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (id int primary key auto_increment, model varchar (50) NOT NULL, speed smallint NOT NULL, ram smallint NOT NULL, hd real NOT NULL, cd varchar (10) NOT NULL, price decimal(12,2) NULL)"""
        kursor.execute(sorov)
        con.commit()
        
    def create_table3(self, tb_name = "Product", db_name = "Techno_db"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (maker varchar (10) NOT NULL, model varchar (50) NOT NULL PRIMARY KEY, type varchar (50) NOT NULL)"""
        kursor.execute(sorov)
        con.commit()
        
    def create_table4(self, tb_name = "Printer", db_name = "Techno_db"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        kursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (id int primary key auto_increment, model varchar (50) NOT NULL, color char (1) NOT NULL, type varchar (10) NOT NULL, price decimal(12,2) NULL)"""
        kursor.execute(sorov)
        con.commit()
        
    def insert_into1(self, model, speed, ram, hd, price, screen):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Insert into Laptop (model, speed, ram, hd, price, screen)  Values(%s, %s, %s, %s, %s, %s)"""
        value = (model, speed, ram, hd, price, screen)
        kursor.execute(sql, value)
        con.commit()
    
    def insert_into2(self, model, speed, ram, hd, cd, price):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Insert into PC (model, speed, ram, hd, cd, price)  Values(%s, %s, %s, %s, %s, %s)"""
        value = (model, speed, ram, hd, cd, price)
        kursor.execute(sql, value)
        con.commit()
    
    def insert_into3(self, maker, model, type):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Insert into Product (maker, model, type)  Values(%s, %s, %s)"""
        value = (maker, model, type)
        kursor.execute(sql, value)
        con.commit()
        
    def insert_into4(self, model, color, type, price):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Insert into Printer (model, color, type, price)  Values(%s, %s, %s, %s)"""
        value = (model, color, type, price)
        kursor.execute(sql, value)
        con.commit()
    
        # 1 - SHART _____________________________________
    def tekshir1(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Select t1.model, t2.speed, t2.ram, t2.hd, t2.cd, t2.price FROM Product as t1 INNER JOIN PC as t2 ON t1.model = t2.model"""
        kursor.execute(sql)
        data = kursor.fetchall()
        print("\n                    1 - SHART\n")
        for row in data:
            print("-"*50)
            print(row)
            
        con.commit()
        
    def tekshir2(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Select t1.model, t2.speed, t2.ram, t2.hd, t2.price, t2.screen FROM Product as t1 INNER JOIN Laptop as t2 ON t1.model = t2.model"""
        kursor.execute(sql)
        data = kursor.fetchall()
        print("\n                    2 - SHART\n")
        for row in data:
            print("-"*50)
            print(row)
            
        con.commit()
        
    def tekshir3(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Select t1.model, t2.color, t2.type, t2.price FROM Product as t1 INNER JOIN Printer as t2 ON t1.model = t2.model"""
        kursor.execute(sql)
        data = kursor.fetchall()
        print("\n                    3 - SHART\n")
        for row in data:
            print("-"*50)
            print(row)
            
        con.commit()
        
    def tekshir4(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Select t1.maker, t2.model, t2.price FROM Product as t1 INNER JOIN Printer as t2 ON t1.model = t2.model where t2.color = "y" """
        kursor.execute(sql)
        data = kursor.fetchall()
        print("\n                    4 - SHART\n")
        for row in data:
            print("-"*50)
            print(row)
            
        con.commit()
        
    def tekshir5(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        kursor = con.cursor()
        sql = """Select sum(t2.price) / count(t2.id) FROM Product as t1 INNER JOIN PC  t2 ON t1.model = t2.model where t1.maker = "A" """
        kursor.execute(sql)
        data = kursor.fetchall()
        print("\n                    5 - SHART\n")
        for row in data:
            print("-"*50)
            print(row)

        con.commit()
        
    def tekshir6(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        cursor = con.cursor()
        sql = """Select distinct t1.maker FROM Product as t1 INNER JOIN PC as t2 ON t1.model = t2.model where t2.speed > 450"""
        cursor.execute(sql)
        data = cursor.fetchall()
        print("\n                    6 - SHART\n")
        for row in data:
            print("-"*50)
            print(row)
            
        con.commit()
        
    def tekshir7(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "Techno_db")
        cursor = con.cursor()
        sql = """Select t1.maker, max(t2.price) FROM Product as t1 INNER JOIN PC as t2 ON t1.model = t2.model and t1.type = "PC" group by t1.maker"""
        cursor.execute(sql)
        data = cursor.fetchall()
        print("\n                    7 - SHART\n")
        for row in data:
            print("-"*50)
            print(row)
            
        con.commit()



        
db = Database()
# db.create_database("Techno_db")
# db.create_table1("Laptop")
# db.create_table2("PC")
# db.create_table3("Product")
# db.create_table4("Printer")

# db.insert_into1('1298', 350, 32, 4, '700', 11)
# db.insert_into1('1321', 500, 64, 8, '970', 12)
# db.insert_into1('1750', 750, 128, 12, '1200', 14)
# db.insert_into1('1298', 600, 64, 10, '1050', 15)
# db.insert_into1('1752', 750, 128, 10, '1150', 14)
# db.insert_into1('1298', 450, 64, 10, '950', 12)

# db.insert_into2('1232',500,64,5,'12x','600')
# db.insert_into2('1121',750,128,14,'40x','850')
# db.insert_into2('1233',500,64,5,'12x','600')
# db.insert_into2('1121',600,128,14,'40x','850')
# db.insert_into2('1121',600,128,8,'40x','850')
# db.insert_into2('1233',750,128,20,'50x','950')
# db.insert_into2('1232',500,32,10,'12x','400')
# db.insert_into2('1232',450,64,8,'24x','350')
# db.insert_into2('1232',450,32,10,'24x','350')
# db.insert_into2('1260',500,32,10,'12x','350')
# db.insert_into2('1233',900,128,40,'40x','980')
# db.insert_into2('1233',800,128,20,'50x','970')

# db.insert_into3('B','1121','PC')
# db.insert_into3('A','1232','PC')
# db.insert_into3('A','1233','PC')
# db.insert_into3('E','1260','PC')
# db.insert_into3('A','1276','Printer')
# db.insert_into3('D','1288','Printer')
# db.insert_into3('A','1298','Laptop')
# db.insert_into3('C','1321','Laptop')
# db.insert_into3('A','1401','Printer')
# db.insert_into3('A','1408','Printer')
# db.insert_into3('D','1433','Printer')
# db.insert_into3('E','1434','Printer')
# db.insert_into3('B','1750','Laptop')
# db.insert_into3('A','1752','Laptop')
# db.insert_into3('E','2113','PC')
# db.insert_into3('E','2112','PC')

# db.insert_into4('1276','n','Laser','400')
# db.insert_into4('1433','y','Jet','270')
# db.insert_into4('1434','y','Jet','290')
# db.insert_into4('1401','n','Matrix','150')
# db.insert_into4('1408','n','Matrix','270')
# db.insert_into4('1288','n','Laser','400')

db.tekshir1()
db.tekshir2()
db.tekshir3()
db.tekshir4()
db.tekshir5()
db.tekshir6()
db.tekshir7()
