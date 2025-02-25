# Function to count the number of vowels in a given string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    
    # Loop through each character in the string and check if it's a vowel
    for char in string:
        if char in vowels:
            count += 1
            
    return count

# Get input from the user
input_string = input("Enter a string: ")

# Call the function to count vowels and display the result
no_of_vowels = count_vowels(input_string)
print(f"Number of vowels: {no_of_vowels}")