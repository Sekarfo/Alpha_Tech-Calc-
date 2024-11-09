def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Div by zero is invalid "


while True:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    operation = input("Enter operation (1/2/3/4/5): ")

    if operation == '1':
        print(f"Result: {add(num1, num2)}")
    elif operation == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"Result: {divide(num1, num2)}")
    elif operation == '5':
        break;