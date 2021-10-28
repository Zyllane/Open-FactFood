import mysql.connector
from Classes.constants import CREDENTIALS

class Sql:
    """
    This class manages all interactions with db sql
    """

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=CREDENTIALS["host"],
            user=CREDENTIALS["username"],
            passwd=CREDENTIALS["password"],
            database=CREDENTIALS["dbname"]
        )
        self.mycursor = self.mydb.cursor()
        self.reset_database()

    def create_new_category(self, name):
        print("creating new category ", name)
        query = "INSERT INTO Categories(nom) VALUES (%s)"
        self.mycursor.execute(query, (name,))
        self.mydb.commit()


    def reset_database(self):

        # Reset Database + Création Database (pour reboot) #

        self.mycursor.execute("DROP DATABASE IF exists mydatabase")
        self.mycursor.execute("CREATE DATABASE IF NOT exists mydatabase")
        self.mycursor.execute("USE mydatabase")
        # Création des deux tables  #
        self.mycursor.execute("CREATE TABLE IF NOT exists Categories(id_categories INT PRIMARY KEY NOT NULL AUTO_INCREMENT"
                         ", nom VARCHAR(40))")
        self.mycursor.execute("CREATE TABLE IF NOT exists Produits("
                         "product_id VARCHAR(40),"
                         " url VARCHAR(40),"
                         "nom VARCHAR(255) NOT NULL, "
                         "grade ENUM('A','B','C','D','E') NOT NULL,"
                         "categorie INT, magasin VARCHAR(40), image VARCHAR(40),"
                         "PRIMARY KEY (product_id))")

