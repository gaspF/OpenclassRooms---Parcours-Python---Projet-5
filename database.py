import mysql.connector

from constants import *
from api_requests import *


offfile = FILE
usergf = MAIN_USER
hostgf = MAIN_HOST
passwrdgf = MAIN_PASSWORD
databasegf = MAIN_DATABASE
""" Régler le pb entre self.mydb et mydb.. Conflit possible entre les deux ?"""

class Database:
    db_user=usergf
    db_password=passwordGF
    db_host=hostgf
    db_name=databasegf
    db_file=offfile

    @staticmethod
    def loging():
        mydb = mysql.connector.connect(host=Database.db_host,
                                       user=Database.db_user,
                                       password=Database.db_password,
                                       database=Database.db_name
                                       )

    @staticmethod
    def create_database():
        mydb = mysql.connector.connect(
            host=Database.db_host,
            user=Database.db_user,
            password=Database.db_password,
            )
        cursor = mydb.cursor()
        sql = open(offfile).read()
        cursor.execute(sql)
        
    def __init__(self):
        MySQLConfig = {'user':usergf,'password':passwordGF,'host':hostgf,'database':databasegf}
        self.mydb = mysql.connector.connect(**MySQLConfig)
        self.cursor = self.mydb.cursor()

    def display_categories(self):
        self.cursor.execute(QUERY_DISPLAY_CATEGORY)
        for id, name in self.cursor:
            print(id, ".....", name)

    def display_saved(self):
        self.cursor.execute(QUERY_DISPLAY_SAVED)
        for saved_product_id, saved_product_name, saved_product_grade, saved_substitute_id, saved_substitute_name, saved_substitute_grade in self.cursor:
            print(saved_product_id, "--", saved_product_name, "--", saved_product_grade, "--", saved_substitute_id, "--", saved_substitute_name, "--", saved_substitute_grade)

    def select_category(self, cat_id):
        self.cursor.execute(QUERY_SELECT_CATEGORY, cat_id)
        for id, name in self.cursor:
            print(id, ".....", name)



