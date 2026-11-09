# ==========================================
# Problem 12: Electricity Bill with Area Eligibility Validation (OOP)
# Description: Validates whether a customer's area is served before
#              recording unit consumption and generating the bill.
# ==========================================

# Step 1: Define the electricity bill class
class ElectricityBill:
    def __init__(self, name, unit):
        """Initialize consumer name and units consumed."""
        self.name = name
        self.unit = unit

    # Step 2: Method to display consumer details
    def display(self):
        """Print consumer billing details."""
        print("Consumer's name:", self.name.title())
        print("Units consumed:", self.unit)

    # Step 3: Method to categorize power usage
    def category(self):
        """Classify energy usage tier according to units consumed."""
        if self.unit < 0:
            print("Usage Category: Invalid unit amount! Units cannot be negative.")
        elif self.unit <= 100:
            print("Usage Category: Low usage")
        elif self.unit < 300:
            print("Usage Category: Medium usage")
        elif self.unit <= 500:
            print("Usage Category: High usage")
        else:
            print("Usage Category: Very High Voltage")


# Backward compatibility alias
electricity_bill = ElectricityBill

# Step 4: Define eligible coverage areas (Moved outside the class definition)
area = ["savar", "uttara", "dakkshinkhan", "airport"]

# Step 5: Receive customer credentials and area input
customer_name = input("Enter customer name: ").strip()
selected_area = input("Enter area: ").strip().lower()

# Step 6: Validate area eligibility
if selected_area not in area:
    print("You're an outsider, get lost, no bill for you")
else:
    # Step 7: Only prompt for units and generate bill if area is valid
    # (Fixed bug where unverified area still attempted to instantiate bill with undefined bill_unit)
    bill_unit = int(input("Enter bill unit: "))
    bill = ElectricityBill(customer_name, bill_unit)
    print("\n--- Bill Summary ---")
    bill.display()
    bill.category()
