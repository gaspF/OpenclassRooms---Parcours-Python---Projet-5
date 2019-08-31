from motdepasse import *
import mysql.connector 

# login parameters
main_user = "root"
main_database = "DBOFF"
main_password = passwordGF
main_host = "localhost"
file = "DBOFF.sql"


# MYSQL Querys

add_data = ("INSERT INTO PRODUCT"
            "(product_name, nutrition_grade, product_url, product_store, category_name)"
            "VALUES (%s, %s, %s, %s, %s)")

add_cat_data = ("INSERT INTO CATEGORY"
                "(category_name)"
                "VALUES (%s)")

query_display_category = ("SELECT id, category_name from Category")

query_select_category = ("SELECT Product.id, Product.product_name from Product"
                         " INNER JOIN Category"
                         " ON Product.category_name = Category.category_name"
                         " WHERE Category.id = %s")

query_create_select_product = ("SELECT Product.id, Product.product_name, Product.category_name, Product.nutrition_grade, Product.product_url, Product.category_id from Product"
                               " WHERE Product.id = %s")

query_better_nutrition_grade = ("SELECT * FROM product"
                               "WHERE nutrition_grade < %s"
                                "AND category_id = %s")


query_save = ("INSERT INTO SUBSTITUTE"
              "(saved_product_id, saved_product_name, saved_product_grade, saved_substitute_id, saved_substitute_name, saved_substitute_grade)"
              "VALUES (%s, %s, %s, %s, %s, %s)")

query_display_saved = ("SELECT saved_product_id, saved_product_name, saved_product_grade, saved_substitute_id, saved_substitute_name, saved_substitute_grade FROM substitute")
