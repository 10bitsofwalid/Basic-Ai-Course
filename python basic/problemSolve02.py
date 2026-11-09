# ==========================================
# Module: python basic / problemSolve02.py
# Description: Product Inventory Management System (OOP).
#              Demonstrates object-oriented modeling with price categorization
#              and total inventory valuation calculation.
# ==========================================

# Step 1: Define the Product class
class Product:
    def __init__(self, product_id, product_name, product_price, product_quantity):
        """Constructor to initialize product properties."""
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    # Step 2: Method to display product information
    def display(self):
        """Print product specification and inventory count."""
        print(f"Product ID:       {self.product_id}")
        print(f"Product Name:     {self.product_name}")
        print(f"Product Price:    ${self.product_price:.2f}")
        print(f"Product Quantity: {self.product_quantity}")

    # Step 3: Method to evaluate price category
    def check_price(self):
        """Classify item as Expensive, Moderate, or Cheap based on unit price."""
        if self.product_price >= 1000:
            return "Expensive"
        elif self.product_price >= 500:
            return "Moderate"
        else:
            return "Cheap"

    # Step 4: Method to calculate total inventory value
    def calculate_total(self):
        """Compute total value of available stock (price * quantity)."""
        return self.product_price * self.product_quantity


# Step 5: Create Product instances with varying price points and stock counts
product1 = Product("P001", "Laptop", 1200.00, 5)
product2 = Product("P002", "Smartphone", 800.00, 10)
product3 = Product("P003", "Headphones", 150.00, 25)

# Step 6: Store products in a list for iteration
products = [product1, product2, product3]

# Step 7: Display inventory summary, price bracket, and total holding value
print("=" * 40)
print("       PRODUCT INVENTORY REPORT")
print("=" * 40)

for i, product in enumerate(products, 1):
    print(f"\n--- Product {i} Details ---")
    product.display()
    print(f"Price Category:   {product.check_price()}")
    print(f"Total Stock Value: ${product.calculate_total():.2f}")

print("\n" + "=" * 40)
