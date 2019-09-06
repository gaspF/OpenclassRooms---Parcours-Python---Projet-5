import requests
from Product import *
import mysql.connector


def get_data():
    """Get data (categories and products from OpenFoodFacts"""
    main_url = "https://fr.openfoodfacts.org/categories.json"
    r = requests.get(main_url)
    categories = r.json()
    category_name = ""
    categorie = Category()
    nbr = 15

    print("Téléchargement de ", nbr, "catégories")

    for c in range(nbr):
        category_name_url = categories["tags"][c]["name"]
        categorie.add(category_name_url)
        print("Téléchargement des produits de la catégorie", category_name_url)

        for page in range(4):
            product_url = categories["tags"][c]["url"] + "/" + str(page + 1) + ".json"
            pr = requests.get(product_url)
            products = pr.json()

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
                    category_name = category_name_url

                except KeyError:
                    pass

                product.add(
                    product_name,
                    nutrition_grade,
                    product_url,
                    product_store,
                    category_name,
                )

            product.cursor_closed()
