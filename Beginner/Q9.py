# Get input from the user
input_list = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of integers
input_list = list(map(int, input_list.split()))
#We can also get list input using loop

# Initialize dictionary to store frequencies
frequency_count = {}

# Count the frequency of each element in the list
for x in input_list:
    if x in frequency_count:
        frequency_count[x] += 1
    else:
        frequency_count[x] = 1

# Print the frequency count
print("Frequency count:", frequency_count)