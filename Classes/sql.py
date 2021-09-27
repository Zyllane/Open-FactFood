import mysql.connector


class Sql:
    """
    This class manages all interactions with db sql
    """

    def __init__(self, user, password, host, databse):
        self.user = str(user)
        self.password = str(password)
        self.host = str(host)
        self.database = str(databse)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ocp5"
)

mycursor = mydb.cursor()

# Reset Database + Création Database (pour reboot) #

mycursor.execute("DROP DATABASE IF exists mydatabase")
mycursor.execute("CREATE DATABASE IF NOT exists mydatabase")
mycursor.execute("USE mydatabase")
# Création des deux tables  #
mycursor.execute("CREATE TABLE IF NOT exists Categories(id_categories INT PRIMARY KEY NOT NULL AUTO_INCREMENT"
                 ", nom VARCHAR(40))")
mycursor.execute("CREATE TABLE IF NOT exists Produits("
                 "product_id VARCHAR(40),"
                 " url VARCHAR(40),"
                 "nom VARCHAR(255) NOT NULL, "
                 "grade ENUM('A','B','C','D','E') NOT NULL,"
                 "categorie INT, magasin VARCHAR(40), image VARCHAR(40),"
                 "PRIMARY KEY (product_id))")
