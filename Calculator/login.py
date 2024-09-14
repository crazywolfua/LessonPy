import json

def authorize(username, password):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return False
    if username in users and users[username] == password:
        return True
    else:
        return False