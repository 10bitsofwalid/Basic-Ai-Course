# ==========================================
# Problem 08: Disaster Response Decision System (Rule-Based Expert System)
# Description: Evaluates disaster indicators (affected casualties, damage,
#              hospital capacity, rescue items) to determine emergency response level.
# ==========================================

# Step 1: Collect situational data from user
number_of_affected_people = int(input("Enter number of affected people: "))
number_of_injured_people = int(input("Enter number of injured people: "))
infrastructure_damage = input("Enter infrastructure damage situation (High/Low): ").strip().lower()
weather_condition = "Dangerous"  # Current environmental condition
available_rescue_items = int(input("Enter number of available rescue items: "))
hospital_capacity = float(input("Enter hospital capacity in %: "))

# Step 2: Define response levels
LEVEL_1 = "Level 1: Normal Response"
LEVEL_2 = "Level 2: Increased Response"
LEVEL_3 = "Level 3: Emergency Response"
LEVEL_4 = "Level 4: Major Disaster Response"

# Step 3: Apply rule-based classification based on severity criteria
# Level 4: Severe mass casualties
if number_of_affected_people > 500 and number_of_injured_people > 100:
    print("Action Required:", LEVEL_4)

# Level 3: Significant casualties with low hospital capacity OR high damage with low capacity
elif (number_of_affected_people > 200 and hospital_capacity < 30) or (infrastructure_damage == "high" and hospital_capacity < 30):
    print("Action Required:", LEVEL_3)

# Level 2: Moderate impact or dwindling resources/capacity
elif number_of_affected_people > 100 or number_of_injured_people > 50 or hospital_capacity < 50 or available_rescue_items < 30:
    print("Action Required:", LEVEL_2)

# Level 1: Conditions within manageable routine parameters
else:
    print("Action Required:", LEVEL_1)
