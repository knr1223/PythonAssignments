# Get input
input_arr = list(map(int, input("Enter a list of numbers (comma separated): ").split(',')))
D = int(input("Enter the number of rotations (D): "))

# Rotate the array by D elements towards right
n = len(input_arr)
D = D % n  # if D > n it resolves issue
rotated_arr = input_arr[-D:] + input_arr[:-D]

# Display the result
print("Array after rotation:", rotated_arr)