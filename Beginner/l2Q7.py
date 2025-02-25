# Function
def find_median(input_list):
    # Sort the list
    input_list.sort()

    n = len(input_list)
    
    # Check if the length of the list is odd or even
    if n % 2 == 1:
        #return the middle element
        return input_list[n // 2]
    else:
        #return the average of the two middle elements
        mid1, mid2 = input_list[n // 2 - 1], input_list[n // 2]
        return (mid1 + mid2) / 2

input_list = list(map(int, input("Enter numbers (comma separated): ").split(',')))

median = find_median(input_list)
print(f"Median: {median}")