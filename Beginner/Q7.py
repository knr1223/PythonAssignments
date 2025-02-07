# Input strings
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if the sorted characters of both strings are the same
if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")