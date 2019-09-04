import mysql.connector
from constants import *
from motdepasse import *

usergf = MAIN_USER
hostgf = MAIN_HOST
passwrdgf = MAIN_PASSWORD
databasegf = MAIN_DATABASE


class Products:
    """A class that allows program to add products to database, or as well display or substitute them"""

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
        MySQLConfig = {
            "user": usergf,
            "password": passwordGF,
            "host": hostgf,
            "database": databasegf,
        }
        self.mydb = mysql.connector.connect(**MySQLConfig)
        self.cursor = self.mydb.cursor(buffered=True)

    def add(
        self, product_name, nutrition_grade, product_url, product_store, category_name
    ):
        """Add product to database"""
        self.product_name = product_name
        self.nutrition_grade = nutrition_grade
        self.product_url = product_url
        self.product_store = product_store
        self.category_name = category_name

        add_product = (
            self.product_name,
            self.nutrition_grade,
            self.product_url,
            self.product_store,
            self.category_name,
        )

        try:
            self.cursor.execute(ADD_DATA, add_product)
            self.mydb.commit()

        except mysql.connector.errors.IntegrityError:
            pass

    def cursor_closed(self):
        self.cursor.close()
        self.mydb.close()

    def get_product(self, product_id):
        """Method that catchs a product selected by user, in order to get it's nutrition grade, or even display
         or save it later into substitute table."""
        self.cursor.execute(QUERY_CREATE_SELECT_PRODUCT, (product_id,))

        for (
            id,
            product_name,
            category_name,
            nutrition_grade,
            product_url,
            category_id,
        ) in self.cursor:
            self.id = id
            self.product_name = product_name
            self.nutrition_grade = nutrition_grade
            self.category_name = category_name
            self.category_id = category_id

        return self.nutrition_grade

    def display(self):
        """Method used for displaying the catched product"""
        print(
            " Aliment {} de la catégorie {} \n\n"
            "Son nutriscore est de {} \n\n".format(
                self.product_name, self.category_name, self.nutrition_grade
            )
        )

    def substitute(self):
        """Method that queries the database to find a better nutrition's grade product than the selected one"""
        self.cursor.execute(
            """SELECT * FROM product WHERE nutrition_grade < %s AND category_name = %s""",
            (self.nutrition_grade, self.category_name),
        )
        row = self.cursor.fetchone()

        for element in row:
            print(element, end=" -- ")
            self.substitute_id = row[0]
            self.substitute_name = row[1]
            self.substitute_grade = row[4]

        return self.substitute_id, self.substitute_name, self.substitute_grade

    def save(self):
        """Method that saves the catched product and the substitute product into the substitute table"""
        add_element = (
            self.id,
            self.product_name,
            self.nutrition_grade,
            self.substitute_id,
            self.substitute_name,
            self.substitute_grade,
        )
        self.cursor.execute(QUERY_SAVE, add_element)
        self.mydb.commit()


class Category:
    """A class that allows program to add categories to database"""

    def __init__(self):
        self.category_name = ""
        self.id = 0

    def add(self, category_name):
        self.category_name = category_name

        add_category = self.category_name

        try:
            mydb = mysql.connector.connect(
                host=hostgf, user=usergf, password=passwrdgf, database=databasegf
            )
            cursor = mydb.cursor()
            cursor.execute(ADD_CAT_DATA, (add_category,))
            mydb.commit()
            cursor.close()
            mydb.close()

        except mysql.connector.errors.IntegrityError:
            pass
