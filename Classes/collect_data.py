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
        """
        Constructor of the class, which initialise the link with db and the user view (menu)
        """
        self.database = Sql()
        self.menu = Menu()

    def create_categories(self):
        """
        Parse the constant CATEGORY in the constants file to create all categories described in
        Call the create_products method to create the product associated to each category
        """
        for category in CATEGORY:
            id = self.database.create_new_category(category)
            self.create_products(category, id)

    def create_products(self, category_name, category_id):
        """
        Call the Open Food Fact API to retrieve product information and create them in the db
        """
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
        """
        Suggest a better product for a given product of the same category
        If the first product already has a grade = "a",
        then it will inform the user that there is no need to suggest another product
        """
        if grade != "a":
            suggestions = self.database.suggest(id_category, )
            if len(suggestions) == 0:
                self.database.suggest_all_categories()
        else:
            print(name, " poss??de d??j?? le grade 'a'")

    def display_menu1(self):
        """
        Display the first menu in menu.py and allows the user to make choices
        """
        choice = self.menu.menu1()
        if choice == 1:
            self.display_menu_application()
        elif choice == 2:
            self.database.reset_database()
            print("Veuiller patienter")
            self.create_categories()
            print('La base de donn??es a ??t?? r??initialis??e')
            self.display_menu1()
        elif choice == 3:
            print('Vous quitter l\'application')
            return 0

    def display_menu_application(self):
        """
        Display the application menu in menu.py and allows the user to make choices
        """
        choice = self.menu.menu_application()
        if choice == 1:
            self.display_menu_categories()
        elif choice == 2:
            self.display_menu_favorites()
        elif choice == 3:
            print('Vous quitter l\'application')

    def display_menu_categories(self):
        """
        Display the menu categories in menu.py and allows the user to make choices
        """
        categories = self.database.get_categories()
        choice = self.menu.menu_categories(categories)
        self.display_menu_products(choice)

    def display_menu_products(self, id_categories):
        """
        Display the product menu in menu.py and allows the user to make choices
        """
        products = self.database.get_products_by_cat(id_categories)
        choice = self.menu.menu_products(products)
        found = False
        for i in range(len(products)):
            if products[i][2] == "a" and choice == products[i][0]:
                print("Le produit s??lectionn?? poss??de d??j?? un grade=a, pas besoin de suggestion")
                found = True
                break
        if not found:
            self.display_menu_suggest(id_categories, choice)

    def display_menu_suggest(self, id_categories, id_product):
        """
        Display the menu suggest in menu.py and allows the user to make choices
        """
        suggest = self.database.suggest(id_categories)
        choice = self.menu.menu_suggest(suggest)
        self.database.create_new_substitute(id_product, choice)

    def display_menu_favorites(self):
        """
        Display the menu favorites in menu.py and allows the user to make choices
        """
        substitute = self.database.get_all_substitute()
        favorites = []
        for sub in substitute:
            sub_name = self.database.get_product_name_by_id(sub[2])[0]
            product_name = self.database.get_product_name_by_id(sub[1])[0]
            tmp = {
                "sub_name": sub_name,
                "product_name": product_name
            }
            favorites.append(tmp)
        self.menu.menu_favorites(favorites)
