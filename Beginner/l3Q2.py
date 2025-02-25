import os

def count_lines_in_file(file_path):
  if not os.path.exists(file_path):  # Check if file exists
    print(f"Error: {file_path} not found!")
    return 0

  with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)  # Count the number of lines

  return line_count

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the correct file path
file_path = os.path.join(script_dir, "demo.txt")

line_count = count_lines_in_file(file_path)
print(f"Total number of lines in {file_path}: {line_count}")
