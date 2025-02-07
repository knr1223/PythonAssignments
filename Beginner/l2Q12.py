# For registration
username = input("Enter a username: ")

while True:
    password = input("Enter a password: ")
    retype_password = input("Re-type the password: ")
    
    if password == retype_password:
        print("Registration successful!\n")
        break
    else:
        print("Passwords does not match. Please try again.\n")

# Login process with 3 attempts
attempts = 3

while attempts > 0:
    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")
    
    if login_username == username and login_password == password:
        print("Login successful! Welcome,", username)
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect username or password. You have {attempts} attempts left.\n")
        else:
            print("Too many failed attempts. Access denied.")