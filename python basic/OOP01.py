# ==========================================
# Module: python basic / OOP01.py
# Description: Student Database Management System using Object-Oriented Programming (OOP).
#              Demonstrates class attributes, methods, object instantiation, and searching.
# ==========================================

# Step 1: Define the Student class blueprint
class Student:
    def __init__(self, name, student_id, age, cgpa):
        """Constructor to initialize student attributes."""
        self.name = name
        self.student_id = student_id
        self.age = age
        self.cgpa = cgpa

    def display(self):
        """Method to display student profile details."""
        print("Name: ", self.name)
        print("ID:   ", self.student_id)
        print("Age:  ", self.age)
        print("CGPA: ", self.cgpa, "\n")


# Step 2: Instantiate student objects (Simulating database records)
s1 = Student("Walid", "241-35-435", 24, 3.95)
s2 = Student("Ashraf", "241-35-378", 22, 3.96)
s3 = Student("Arafat", "241-35-190", 23, 3.66)
s4 = Student("Fathum", "241-35-554", 24, 3.85)

# Step 3: Display all initialized student records
print("--- All Student Records ---")
s1.display()
s2.display()
s3.display()
s4.display()

# Step 4: Group student objects into an array (list)
students_array = [s1, s2, s3, s4]

# Step 5: Receive search credentials from the user
print("--- Search Student ---")
user_name = input("Enter your name: ").strip()
user_id = input("Enter your ID: ").strip()

# Step 6: Search the database with case-insensitive name matching
found = False
for st in students_array:
    if st.name.lower() == user_name.lower() and st.student_id == user_id:
        print("\nCongratulations! Student found.")
        found = True
        st.display()
        break

# Step 7: Notify user if student record was not found
if not found:
    print("\nNo student available matching the given name and ID.")
