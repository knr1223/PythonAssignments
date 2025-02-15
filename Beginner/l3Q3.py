import os

def JtoI(file_path):
    if not os.path.exists(file_path):  # Check if file exists
        print(f"Error: {file_path} not found!")
        return

    with open(file_path, 'r') as file:
        content = file.read()  # Read the entire content

    corrected_content = content.replace('J', 'I')  # Replace 'J' with 'I'

    print("Corrected Content:\n")
    print(corrected_content)  # Display the modified content


# Get the script's directory dynamically
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the correct file path
file_path = os.path.join(script_dir, "words.txt")

JtoI(file_path)
