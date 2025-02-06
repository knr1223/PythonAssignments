# Get input
str = input("Enter a string: ")

# Initialize counters for letters and digits
letter_count = 0
digit_count = 0

# Iterating through each character in the string
for char in str:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

# using fstring to print result
print(f"Alphabets: {letter_count} & Numbers: {digit_count}")