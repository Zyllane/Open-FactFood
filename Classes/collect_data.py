import sys
import requests
from Classes.constants import CATEGORY,CATEGORY_URL
from Classes.sql import Sql

class CollectData:
    """
    Use to create an url to parse. Then
    to insert data into sql db
    """

    def __init__(self):  # url is 'https://fr.openfoodfacts.org/categories/'
        print("Vous etes ici")
        self.database = Sql()

    def create_url(self, category):
        """
        create new url to parse with category in paramter
        """
        print("generate url")
        self.url = self.base_url + str(category)
        print("Url {} is created".format(self.url))
        return category  # return to put him in parameter of function create_database

    def create_categories(self):
        for category in CATEGORY:
            id = self.database.create_new_category(category)
            self.create_products(category, id)

    def create_products(self, category_name, category_id):
        category_url = CATEGORY_URL + category_name + ".json"
        request = requests.get(category_url)
        data = request.json()
        for product in data["products"]:
            print(product["product_name"])
            self.database.create_new_product(product["product_name"], product.get("nutriscore_grade","X"), category_id)
