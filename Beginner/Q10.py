# Get input
input_sentence = input("Enter a sentence: ")

# Split sentence into words
words = input_sentence.split()  

# Reverse and join words
reversed_sentence = " ".join(words[::-1])  

# Display the output
print("Output after reverse:", reversed_sentence)