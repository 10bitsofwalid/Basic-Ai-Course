# ==========================================
# Problem 01: Temperature Suitability Checker
# Description: Evaluates input temperature and classifies it
#              as Suitable, Bearable, or Unbearable.
# ==========================================

# Step 1: Prompt the user to enter the temperature as an integer
temp = int(input("Enter temperature: "))

# Step 2: Check the temperature against defined thresholds
if temp < 30:
    # Temperatures strictly below 30 are comfortable/suitable
    print("Suitable")
elif temp == 30:
    # Exactly 30 degrees is considered bearable
    # (Simplified from 'temp <= 30 and temp >= 30' which logically checks temp == 30)
    print("bearable")
else:
    # Temperatures above 30 degrees are considered unbearable
    print("unbearable")
