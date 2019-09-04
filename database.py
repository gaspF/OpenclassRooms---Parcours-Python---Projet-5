import mysql.connector

from constants import *
from api_requests import *


offfile = FILE
usergf = MAIN_USER
hostgf = MAIN_HOST
passwrdgf = MAIN_PASSWORD
databasegf = MAIN_DATABASE

class Database:
    """A class that allow user to connect to the database or creating a new one from the database file, with
    two staticmethor, or query database in order to display required data."""
    db_user=usergf
    db_password=passwrdgf
    db_host=hostgf
    db_name=databasegf
    db_file=offfile

    @staticmethod
    def loging():
        """Staticmethod for login"""
        mydb = mysql.connector.connect(host=Database.db_host,
                                       user=Database.db_user,
                                       password=Database.db_password,
                                       database=Database.db_name
                                       )

    @staticmethod
    def create_database():
        """Staticmethod for creating database"""
        mydb = mysql.connector.connect(host=Database.db_host,
                                       user=Database.db_user,
                                       password=Database.db_password,
                                       )
        cursor = mydb.cursor()
        sql = open(offfile).read()
        cursor.execute(sql)
        
    def __init__(self):
        """Setting Cursor's parameters into class constructor"""
        MySQLConfig = {'user':usergf,'password':passwordGF,'host':hostgf,'database':databasegf}
        self.mydb = mysql.connector.connect(**MySQLConfig)
        self.cursor = self.mydb.cursor()

    def display_categories(self):
        """Method used for displaying categories"""
        self.cursor.execute(QUERY_DISPLAY_CATEGORY)
        for id, name in self.cursor:
            print(id, ".....", name)

    def display_saved(self):
        """Method used for displaying substitute table"""
        self.cursor.execute(QUERY_DISPLAY_SAVED)
        for saved_product_id, saved_product_name, saved_product_grade, saved_substitute_id, saved_substitute_name, \
            saved_substitute_grade in self.cursor:
            print("Produit à substituer :", "\n", "ID :", saved_product_id, "...", "Nom du produit :",
                  saved_product_name, "...", "Grade nutritionnel :", saved_product_grade, "\n",
                  "Produit de substitution :", "\n", "ID :", saved_substitute_id, "...", "Nom du produit :",
                  saved_substitute_name, "...", "Grade nutritionnel :", saved_substitute_grade, "\n")

    def select_category(self, cat_id):
        """Method used displaying all products from a selected category"""
        self.cursor.execute(QUERY_SELECT_CATEGORY, cat_id)
        for id, name in self.cursor:
            print(id, ".....", name)

    def db_cursor_closed(self):
        self.cursor.close()
        self.mydb.close()



