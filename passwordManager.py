import random
import string

passwords = {}

#load exiting passwords from file
try:
    with open("passwords.txt", "r") as f:
        for line in f:
            website, password = line.strip().split(":")
            passwords[website] = password
except FileNotFoundError:
    pass

def generate_password(length=12):
    """Generate a random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    print("\n-----PASSWORD MANAGER APP-----")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add password
    if choice == "1":
        website = input("Enter website name: ")
        password = generate_password()
        passwords[website] = password
        with open("passwords.txt", "a") as f:
            f.write(f"{website}:{password}\n")
        print(f"Password for {website} successfully added!")

    # View passwords
    elif choice == "2":
        if not passwords:
            print("No passwords found!")
        else:
            for website, password in passwords.items():
                print(website, ":", password)

    # Exit
    elif choice == "3":
        print("Exiting.......")
        break

    else:
        print("Invalid input")