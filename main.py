import requests
from Produits import *
from constants import *
from api_requests import *
from create_database import *
import mysql.connector
from motdepasse import *
import sys

password = passwordGF

def logging():
    loop = 1
    while loop:
        choice = int(input("1 - Nouvel utilisateur : Créer la base de données.\n"
                           "2 - Utilisateur existant : Poursuivre. \n"
                           "3 - Quitter le programme. \n"))
        if choice == 1 :
            creating_database()
            print("Base de données créée.")
            filling_database()

        if choice == 2:
            database_logging()
            print("Connecté à la base de données.")
            filling_database()

        if choice == 3:
            loop = 0
            sys.exit(0)


def filling_database():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
    cursor = mydb.cursor()
    loop = 1
    while loop:
        choice = int(input("Mettre à jour les catégories et produits ? 1 == Oui // 2 == Non \n"))

        if choice == 1:
            fill_category()
            get_data("volailles")
            get_data("snacks")
            get_data("Boissons")
            get_data("Conserves")
            get_data("fruits secs")
            mydb.commit()
            cursor.close()
            mydb.close()
            start_menu()

        if choice == 2 :
            start_menu()

def start_menu():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
    cursor = mydb.cursor()
    loop = 1
    while loop:
        choice = int(input("1 - Remplacer un aliment. \n"
                           "2 - Accéder aux aliments substitués. \n"
                           "3 - Quitter le programme. \n"))
        if choice == 3:
            loop = 0
            sys.exit(0)

        if choice == 1:
            display_categories()
            cat_id = (int(input("Choisissez la catégorie: \n")),)

            select_category(cat_id)

            product_id = (int(input("Choissez un produit à substituer: \n")))

            p_selected = Products()
            p_selected.get_product(product_id)
            print("vous avez seléctionné: \n")
            
            p_selected.display()
            print("Ce produit a été substitué par : \n")
            p_selected.substitute()
            
            choice = input("Voulez-vous sauvegarder ce produit ? o / n \n")
            if choice == "o":
                p_selected.save()
            if choice == "n":
                print("Sauvegarde non effectuée")
                
        if choice == 2:
            display_saved()

            
def display_categories():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
    cursor = mydb.cursor()
    cursor.execute(query_display_category)

    for id, name in cursor:
        print(id, ".....", name)

def display_saved():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
    cursor = mydb.cursor()
    cursor.execute(query_display_saved)

    for saved_product_id, saved_product_name, saved_product_grade, saved_substitute_id, saved_substitute_name, saved_substitute_grade in cursor:
        print(saved_product_id, "--", saved_product_name, "--", saved_product_grade, "--", saved_substitute_id, "--", saved_substitute_name, "--", saved_substitute_grade)

def select_category(cat_id):
    mydb = mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBOFF")
    cursor = mydb.cursor()
    cursor.execute(query_select_category, cat_id)
    for id, name in cursor:
        print(id, ".....", name)







if __name__ == "__main__":
    logging()

