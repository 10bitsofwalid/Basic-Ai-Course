number_of_affected_people = int(input("Enter number of affected people :"))
number_of_injured_people = int(input("Enter number of injured people :"))
infrastructure_damage = input("Enter infrastructure damage situation (High/Low):").lower()
weather_condition = "Dangerous"
available_rescue_items = input("Enter number of available rescue items :")
hospital_capacity = float(input("Enter number of hospital capacity in % :"))

LEVEL_1 = "Normal Response"
LEVEL_2 = "Increased Response"
LEVEL_3 = "Emergency Response"
LEVEL_4 = "Major Disaster Response"

if number_of_affected_people > 500 and number_of_injured_people > 100:
    print(LEVEL_4)
elif number_of_affected_people > 200 and hospital_capacity < 30 :
    print(LEVEL_3)
elif infrastructure_damage and hospital_capacity < 30 :
    print(LEVEL_3)

