import requests
from Produits import *
from constants import *
from api_requests import *
from database import *
import mysql.connector
import sys


usergf = MAIN_USER
hostgf = MAIN_HOST
passwrdgf = MAIN_PASSWORD
databasegf = MAIN_DATABASE


def global_new_user():
    """Global user is a Database class instance"""
    global new_user
    new_user = Database()


def logging():
    """First user screen"""
    loop = 1
    while loop:
        choice = int(input("1 - Nouvel utilisateur : Créer la base de données.\n"
                           "2 - Utilisateur existant : Poursuivre. \n"
                           "3 - Quitter le programme. \n"))
        if choice == 1 :
            Database.create_database()
            global_new_user()
            print("Base de données créée.")
            second_screen()

        if choice == 2:
            Database.loging()
            print("Connecté à la base de données.")
            second_screen()

        if choice == 3:
            loop = 0
            sys.exit(0)


def second_screen():
    """second user screen"""
    mydb = mysql.connector.connect(host=hostgf,user=usergf,password=passwrdgf,database=databasegf)
    cursor = mydb.cursor()
    loop = 1
    global_new_user()
    while loop:
        choice = int(input("Mettre à jour les catégories et produits ? 1 = Oui // 2 = Non \n"))

        if choice == 1:
            get_data()
            mydb.commit()
            cursor.close()
            mydb.close()
            main_screen()

        if choice == 2 :
            main_screen()

def main_screen():
    """main screen"""
    mydb = mysql.connector.connect(host=hostgf,user=usergf,password=passwrdgf,database=databasegf)
    cursor = mydb.cursor()
    global_new_user()
    
    loop = 1
    while loop:
        choice = int(input("1 - Substituer un aliment. \n"
                           "2 - Accéder aux aliments substitués. \n"
                           "3 - Quitter le programme. \n"))
        if choice == 3:
            loop = 0
            sys.exit(0)

        if choice == 1:
            Database.display_categories(new_user)
            cat_id = (int(input("Choisissez la catégorie: \n")),)

            Database.select_category(new_user, cat_id)

            product_id = (int(input("Choissez un produit à substituer: \n")))

            p_selected = Products()
            p_selected.get_product(product_id)
            print("vous avez seléctionné: \n")
            
            p_selected.display()
            print("Ce produit a été substitué par : \n")
            p_selected.substitute()
            
            choice = input("Voulez-vous sauvegarder ce produit ? 1 = Oui // 2 = Non \n")
            if choice == "1":
                p_selected.save()
            if choice == "2":
                print("Sauvegarde non effectuée.")
                
        if choice == 2:
            Database.display_saved(new_user)


if __name__ == "__main__":
    logging()

