# Get input from user
try:
    num = int(input("Enter a number: "))
    
    # Check if the number is negative or zero
    if num <= 0:
        raise ValueError("Number cannot be zero or negative.")
    
    revnum = 0
    
    while num > 0:
        revnum = revnum * 10 + num % 10
        num //= 10

    print("Reversed number:", revnum)

except ValueError as e:
    print(e)