#can be done using abs() from math library also
#get input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find the maximum of the two numbers
max_num = max(num1, num2)

# Initialize LCM to the maximum number
lcm = max_num

# find common multiple
while True:
    if lcm % number1 == 0 and lcm % number2 == 0:
        break
    lcm += max_num

print(f"LCM of {num1} and {num2} is: {lcm}")