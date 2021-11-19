import sys
import requests
from Classes.constants import CATEGORY, CATEGORY_URL
from Classes.sql import Sql
from Classes.menu import Menu


class CollectData:
    """
    Use to create an url to parse. Then
    to insert data into sql db
    """

    def __init__(self):  # url is 'https://fr.openfoodfacts.org/categories/'
        print("Vous etes ici")
        self.database = Sql()
        self.menu = Menu()

    def create_categories(self):
        for category in CATEGORY:
            id = self.database.create_new_category(category)
            self.create_products(category, id)

    def create_products(self, category_name, category_id):
        category_url = CATEGORY_URL + category_name + ".json"
        request = requests.get(category_url)
        data = request.json()
        for product in data["products"]:
            self.database.create_new_product(product["product_name"],
                                             product.get("nutriscore_grade", "X"),
                                             product["url"],
                                             product.get("stores", ""),
                                             category_id)

    def suggest_better_product(self, id_category, grade, name):
        if grade != "a":
            suggestions = self.database.suggest(id_category, )
            if len(suggestions) == 0:
                self.database.suggest_all_categories()
        else:
            print(name, " possède déjà le grade 'a'")

    def display_menu1(self):
        choice = self.menu.menu1()
        if choice == 1:
            self.display_menu_application()
        elif choice == 2:
            self.database.reset_database()
            print("Veuiller patienter")
            self.create_categories()
            print('La base de données a été réinitialisée')
            self.display_menu1()
        elif choice == 3:
            print('Vous quitter l\'application')
            return 0

    def display_menu_application(self):
        choice = self.menu.menu_application()
        if choice == 1:
            self.display_menu_categories()

    def display_menu_categories(self):
        categories = self.database.get_categories()
        choice = self.menu.menu_categories(categories)
        self.display_menu_products(choice)

    def display_menu_products(self, id_categories):
        products = self.database.get_products_by_cat(id_categories)
        choice = self.menu.menu_products(products)
        self.display_menu_suggest(id_categories)

    def display_menu_suggest(self, id_categories):
        suggest = self.database.suggest(id_categories)
        choice = self.menu.menu_suggest(suggest)
