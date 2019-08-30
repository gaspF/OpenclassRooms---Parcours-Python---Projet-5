import mysql.connector
from constants import *
from motdepasse import *

password = passwordGF

class Products():

    def __init__(self):
        self.product_name = ""
        self.nutrition_grade = ""
        self.product_url = ""
        self.id = 0
        self.product_store = ""
        self.category_name = ""
        self.substitute_id = 0
        self.substitute_name = ""
        self.substitute_grade = ""
        self.category_id = 0

    def add(self, product_name, nutrition_grade, product_url, product_store, category_name):
        self.product_name = product_name
        self.nutrition_grade = nutrition_grade
        self.product_url = product_url
        self.product_store = product_store
        self.category_name = category_name

        add_product = (self.product_name, self.nutrition_grade, self.product_url, self.product_store, self.category_name)


        try:
            mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
            cursor = mydb.cursor()
            cursor.execute(add_data, add_product)
            mydb.commit(),
            cursor.close()
            mydb.close()

        except mysql.connector.errors.IntegrityError:
            pass

    def get_product(self, product_id):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
        cursor = mydb.cursor() 
        cursor.execute(query_create_select_product, (product_id,))

        for id, product_name, category_name, nutrition_grade, product_url, category_id in cursor:
            self.id = id
            self.product_name = product_name
            self.nutrition_grade = nutrition_grade
            self.category_name = category_name
            self.category_id = category_id

        return self.nutrition_grade
        
    def display(self):
        print(" Aliment {} de la catégorie {} \n\n"
              "Son nutriscore est de {} \n\n"
              .format(self.product_name, self.category_name, self.nutrition_grade))
        

    def substitute(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
        cursor = mydb.cursor()
        cursor.execute("""SELECT * FROM product
WHERE nutrition_grade < %s AND category_name = %s""", (self.nutrition_grade, self.category_name))
        row = cursor.fetchone()
        
        for element in row:
            print(element, end = ' -- ')
            self.substitute_id = row[0]
            self.substitute_name = row[1]
            self.substitute_grade = row[4]
            
        return self.substitute_id, self.substitute_name, self.substitute_grade

    def save(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
        cursor = mydb.cursor()
        add_element = (self.id, self.product_name, self.nutrition_grade, self.substitute_id, self.substitute_name, self.substitute_grade)
        cursor.execute(query_save, add_element)
        mydb.commit()

        

class Category():

    def __init__(self):
        self.category_name = ""
        self.id = 0

    def add(self, category_name):
        self.category_name = category_name

        add_category = (self.category_name)

        try:
            mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
            cursor = mydb.cursor()
            cursor.execute(add_cat_data, (add_category,))
            mydb.commit()
            cursor.close()
            mydb.close()

        except mysql.connector.errors.IntegrityError:
            pass
