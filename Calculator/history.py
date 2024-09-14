import json
import datetime

def save_operation(operation, result, user_id):
    try:
        with open("operations.json", "r") as f:
            operations = json.load(f)
    except FileNotFoundError:
        operations = []
    operation_id = len(operations) + 1
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    operation_data = {
        "id": operation_id,
        "date": current_date,
        "operation": operation,
        "result": result,
        "user_id": user_id
    }
    operations.append(operation_data)
    with open("operations.json", "w") as f:
        json.dump(operations, f)

def view_history(user_id):
    try:
        with open("operations.json", "r") as f:
            operations = json.load(f)
    except FileNotFoundError:
        print("No operation history found.")
        return
    user_operations = [op for op in operations if op["user_id"] == user_id]
    if user_operations:
        print("Operation History:")
        for operation in user_operations:
            print(f"ID: {operation['id']}, Date: {operation['date']}, Operation: {operation['operation']}, Result: {operation['result']}")
    else:
        print("No operations found for this user.")