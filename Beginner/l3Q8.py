def parse_encoded_string(encoded_str):
  parts = [part for part in encoded_str.split('0') if part]

  # Extract the first name, last name, and ID
  return {
    "first_name": parts[0],
    "last_name": parts[1],
    "id": parts[2]
  }

# Taking input from user with clear instructions
print("Enter an encoded string where first name, last name, and ID separated by any number of 0.")
user_input = input("Enter your encoded string: ")

parsed_data = parse_encoded_string(user_input)

print("\nParsed Data:")
print(parsed_data)
