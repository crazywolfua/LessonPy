import json

def register(username, password):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    if username in users:
        print("Username already exists!")
        return
    users[username] = password
    with open("users.json", "w") as f:
        json.dump(users, f)
    print("User registered successfully!")