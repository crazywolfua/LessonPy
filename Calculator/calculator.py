import math
from history import save_operation

def basic_calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation!")
                continue
            print(f"Result: {result}")
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def advanced_calculator(user_id):
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /, sin, cos, tan, cot): ")
            if operation in ("sin", "cos", "tan", "cot"):
                result = None
                if operation == "sin":
                    result = math.sin(math.radians(num1))
                elif operation == "cos":
                    result = math.cos(math.radians(num1))
                elif operation == "tan":
                    result = math.tan(math.radians(num1))
                elif operation == "cot":
                    if math.sin(math.radians(num1)) == 0:
                        print("Error: cotangent is undefined for 0 degrees.")
                        continue
                    result = 1 / math.tan(math.radians(num1))
                print(f"Result: {result}")
                save_operation(operation, result, user_id)
            else:
                num2 = float(input("Enter second number: "))
                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "*":
                    result = num1 * num2
                elif operation == "/":
                    if num2 == 0:
                        print("Cannot divide by zero!")
                        continue
                    result = num1 / num2
                else:
                    print("Invalid operation!")
                    continue
                print(f"Result: {result}")
                save_operation(operation, result, user_id)
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")