# ==========================================
# Problem 03: Student Grade Evaluation System
# Description: Takes a numeric score as input and prints the
#              corresponding letter grade based on predefined score brackets.
# ==========================================

# Step 1: Prompt the user to enter their numerical grade/marks
grade = int(input("Enter Your Grade: "))

# Step 2: Validate the input range (grades typically between 0 and 100)
if grade < 0 or grade > 100:
    print("Invalid grade! Grade must be between 0 and 100.")

# Step 3: Categorize score into appropriate letter grade
elif grade >= 80:
    print("A+")
elif grade >= 70:
    # 70 to 79 (redundant 'and grade < 80' removed since previous if caught >= 80)
    print("A")
elif grade >= 60:
    # 60 to 69
    print("A-")
elif grade >= 50:
    # 50 to 59
    print("B+")
elif grade >= 40:
    # 40 to 49
    print("D")
else:
    # Scores below 40 are failing
    print("F")
