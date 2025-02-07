#get input
num = int(input("Enter a number: "))

# Initialize the result to 1
result = 1

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Use a for loop to multiply numbers from 1 to num
    for i in range(1, num + 1):
        result *= i

    # Print the factorial
    print(f"The factorial of {num} is: {result}")