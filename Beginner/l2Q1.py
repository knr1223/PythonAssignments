# Get input from user for two lists using map
l1 = list(map(int, input("Enter the first list of numbers (comma separated): ").split(',')))
l2 = list(map(int, input("Enter the second list of numbers (comma separated): ").split(',')))

# using set intersection to find common elements
common_elements = list(set(l1) & set(l2))

print("Common elements:", common_elements)