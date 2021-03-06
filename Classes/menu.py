class Menu:
    """
    This class manage all graphical menu for the user view
    """
    def __init__(self):
        """
        default constructor
        """
        pass

    def menu1(self):
        """
        Create the menu 1 design
        """
        print("-----------------------------------------")
        print("1.Utiliser l'application")
        print("2.Réinitialiser la base de données")
        print("3.Quitter l'application")
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_application(self):
        """
        Create the menu application design
        """
        print("-----------------------------------------")
        print("1.Afficher les catégories")
        print("2.Afficher les favoris")
        print("3.Quitter l'application")
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_categories(self, categories):
        """
        Create the menu categories design
        """
        print("-----------------------------------------")
        for cat in categories:
            print(cat[0], '.', cat[1])
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_products(self, products):
        """
        Create the menu products design
        """
        print("-----------------------------------------")
        for product in products:
            print(product[0], '-', product[1], '- nutriscore=', product[2])
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_suggest(self, suggest):
        """
        Create the menu suggest design
        """
        print("-----------------------------------------")
        print(suggest[0], '-', suggest[1], 'disponible dans le magasin: ', suggest[4], 'ou sur ', suggest[3])
        print("Taper le numéro de produit pour le rajouter aux favoris")
        print("Taper n'importe quelle autre touche pour quitter l'application")
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_favorites(self, favorites):
        """
        Create the menu favorites design
        """
        print("-----------------------------------------")
        for fav in favorites:
            print(fav["product_name"], 'a été substitué par ', fav["sub_name"])
        print("-----------------------------------------")
