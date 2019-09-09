import requests
from Product import *
from constants import *
from api_requests import *
from database import *
import mysql.connector
import sys


usergf = MAIN_USER
hostgf = MAIN_HOST
passwrdgf = MAIN_PASSWORD
databasegf = MAIN_DATABASE


def logging():
    """First user screen"""
    loop = 1
    while loop:
        choice = int(
            input(
                "1 - Nouvel utilisateur : Créer la base de données.\n"
                "2 - Utilisateur existant : Poursuivre. \n"
                "3 - Quitter le programme. \n"
            )
        )
        if choice == 1:
            Database.create_database()
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
    """Second user screen"""
    loop = 1
    while loop:
        choice = int(
            input("Mettre à jour les catégories et produits ? 1 = Oui // 2 = Non \n")
        )

        if choice == 1:
            get_data()
            main_screen()

        if choice == 2:
            main_screen()


def main_screen():
    """Main user screen"""
    new_user = Database()
    p_selected = Products()
    loop = 1
    while loop:
        choice = int(
            input(
                "1 - Substituer un aliment. \n"
                "2 - Accéder aux aliments substitués. \n"
                "3 - Quitter le programme. \n"
            )
        )
        if choice == 3:
            loop = 0
            sys.exit(0)

        if choice == 1:
            Database.display_categories(new_user)
            cat_id = (int(input("Choisissez la catégorie: \n")),)

            Database.select_category(new_user, cat_id)

            product_id = int(input("Choissez un produit à substituer: \n"))

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
            Database.display_saved(p_selected)


if __name__ == "__main__":
    logging()
