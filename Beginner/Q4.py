import math

try:
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  if (num2 < num1):
    raise ValueError("second number must be larger than first number")
  
  sum_odd = 0

  for x in range(num1,num2+1):
    if x > 0 and x % 2 != 0:
      sum_odd += x
  
  print(f"Sum of odd numbers from num1 to num2: {sum_odd}")

except ValueError as e:
  print(f"Error: {e}")