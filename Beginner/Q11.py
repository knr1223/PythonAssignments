# Get input
num = int(input("Enter a number: "))

# Compute sum of digits until it becomes a single-digit number
while num >= 10:
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num //= 10
    print("Intermediate Sum:", sum_of_digits)
    num = sum_of_digits  # Update num with new sum

print("Final Output:", num)