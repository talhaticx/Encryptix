import math
from rich.console import Console
from functools import wraps

console = Console()

def caution(message):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                console.print(f"{message}: {e}", style="bold red")
        return wrapper
    return decorator

@caution("Invalid input. Please enter a valid number.")
def get_number(prompt):
    while True:
            return float(input(prompt))

def get_operation():
    operations = {
        "+": "Addition",
        "-": "Subtraction",
        "*": "Multiplication",
        "/": "Division",
        "**": "Exponentiation",
        "%": "Modulus",
        "sqrt": "Square Root"
    }
    
    print("Select an operation:")
    for symbol, name in operations.items():
        console.print(f"{symbol} : {name}", style="bold green")

    while True:
        operation = input("Enter operation: ").strip()
        if operation in operations:
            return operation
        else:
            print("Invalid operation. Please choose a valid operation.")

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "**":
        return num1 ** num2
    elif operation == "%":
        return num1 % num2
    
def main():
    print("Welcome to the advanced CLI calculator!\n")

    while True:
        num1 = get_number("Enter the first number: ")
        while num1 == None:
            num1 = get_number("Enter the first number: ")
        print()
        operation = get_operation()
        print()
        
        if operation == "sqrt":
            console.print(f"The square root of {num1} is {math.sqrt(num1)}", style="bold blue")
        else:
            num2 = get_number("Enter the second number: ")
            result = calculate(num1, num2, operation)
            console.print(f"The result of {num1} {operation} {num2} is {result}", style="bold blue")

        console.print("\nDo you want to perform another calculation? (yes/no): ", style="bold purple")
        another = input().strip().lower()
        if another != "yes":
            break

    print()
    console.print("Thank you for using the advanced CLI calculator!", style="bold cyan")

if __name__ == "__main__":
    main()
