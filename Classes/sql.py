import mysql.connector
from Classes.constants import CREDENTIALS


class Sql:
    """
    This class manages all interactions with the db
    """


    def __init__(self):
        """
        Constructor of the class, which initialise the connection to the db
        """
        self.mydb = mysql.connector.connect(
            host=CREDENTIALS["host"],
            user=CREDENTIALS["username"],
            passwd=CREDENTIALS["password"],
            database=CREDENTIALS["dbname"]
        )
        self.mycursor = self.mydb.cursor(buffered=True)
        """self.reset_database()"""

    def create_new_category(self, name):
        """
        Create a new entry in the CATEGORIES table
        """
        query = "INSERT INTO Categories(nom) VALUES (%s)"
        self.mycursor.execute(query, (name,))
        self.mydb.commit()
        return self.mycursor.lastrowid

    def create_new_product(self, name, grade, url, stores, id_category):
        """
        Create a new entry in the PRODUCT table
        """
        query = "INSERT INTO Products(nom, grade, url, stores, id_categories) VALUES (%s, %s, %s, %s, %s)"
        self.mycursor.execute(query, (name, grade, url, stores, id_category,))
        self.mydb.commit()

    def create_new_substitute(self, id_product, id_substitute_product):
        """
        Create a new entry in the SUBSTITUTE table
        """
        query = "INSERT INTO Substitute(id_product, id_substitute_product) VALUES (%s, %s)"
        self.mycursor.execute(query, (id_product, id_substitute_product,))
        self.mydb.commit()

    def suggest(self, id_categories):
        """
        Return the first product with "a" grade in the same chosen product category
        """
        query = "SELECT * FROM products WHERE grade = 'a' AND id_categories = %s "
        self.mycursor.execute(query, (id_categories,))
        return self.mycursor.fetchone()

    def get_product_name_by_id(self, id_product):
        """
        Return the name of the product for the given id
        """
        query = "SELECT nom FROM products WHERE id_product = %s"
        self.mycursor.execute(query, (id_product,))
        return self.mycursor.fetchone()

    def get_all_substitute(self):
        """
        Return all substitute from the table SUBSTITUTE
        """
        query = "SELECT * FROM substitute "
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def suggest_all_categories(self):
        """
        Return all the products where grade = "a"
        """
        query = "SELECT * FROM products WHERE grade = 'a'"
        self.mycursor.execute(query)
        return self.mycursor.fetchone()

    def get_categories(self):
        """
        Return all categories in the table CATEGORIES
        """
        query = "SELECT * FROM categories"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def get_products_by_cat(self, id_categories):
        """
        Return all product for the given category id
        """
        query = "SELECT * FROM products WHERE id_categories = %s"
        self.mycursor.execute(query, (id_categories,))
        return self.mycursor.fetchall()

    def reset_database(self):
        """
        Drop and reset the database from scratch by creating the 3 tables after deleting them
        """
        # Reset Database + Création Database (pour reboot) #

        self.mycursor.execute("DROP DATABASE IF exists mydatabase")
        self.mycursor.execute("CREATE DATABASE IF NOT exists mydatabase")
        self.mycursor.execute("USE mydatabase")
        # Création des deux tables  #
        self.mycursor.execute(
            "CREATE TABLE IF NOT exists Categories(id_categories INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
            "nom VARCHAR(40))")
        self.mycursor.execute(
            "CREATE TABLE IF NOT exists Products(id_product INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
            "nom VARCHAR(255) NOT NULL, "
            "grade ENUM('a', 'b', 'c', 'd', 'e', 'X') NOT NULL,"
            "url VARCHAR(255),"
            "stores VARCHAR(255),"
            "id_categories INT,"
            "FOREIGN KEY (id_categories) REFERENCES Categories(id_categories))")
        self.mycursor.execute(
            "CREATE TABLE IF NOT exists Substitute(id_substitute INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
            "id_product INT NOT NULL,"
            "id_substitute_product INT NOT NULL,"
            "FOREIGN KEY (id_product) REFERENCES Products(id_product),"
            "FOREIGN KEY (id_substitute_product) REFERENCES Products(id_product))")
