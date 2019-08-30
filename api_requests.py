import requests
from Produits import *
from create_database import *
import mysql.connector

def get_data(category):

    main_url = "https://fr.openfoodfacts.org/categorie"
    print("Téléchargement en cours")
    nb_page = 1
    file_type = "json"

    url = "{}/{}/{}.{}".format(main_url, category, nb_page, file_type)

    r = requests.get(url)
    products = r.json()
    
    count = products["count"]
    loop = 4

    while loop > 0:
        url = "{}/{}/{}.{}".format(main_url, category, nb_page, file_type)
        
        r = requests.get(url)
        products = r.json()
        
        product_name = ""
        product_url = ""
        nutrition_grade = ""
        product_store = ""
        category_name = ""
        
        product = Products()
        for p in products["products"]:

            try:
                product_name = p["product_name_fr"]
                nutrition_grade = p["nutrition_grades"]
                product_url = p["url"]
                product_store = p["stores"]
                category_name = category

            except KeyError:
                pass

            product.add(product_name, nutrition_grade, product_url, product_store, category_name)

        nb_page += 1
        loop -= 1

def fill_category():
    main_url = "https://fr.openfoodfacts.org/categories.json"
    
    r = requests.get(main_url)
    categories = r.json()
    category_name = ""
    categorie = Category()
    nbr = 100
    print("téléchargement de ", nbr, "catégories")

    for c in range(nbr):
        category_name = categories["tags"][c]["name"]
        categorie.add(category_name)

    

        
        

    
