# ==========================================
# Problem 14: Multi-Zone Customer Registry & Billing Verification (OOP)
# Description: Two-factor verification: ensures area is in the service region,
#              verifies customer in authorized customer sets, and calculates usage category.
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
            # Fixed boundary gap where 500 units fell into 'else'
            print("Usage Category: High usage")
        else:
            print("Usage Category: Very High Voltage")


# Backward compatibility alias
electricity_bill = ElectricityBill

# Step 4: Define valid service areas (area0) and customer groups (area1, area2)
area0 = ["mirpur", "uttora", "ecb", "taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu"]
area1 = ["tunbir", "wudud", "ushraff", "muria"]
area2 = ["ahuna", "tunmuii", "ishparsha", "ishfundun"]

# Step 5: Collect area and customer name from user
selected_area = input("Enter area: ").strip().lower()
customer_name = input("Enter customer name: ").strip().lower()

# Step 6: Step 1 of validation - Check if the selected area is serviced
if selected_area not in area0:
    print("You're an outsider, get lost, no bill for you")
else:
    # Step 7: Step 2 of validation - Check if customer is registered in area1 or area2
    is_valid_customer = False
    if customer_name in area1:
        print("Area verified, Customer found in area1.")
        is_valid_customer = True
    elif customer_name in area2:
        print("Area verified, Customer found in area2.")
        is_valid_customer = True
    else:
        print("Area verified, but customer name is unrecognized.")

    # Step 8: If customer is registered, prompt for consumption units and generate bill
    if is_valid_customer:
        bill_unit = int(input("Enter bill unit: "))
        bill = ElectricityBill(customer_name, bill_unit)
        print("\n--- Bill Summary ---")
        bill.display()
        bill.category()
    else:
        print("Cannot generate bill for unrecognized customers.")
