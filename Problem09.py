# ==========================================
# Problem 09: Student Information Database (OOP)
# Description: Demonstrates class creation, object instantiation, and searching
#              an array of student objects by name and ID.
# ==========================================

# Step 1: Define the Student class blueprint
class Student:
    def __init__(self, name, student_id, age, cgpa):
        """Initialize Student attributes."""
        self.name = name
        self.student_id = student_id
        self.age = age
        self.cgpa = cgpa

    def display(self):
        """Display student record details."""
        print("Name: ", self.name)
        print("ID: ", self.student_id)
        print("Age: ", self.age)
        print("CGPA: ", self.cgpa, "\n")


# Step 2: Instantiate student objects (Simulating database records)
s1 = Student("walid", "241-35-435", 24, 3.95)
s2 = Student("ashraf", "241-35-378", 22, 3.96)
s3 = Student("arafat", "241-35-190", 23, 3.66)
s4 = Student("fathum", "241-35-554", 24, 3.85)

# Step 3: Display all initialized student records
print("--- All Student Records ---")
s1.display()
s2.display()
s3.display()
s4.display()

# Step 4: Store student objects in a list for iteration
students_array = [s1, s2, s3, s4]

# Step 5: Receive search credentials from user
print("--- Student Verification ---")
user_name = input("Enter your name: ").strip()
user_id = input("Enter your ID: ").strip()

# Step 6: Search the list for a matching student record
found = False
for st in students_array:
    # Case-insensitive comparison for name and exact match for ID
    if st.name.lower() == user_name.lower() and st.student_id == user_id:
        print("\nCongratulations! Student found.")
        found = True
        st.display()
        break

# Step 7: Notify user only if no student matched the search criteria
# (Fixed bug where 'else:' was inside loop printing 'No student available' on every mismatch)
if not found:
    print("\nNo student available with the provided credentials.")
