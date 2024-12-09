correct_password = "Goa"


while True:

    password = input("Enter the password: ")

    if password == correct_password:
        print("Password is correct! Access.")
        break
    else:
        print("Incorrect password. Try again.")