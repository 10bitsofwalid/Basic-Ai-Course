class ElectricityBill:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def display(self):
        print("Consumer's name:", self.name.title())
        print("Units consumed:", self.unit)

    def category(self):
        if self.unit <= 100:
            print("Low usage")
        elif 100 < self.unit < 300: 
            print("Medium usage")
        elif 300 <= self.unit <= 500: 
            print("High usage")
        elif self.unit > 500:
            print("Very High Voltage")
        else:
            print("Invalid unit amount!")

area0 = ["mirpur", "uttara", "ecb", "dhanmondi"]
area1 = ["savar", "dhamrai", "ulukhola", "nabalpur"]
area2 = ["dakkshinkhan", "panditpara", "kackura", "dobadia"]

valid_customers = ["walid", "Ashraf", "Arafat", "Fathum"]

selected_area = input("Enter area name: ").lower()
customer_name = input("Enter customer name: ").lower()

all_valid_areas = area0 + area1 + area2

if selected_area not in all_valid_areas:
    print("Not eligible for this area!")
else:
    if customer_name in valid_customers:
        print(f"Area verified ({selected_area.title()}), Customer found.")
        
        bill_unit = int(input("Enter bill unit: "))
        bill = ElectricityBill(customer_name, bill_unit)
        bill.display()
        bill.category()
    else:
        print("Area verified, but customer name is unrecognized. Cannot generate bill.")