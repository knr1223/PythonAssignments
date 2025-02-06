try:
  # Get input and converting to integer
  n = int(input("Enter a number: "))

  # Checking divisibility with conditional statements
  if n % 3 == 0 and n % 5 == 0:
    print("Consultadd - Python Training")
  elif n % 3 == 0:
    print("Consultadd")
  elif n % 5 == 0:
    print("Python Training")
  else:
    print("Number is not divisible by 3 or 5.") 

#Exception handling for invalid inputs like"abc"
except ValueError:
  print("Error: Invalid input. Please enter an integer.")