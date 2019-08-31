import mysql.connector
from constants import *


offfile = file
usergf = main_user
hostgf = main_host
passwrdgf = passwordGF
databasegf = main_database

def database_logging():
    mydb = mysql.connector.connect(
        host=hostgf,
        user=usergf,
        password=passwrdgf,
        database=databasegf,
        )

def creating_database():
    mydb = mysql.connector.connect(
        host=hostgf,
        user=usergf,
        password=passwrdgf
        )
    cursor = mydb.cursor()
    sql = open(offfile).read()
    cursor.execute(sql)

if __name__ == "__main__":
    database_logging()


