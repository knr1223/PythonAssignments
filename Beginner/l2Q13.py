# Get input string and charecter
input_string = input("Enter a string: ")
given_char = input("Enter the character to check: ")

# Lambda function to check if the string starts with the given character
starts_with = lambda s, c: s.startswith(c)

# Output the result
print(starts_with(input_string, given_char))