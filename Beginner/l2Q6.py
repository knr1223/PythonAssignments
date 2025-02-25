# Function to check if a number is a power of two
def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    # Recursive case: divide n by 2
    return is_power_of_two(n // 2)

# Get input from the user
num = int(input("Enter a number to check if it's a power of two: "))

if is_power_of_two(num):
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")