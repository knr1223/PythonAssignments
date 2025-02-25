# Get input of list of strings
string_list = input("Enter words separated by commas: ")

# Convert into a list of words
words = string_list.split(',')

# Strip any extra spaces
words = [word.strip() for word in words]

# convert each word to list of characters
result = list(map(list, words))

print(result)