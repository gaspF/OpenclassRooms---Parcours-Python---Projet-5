from motdepasse import *
import mysql.connector 

""" login parameters """

MAIN_USER = "root"
MAIN_DATABASE = "DBOFF"
MAIN_PASSWORD = passwordGF
MAIN_HOST = "localhost"
FILE = "DBOFF.sql"


""" MYSQL Querys """

ADD_DATA = ("INSERT INTO PRODUCT"
            "(product_name, nutrition_grade, product_url, product_store, category_name)"
            "VALUES (%s, %s, %s, %s, %s)")

ADD_CAT_DATA = ("INSERT INTO CATEGORY"
                "(category_name)"
                "VALUES (%s)")

QUERY_DISPLAY_CATEGORY = ("SELECT id, category_name from Category")

QUERY_SELECT_CATEGORY = ("SELECT Product.id, Product.product_name from Product"
                         " INNER JOIN Category"
                         " ON Product.category_name = Category.category_name"
                         " WHERE Category.id = %s")

QUERY_CREATE_SELECT_PRODUCT = ("SELECT Product.id, Product.product_name, Product.category_name, Product.nutrition_grade, Product.product_url, Product.category_id from Product"
                               " WHERE Product.id = %s")

QUERRY_BETTER_NUTRITION_GRADE = ("SELECT * FROM product"
                               "WHERE nutrition_grade < %s"
                                "AND category_id = %s")


QUERY_SAVE = ("INSERT INTO SUBSTITUTE"
              "(saved_product_id, saved_product_name, saved_product_grade, saved_substitute_id, saved_substitute_name, saved_substitute_grade)"
              "VALUES (%s, %s, %s, %s, %s, %s)")

QUERY_DISPLAY_SAVED = ("SELECT saved_product_id, saved_product_name, saved_product_grade, saved_substitute_id, saved_substitute_name, saved_substitute_grade FROM substitute")
