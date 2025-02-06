try:
  # Get input marks for each subject
  physics = float(input("Enter marks for Physics: "))
  chemistry = float(input("Enter marks for Chemistry: "))
  biology = float(input("Enter marks for Biology: "))
  mathematics = float(input("Enter marks for Mathematics: "))
  computer = float(input("Enter marks for Computer: "))

  # checking for marks to be valid (0-100)
  for m in [physics, chemistry, biology, mathematics, computer]:
    if m < 0 or m > 100:
      raise ValueError("Marks should be between 0 and 100.")

  # Calculate total and percentage
  total_marks = physics + chemistry + biology + mathematics + computer
  percentage = (total_marks / 500) * 100

  # Determine grade
  if percentage >= 90:
    grade = "A"
  elif percentage >= 80:
    grade = "B"
  elif percentage >= 70:
    grade = "C"
  elif percentage >= 60:
    grade = "D"
  elif percentage >= 40:
    grade = "E"
  else:
    grade = "F"

  # Print results
  print(f"\nTotal Marks: {total_marks}/500")
  print(f"Percentage: {percentage:.2f}%")
  print(f"Grade: {grade}")

#Handling invalid marks
except ValueError as e:
    print(f"Error: {e}")
