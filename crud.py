from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 50000},
    {"id": 2, "name": "Phone", "category": "electronics", "price": 20000},
    {"id": 3, "name": "Shoes", "category": "fashion", "price": 2500}
]


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float


@app.get('/')
def home():
    return {'message': 'Welcome To Home'}


@app.get('/products')
def get_products():
    return products


# retrieve one product by id
@app.get('/products/{product_id}')
def get_product_by_id(product_id: int):
    for product in products:
        if product.get('id') == product_id:
            return product
    return {'message': 'Product ID not Found'}


# add product
@app.post('/create_product')
def create_product(product: Product):
    product_data = product.model_dump()
    products.append(product_data)
    return {'product': product,
            'message': 'Product added successfully'}


@app.put('/update_data/{product_id}')
def update_product(product_data: Product, product_id: int):
    product_data = product_data.model_dump()
    for index, product in enumerate(products):
        if product.get('id') == product_id:
            products[index] = product_data
            return {'message': 'Product updated successfully'}
    return {'message': 'Product not found'}


@app.delete('/delete_product/{product_id}')
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.get('id') == product_id:
            deleted_product = products.pop(index)
            return {
                'message': 'Product deleted successfully',
                'product': deleted_product
            }
    return {'message': 'Product not found'}
