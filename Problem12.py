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

    area = ["savar", "uttara", "dakkshinkhan", "airport"]

    customer_name = input("Enter customer name: ")
    selected_area = input("Enter area: ").lower()
    if selected_area not in area:
        print("You're an outsider, get lost, no bill for you")
    else:
        bill_unit = int(input("Enter bill unit: "))
bill = electricity_bill(customer_name, bill_unit)
bill.display()
bill.category()