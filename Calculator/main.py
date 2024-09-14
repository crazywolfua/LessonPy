import json
from register import register
from login import authorize
from calculator import basic_calculator, advanced_calculator
from history import view_history

def main():
    while True:
        choice = input("1. Register\n2. Login\n3. Basic calculator\n4. Exit\nChoose an option: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authorize(username, password):
                print("Login successful!")
                while True:
                    try:
                        with open("users.json", "r") as f:
                            users = json.load(f)
                        user_id = users[username]
                        action = input("1. Advanced calculator\n2. View History\n3. Logout\nChoose an option: ")
                        if action == "1":
                            advanced_calculator(user_id)
                        elif action == "2":
                            view_history(user_id)
                        elif action == "3":
                            print("Logout successful!")
                            break
                        else:
                            print("Invalid choice!")
                    except (FileNotFoundError, KeyError):
                        print("Error: User data not found. Please register first.")
            else:
                print("Invalid username or password!")
        elif choice == "3":
            basic_calculator()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
