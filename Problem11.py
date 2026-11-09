# ==========================================
# Problem 11: Electricity Bill Calculation & Usage Tier Classification (OOP)
# Description: Defines an ElectricityBill class to track consumer usage
#              and classify it into billing tiers.
# ==========================================

# Step 1: Define the electricity bill class
class ElectricityBill:
    def __init__(self, name, unit):
        """Initialize consumer name and units consumed."""
        self.name = name
        self.unit = unit

    # Step 2: Method to display consumer billing information
    def display(self):
        """Display consumer details."""
        print("Consumer's name:", self.name.title())
        print("Units consumed:", self.unit)

    # Step 3: Method to categorize consumption tier
    def category(self):
        """Classify energy usage tier according to units consumed."""
        # Check for invalid negative units first
        if self.unit < 0:
            print("Usage Category: Invalid unit amount! Units cannot be negative.")
        elif self.unit <= 100:
            print("Usage Category: Low usage")
        elif self.unit < 300:
            # 101 to 299 units
            print("Usage Category: Medium usage")
        elif self.unit <= 500:
            # 300 to 500 units (fixed gap where unit == 500 fell through)
            print("Usage Category: High usage")
        else:
            # Over 500 units
            print("Usage Category: Very High Voltage")


# Maintain alias for backward compatibility with lowercase class name
electricity_bill = ElectricityBill

# Step 4: Take customer name and unit consumption as input
customer_name = input("Enter customer name: ").strip()
bill_unit = int(input("Enter bill unit: "))

# Step 5: Create ElectricityBill object
bill = ElectricityBill(customer_name, bill_unit)

# Step 6: Display bill details and usage category
print("\n--- Bill Summary ---")
bill.display()
bill.category()
