from app.data_access.product_dba import *
from app.models.product import Product

def getAllProducts():
    return dataGetProducts()

def getProduct(id):
    return dataGetProduct(id)

def newProduct(input: Product):
    return dataAddProduct(input)

def updateProduct(input: Product):
    return dataUpdateProduct(input)

def deleteProduct(id: int):
    return dataDeleteProduct(id)
