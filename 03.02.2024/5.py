import mysql.connector as myc
import os

class Database:
    def create_database(self, database_name):
        con = myc.connect(host = "localhost", username = "root", password = "root")
        cursor = con.cursor()
        cursor.execute(f"Create database if not exists {database_name}")
        con.commit()
        
    def create_table(self, tb_name = "employee", db_name = "EMPLOYEE"):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = f"{db_name}")
        cursor = con.cursor()
        sorov = f"""Create table if not exists {tb_name} (EMPLOYEE_ID int, FIRST_NAME VARCHAR(60), LAST_NAME  VARCHAR(60), EMAIL VARCHAR(60), PHONE_NUMBER VARCHAR(60), HIRE_DATE date, JOB_ID VARCHAR(60), SALARY int, COMMISSION_PCT int, MANAGER_ID int, DEPARTAMENT_ID int)"""
        cursor.execute(sorov)
        con.commit()
        
    def insert_into(self, EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTAMENT_ID):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "EMPLOYEE")
        cursor = con.cursor()
        sql = """Insert into employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTAMENT_ID) Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        value = (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTAMENT_ID)
        cursor.execute(sql, value)
        con.commit()
    
    def bolim(self):
        con = myc.connect(host = "localhost", username = "root", password = "root", database = "EMPLOYEE")
        cursor = con.cursor()
        cursor.execute("Select FIRST_NAME, LAST_NAME, SALARY, DEPARTAMENT_ID FROM employee where DEPARTAMENT_ID = 40")
        data = cursor.fetchall()
        for i in range(0, len(data)):
            print(data[i])
            print("-"*35)
 
        

ob = Database()
ob.create_database("EMPLOYEE")
ob.bolim()
# ob.create_table("employee")

# ob.insert_into(100, "Stecen", "King", "SKING", "515.123.4567", "2003-06-17", "AD_PRES", 24000, 0, 0, 90)

# ob.insert_into(101, "Neena", "Kochhar", "NKOCHHAR", "515.123.4568", "2005-09-21", "AD_VP", 17000, 0, 100, 40)

# ob.insert_into(102, "Lex", "De Haan", "LDEHAAN", "515.123.4569", "2001-01-13", "IT_PROG", 17000, 0, 100, 90)

# ob.insert_into(103, "Alexander", "Hunold", "AHUNOLD", "590.423.4567", "2006-01-03", "IT_PROG", 9000, 0, 102, 60)

# ob.insert_into(104, "Bruce", "Ernst", "BERNST", "590.423.4568", "2007-05-21", "IT_PROG", 6000, 0, 103, 40)

# ob.insert_into(105, "David", "Austin", "DAUSTIN", "590.423.4569", "2005-06-25", "IT_PROG", 4800, 0, 103, 60)

# ob.insert_into(106, "Valli", "Pataballa", "VPATABAL", "590.423.4560", "2006-02-05", "IT_PROG", 4800, 0, 103, 40)

# ob.insert_into(107, "Diana", "Lorentz", "DLORENTZ", "590.423.5567", "2007-02-07", "IT_PROG", 4200, 0, 103, 60)
