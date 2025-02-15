import os

def even_length_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()# Considering file could have multiple lines

    even_length_lines = []
    for line in lines:
        words = line.strip().split()  # Split words in each line
        even_words = [word for word in words if len(word) % 2 == 0]  # Select even-length words
        even_length_lines.append(" ".join(even_words))  # Reconstruct the line

    return "\n".join(even_length_lines)  # Return formatted string

# Example usage:

# Dynamically get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))  

# Construct the correct file path
file_path = os.path.join(script_directory, "doc.txt")  

output = even_length_words(file_path)
print(output)
