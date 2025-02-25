# Get input
num = int(input("Enter a number: "))

# Initialize the sum of divisors to 0
sum_of_divisors = 0

# Check if the number is positive
if num <= 0:
    print("Please enter a positive integer.")
else:
    # Loop to find proper divisors
    for x in range(1, num):
        if num % x == 0:  # Check if i is a divisor of num
            sum_of_divisors += x  # Adding the divisor to the sum

    if sum_of_divisors == num:
        print("Yes")
    else:
        print("No")