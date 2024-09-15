from register import login_user, register_user
from calculator import perform_operation
from history import view_history

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Use Calculator (non-authorized)")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
            if user:
                while True:
                    print("\n1. Use Calculator")
                    print("2. View History")
                    print("3. Logout")
                    user_choice = input("Enter choice: ")

                    if user_choice == '1':
                        perform_operation(user)
                    elif user_choice == '2':
                        view_history(user)
                    elif user_choice == '3':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            perform_operation()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()