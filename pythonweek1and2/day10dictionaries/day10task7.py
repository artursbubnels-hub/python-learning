products = {
    "laptop": 1200,
    "phone": 3000,
    "tablet": 500,
    "monitor": 300
}
most_expensive = max(products, key=products.get)

print("Product:", most_expensive)
print("Price:", products[most_expensive])