
  

  

*The project aims to create and use a database.

  

The user can choose a food product that is part of the openfoodfact database.

  

Once a product chooses the program will propose a list of food having a superior nutriscore or equivalent.*

  

  

  

## **Prerequisites:**

  

  

- have mysql

  

- create a db named 'mydatabase'

  

  

  

  

  

## Operations:

  

  

**Folder classes:**

  

  

- collect_data.py:

  

	- we pass him the url of openfoodfact

  

	- we collect the data from the API and then we fill the db with it

  

	- it make the menu fonction with the user interaction


  

- sql.py:

  

	- init we pass all the parameters of authenticity that the user will enter

  

	- first method we use these parameters to connect to the database

  

	- last method we execute the file sql allowing to create or reboot the tables 

  

	- other methods create the filters in the db


  

- constants.py:

  

	- concatenate the CATEGORY to the URL of CATEGORY_URL

  

	- credentials to connect to the db

  

- main.py

  

	- used to run the program


-menu.py

  

	- make the menu design

  

  

## How to use it:

  

  

  

For a first use it is necessary to do:

  

  

- Change CREDENTIALS in constants file.

  

Then execute the following command:

  

  

python3 main.py --init

  

  

After that you can run the progam:

  

  

python3 main.py

Then press and confirm "2" to initialise the db for the first time

  

  
  

  
  

##

  

  

Once the connection is established the user will have to choose between:

  

  

Consult the substitutions he has already seen (empty if it's the first time)

  

  

Or choose a product category for which he will have to choose a particular product

  

  

Then he will be able to record or not the substitute of his choice

  

  

  

## Operations:

  

  

**Folder classes:**

  

  

- collect_data.py:

  

	- we pass him the url of openfoodfact

  

	- the first method