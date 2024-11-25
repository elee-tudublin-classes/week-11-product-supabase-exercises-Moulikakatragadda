from app.models.product import Product
from starlette.config import Config
import httpx

config = Config(".env")

products_data = []

def dataInitDB():
    global products_data
    if products_data:
        return True
    response = httpx.get(config("PRODUCT_DATA_URL"))
    data = response.json()
    products_data = data['products']
    return True

def dataGetProducts():
    dataInitDB()
    return products_data

def dataGetProduct(id: int):
    return next((product for product in products_data if product['id'] == id), None)

def dataAddProduct(new_product):
    new_product.id = len(products_data) + 1
    products_data.append(new_product.dict())
    return new_product

def dataUpdateProduct(update_product):
    for index, product in enumerate(products_data):
        if product['id'] == update_product.id:
            products_data[index] = update_product.dict()
            return update_product
    return None

def dataDeleteProduct(id: int):
    global products_data
    products_data = [product for product in products_data if product['id'] != id]
    return True
