# Object Oriented Programming

class Student:
  def __init__(self, name, student_id, age, cgpa):
    self.name = name
    self.student_id = student_id
    self.age = age
    self.cgpa = cgpa

  def display(self):
    print("Name: ", self.name)
    print("ID: ", self.student_id)
    print("Age: ", self.age)
    print("CGPA: ", self.cgpa, "\n")

# student database
s1 = Student("Walid", "241-35-435", 24, 3.95)
s2 = Student("Ashraf", "241-35-378", 22, 3.96)
s3 = Student("Arafat", "241-35-190", 23, 3.66)
s4 = Student("Fathum", "241-35-554", 24, 3.85)

s1.display()
s2.display()
s3.display()
s4.display()

# students array
students_array=[s1,s2,s3,s4]

# user input
user_name= input("Enter your name: ")
user_id= input("Enter your ID: ")

found=False
for st in students_array:
  if st.name == user_name and st.student_id == user_id:
    print("\nCongratulations! Student found.")
    found=True
    st.display()
    break
else:
    print("No student available")