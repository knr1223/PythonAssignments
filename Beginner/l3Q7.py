students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

# Using a for loop
student_subject_dictionary = {}
for i in range(len(students)):
  student_subject_dictionary[students[i]] = subjects[i]
print("Using for loop:", student_subject_dictionary)

# Using dictionary comprehension
student_subject_dict_comp = {students[i]: subjects[i] for i in range(len(students))}
print("Using dictionary comprehension:", student_subject_dict_comp)
