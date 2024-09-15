import datetime
from db_oper import *

def log_operation(username, operation_str):
    history = load_json(HISTORY_FILE)
    operation_id = len(history) + 1
    date_str = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    history.append({
        'id': operation_id,
        'date': date_str,
        'operation': operation_str,
        'user_id': username
    })

    save_json(HISTORY_FILE, history)


def view_history(username):
    history = load_json(HISTORY_FILE)
    user_history = [entry for entry in history if entry['user_id'] == username]

    print("Select option:")
    print("1. View entire history")
    print("2. View history of the last day")
    choice = input("Enter choice: ")

    if choice == '1':
        for entry in user_history:
            print(entry)
    elif choice == '2':
        one_day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
        recent_history = [entry for entry in user_history if
                          datetime.datetime.strptime(entry['date'], "%d-%m-%Y %H:%M:%S") >= one_day_ago]
        for entry in recent_history:
            print(entry)
    else:
        print("Invalid choice.")
