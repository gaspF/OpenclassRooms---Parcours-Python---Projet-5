import mysql.connector
from motdepasse import *


file = "DBOFF.sql"
password = passwordGF

def database_logging():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="DBOFF"
        )

def creating_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password
        )
    cursor = mydb.cursor()
    sql = open(file).read()
    cursor.execute(sql)

if __name__ == "__main__":
    database_logging()


