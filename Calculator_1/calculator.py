import math
from history import log_operation

def perform_operation(user=None):
    if user:
        print("Select operation: +, -, *, /, sin, cos, tan, cot")
    else:
        print("Select operation: +, -, *, /")

    operation = input("Enter operation: ")

    if operation in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Division by zero error.")
                return
            result = num1 / num2

        operation_str = f"{num1} {operation} {num2} = {result}"

    elif user and operation in ['sin', 'cos', 'tan', 'cot']:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)

        if operation == 'sin':
            result = math.sin(radians)
        elif operation == 'cos':
            result = math.cos(radians)
        elif operation == 'tan':
            result = math.tan(radians)
        elif operation == 'cot':
            if math.tan(radians) == 0:
                print("Cotangent undefined (division by zero).")
                return
            result = 1 / math.tan(radians)

        operation_str = f"{operation}({angle}) = {result}"

    else:
        print("Invalid operation.")
        return

    print(operation_str)

    if user:
        log_operation(user, operation_str)
