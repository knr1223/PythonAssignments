# Base Class
class Student:
  def __init__(self, name, roll_number):
    self.name = name
    self.roll_number = roll_number

  def display(self):
    print(f"Student Name: {self.name}, Roll Number: {self.roll_number}")

# Single Inheritance
class CollegeStudent(Student):
  def __init__(self, name, roll_number, course):
    super().__init__(name, roll_number)
    self.course = course

  def display(self):
    super().display()
    print(f"Course: {self.course}")

# Multiple Inheritance
class Sports:
  def __init__(self, sport_name):
    self.sport_name = sport_name

class SportsStudent(Student, Sports):
  def __init__(self, name, roll_number, sport_name):
    Student.__init__(self, name, roll_number)
    Sports.__init__(self, sport_name)

  def display(self):
    super().display()
    print(f"Sport: {self.sport_name}")

# Multilevel Inheritance
class GraduateStudent(CollegeStudent):
  def __init__(self, name, roll_number, course, research_topic):
    super().__init__(name, roll_number, course)
    self.research_topic = research_topic

  def display(self):
    super().display()
    print(f"Research Topic: {self.research_topic}")

print("\n--- Single Inheritance ---")
college_student = CollegeStudent("Niveditha", 101, "Computer Science")
college_student.display()

print("\n--- Multiple Inheritance ---")
sports_student = SportsStudent("Raja", 102, "Basketball")
sports_student.display()

print("\n--- Multilevel Inheritance ---")
grad_student = GraduateStudent("Ram", 103, "Physics", "Quantum Mechanics")
grad_student.display()