import hashlib
from db_oper import *

users = ''
username = ''
password = ''
hashed_password = ''

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_info():
    global users, username, password, hashed_password
    users = load_json(USERS_FILE)
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    hashed_password = hash_password(password)

    return users, username, password, hashed_password

def register_user():
    get_user_info()

    if any(user['username'] == username for user in users):
        print("Username already exists.")
        return

    users.append({'username': username, 'password': hashed_password})
    save_json(USERS_FILE, users)
    print(f"User {username} registered successfully.")

def login_user():
    get_user_info()

    user = next((user for user in users if user['username'] == username and user['password'] == hashed_password), None)

    if user:
        print(f"User {username} logged in successfully.")
        return username
    else:
        print("Invalid username or password.")
        return None
