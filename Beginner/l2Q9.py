my_list = [10, 20, 30, 40, 50]

# Get the index
index = int(input("Enter the index to modify: "))

# Get the new value to update at the index
new_value = int(input("Enter the new value: "))

try:
    # Attempt to update the element at the provided index
    my_list[index] = new_value
    print(f"Updated list: {my_list}")
except IndexError:
    # Handle the case where the index is out of range
    print("Error: Index is out of range! Please enter a valid index.")