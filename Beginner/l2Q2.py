# Function to return unique elements from a list
def unique_elements(input_list):
    return list(set(input_list))

# Get input
list1 = list(map(int, input("Enter a list of numbers (comma separated): ").split(',')))

# Get unique elements
list2 = unique_elements(list1)

# Display the result
print("List with unique elements:", list2)