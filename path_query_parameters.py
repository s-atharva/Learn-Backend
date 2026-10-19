from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 50000},
    {"id": 2, "name": "Phone", "category": "electronics", "price": 20000},
    {"id": 3, "name": "Shoes", "category": "fashion", "price": 2500},
    {"id": 4, "name": "Watch", "category": "fashion", "price": 5000},
    {"id": 5, "name": "Headphones", "category": "electronics", "price": 3000}
]


# 1. Get all products
@app.get('/')
def get_products():
    return products


# 2. Get a product by ID (PATH PARAMETER)
@app.get('/product/{product_id}')
def get_product_id(product_id: int):
    for product in products:
        if product.get('id') == product_id:
            return product
    return {'message': 'Product not found.'}


# 3. Filter products by category (QUERY PARAMETER)
@app.get('/search')
def search_product(category: str):
    result = []
    for product in products:
        if product.get('category') == category:
            result.append(product)
    return result


# 4. Filter products by maximum price (QUERY PARAMETER)
@app.get('/product-filter')
def product_filter(category: str, max_price: int):
    result = []
    for product in products:
        if product.get('category') == category and product.get('price') <= max_price:
            result.append(product)
    return result

# 5. Filter by category AND maximum price
