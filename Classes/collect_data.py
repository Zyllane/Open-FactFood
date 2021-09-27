import sys
import requests

class CollectData:
    """
    Use to create an url to parse. Then
    to insert data into sql db
    """

    def __init__(self, base_url):  # url is 'https://fr.openfoodfacts.org/categories/'
        self.base_url = str(base_url)
        self.url = None
        self.products_list = []
        self.category_number = None

    def create_url(self, category):
        """
        create new url to parse with category in paramter
        """
        print("generate url")
        self.url = self.base_url + str(category)
        print("Url {} is created".format(self.url))
        return category  # return to put him in parameter of function create_database


