# ==========================================
# Problem 13: Area and Customer Registry Electricity Billing System (OOP)
# Description: Verifies area zone eligibility against area0, matches customer
#              against area1 or area2 registry, prompts for consumption, and bills.
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

# Step 4: Define valid coverage zones and customer registries
area0 = ["mirpur", "uttora", "ecb", "taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu"]
area1 = ["tunbir", "wudud", "ushraff", "muria"]
area2 = ["ahuna", "tunmuii", "ishparsha", "ishfundun"]

# Step 5: Receive area and customer name from user
selected_area = input("Enter area: ").strip().lower()
customer_name = input("Enter customer name: ").strip().lower()

# Step 6: Verify area zone eligibility
if selected_area not in area0:
    print("You're an outsider, get lost, no bill for you")
else:
    # Step 7: Check customer registration against customer groups
    is_valid_customer = False
    if customer_name in area1:
        print("Area verified, Customer found in area1.")
        is_valid_customer = True
    elif customer_name in area2:
        print("Area verified, Customer found in area2.")
        is_valid_customer = True
    else:
        print("Area verified, but customer name is unrecognized.")

    # Step 8: Only prompt for bill_unit and generate bill if customer is verified
    # (Fixed bug where 'bill_unit' was referenced without ever being prompted or defined)
    if is_valid_customer:
        bill_unit = int(input("Enter bill unit: "))
        bill = ElectricityBill(customer_name, bill_unit)
        print("\n--- Bill Summary ---")
        bill.display()
        bill.category()
    else:
        print("Cannot generate bill for unrecognized customers.")
