class Menu:
    def __init__(self):
        pass

    def menu1(self):
        print("-----------------------------------------")
        print("1.Utiliser l'application")
        print("2.Réinitialiser la base de données")
        print("3.Quitter l'application")
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_application(self):
        print("-----------------------------------------")
        print("1.Afficher les catégories")
        print("2.Afficher les favoris")
        print("3.Quitter l'application")
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_categories(self, categories):
        print("-----------------------------------------")
        for cat in categories:
            print(cat[0], '.', cat[1])
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_products(self, products):
        print("-----------------------------------------")
        for product in products:
            print(product[0], '-', product[1], '- nutriscore=', product[2])
        print("-----------------------------------------")
        choice = int(input())
        return choice

    def menu_suggest(self, suggest):
        print("-----------------------------------------")
        print(suggest[0], '-', suggest[1], 'disponible dans le magasin: ', suggest[4], 'ou sur ', suggest[3])
        print("-----------------------------------------")
        choice = int(input())
        return choice
    def menu_favorites(self, favorites):
        print("-----------------------------------------")

        print("-----------------------------------------")
