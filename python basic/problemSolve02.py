class Product:
    # Constructor
    def __init__(self, product_id, product_name, product_price, product_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    # 1. display() method
    def display(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Product Price: ${self.product_price:.2f}")
        print(f"Product Quantity: {self.product_quantity}")

    # 2. check_price() method
    def check_price(self):
        if self.product_price >= 1000:
            return "Expensive"
        elif self.product_price >= 500:
            return "Moderate"
        else:
            return "Cheap"

    # 3. calculate_total() method
    def calculate_total(self):
        return self.product_price * self.product_quantity

# Create three Product objects with different information
product1 = Product("P001", "Laptop", 1200.00, 5)
product2 = Product("P002", "Smartphone", 800.00, 10)
product3 = Product("P003", "Headphones", 150.00, 25)

# Display details, price category, and total value for each product
products = [product1, product2, product3]

for i, product in enumerate(products, 1):
    print(f"Product {i} Details")
    product.display()
    print(f"Price Category: {product.check_price()}")
    print(f"Total Value: ${product.calculate_total():.2f}")