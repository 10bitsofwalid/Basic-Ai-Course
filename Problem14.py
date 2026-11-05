class electricity_bill:

    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def display(self):
        print("Consumers name:", self.name)
        print("Units consumed:", self.unit)

    def category(self):
        if self.unit <= 100:
            print("Low usage")
        elif self.unit > 100 and self.unit <= 299:
            print("Medium usage")
        elif self.unit >= 300 and self.unit <= 499:
            print("High usage")
        elif self.unit > 500:
            print("Very High Voltage")
        else:
            print("No Current for you, good luck")

area0 = ["mirpur", "uttora", "ecb", "taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu"]
area1 = ["tunbir", "wudud", "ushraff", "muria"]
area2 = ["ahuna", "tunmuii", "ishparsha", "ishfundun"]

selected_area = input("Enter area: ").lower()
customer_name = input("Enter customer name: ").lower()

if selected_area not in area0:
    print("You're an outsider, get lost, no bill for you")
else:
    is_valid_customer = False
    if customer_name in area1:
        print("Area verified, Customer found in area1.")
        is_valid_customer = True
    elif customer_name in area2:
        print("Area verified, Customer found in area2.")
        is_valid_customer = True
    else:
        print("Area verified, but customer name is unrecognized.")

    if is_valid_customer:
        bill_unit = int(input("Enter bill unit: "))
        bill = electricity_bill(customer_name, bill_unit)
        bill.display()
        bill.category()
    else:
        print("Cannot generate bill for unrecognized customers.")