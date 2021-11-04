import requests
from Classes.collect_data import CollectData


url = f"https://world.openfoodfacts.org/cgi/search.pl?page_size=50&lang=fr&search_simple=1&action=process&json=1"
print(url)
r = requests.get(url)
data = r.json()
for product in data["products"]:
    print(product["product_name"],product.get("nutrition_grades","pas de note"))

print('-_-_-_-_-')

collect = CollectData()

collect.create_categories()
