# ==========================================
# Module: python basic / problemSolve01.py
# Description: Multi-Zone Electricity Billing System with Customer Verification (OOP).
#              Validates region eligibility across composite area lists,
#              verifies customer identity, and calculates usage tier.
# ==========================================

# Step 1: Define ElectricityBill class
class ElectricityBill:
    def __init__(self, name, unit):
        """Constructor to initialize customer name and consumed unit count."""
        self.name = name
        self.unit = unit

    # Step 2: Display consumer bill summary
    def display(self):
        """Print formatted consumer name and unit details."""
        print("Consumer's name:", self.name.title())
        print("Units consumed: ", self.unit)

    # Step 3: Classify consumption into defined usage brackets
    def category(self):
        """Evaluate consumption volume against tier standards."""
        # Fixed bug: Check for negative values first so 'Invalid unit amount' is reachable
        if self.unit < 0:
            print("Usage Category: Invalid unit amount! Units cannot be negative.")
        elif self.unit <= 100:
            print("Usage Category: Low usage")
        elif 100 < self.unit < 300:
            print("Usage Category: Medium usage")
        elif 300 <= self.unit <= 500:
            print("Usage Category: High usage")
        else:
            print("Usage Category: Very High Voltage")


# Step 4: Define eligible territory area groups
area0 = ["mirpur", "uttara", "ecb", "dhanmondi"]
area1 = ["savar", "dhamrai", "ulukhola", "nabalpur"]
area2 = ["dakkshinkhan", "panditpara", "kackura", "dobadia"]

# Consolidate all supported operational zones
all_valid_areas = area0 + area1 + area2

# Step 5: Define authorized customers (normalized to lowercase for robust matching)
# Fixed bug: Mixed case in list prevented valid users like 'Ashraf' from matching
valid_customers = ["walid", "ashraf", "arafat", "fathum"]

# Step 6: Collect user area and customer name
selected_area = input("Enter area name: ").strip().lower()
customer_name = input("Enter customer name: ").strip().lower()

# Step 7: Validate area against all supported regions
if selected_area not in all_valid_areas:
    print("Not eligible for this area!")
else:
    # Step 8: Validate customer name against registered customer database
    if customer_name in valid_customers:
        print(f"Area verified ({selected_area.title()}), Customer found.")

        # Step 9: Prompt for consumption units and generate bill
        bill_unit = int(input("Enter bill unit: "))
        bill = ElectricityBill(customer_name, bill_unit)
        print("\n--- Bill Details ---")
        bill.display()
        bill.category()
    else:
        print("Area verified, but customer name is unrecognized. Cannot generate bill.")
