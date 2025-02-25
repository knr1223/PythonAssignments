def run_length_encoding(input_str):
  encoded_str = ""
  count = 1

  # Loop through the string and count consecutive characters
  for i in range(1, len(input_str)):
    if input_str[i] == input_str[i - 1]:  # If character repeats
      count += 1
    else:
      encoded_str += input_str[i - 1] + str(count)  
      count = 1  # Reset count for new character

  # Append the last character count
  encoded_str += input_str[-1] + str(count)

  return encoded_str

# User input
user_input = input("Enter a string to encode using Run-Length Encoding: ")

encoded_output = run_length_encoding(user_input)

print("\nRun-Length Encoded String:")
print(encoded_output)
