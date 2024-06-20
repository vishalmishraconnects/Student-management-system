# calculator.py

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def get_user_input():
    """Get two numbers and an operation from the user"""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")
    return num1, num2, operation

def perform_calculation(num1, num2, operation):
    """Perform the calculation based on the operation"""
    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        raise ValueError("Invalid operation!")
    return result

def main():
    num1, num2, operation = get_user_input()
    try:
        result = perform_calculation(num1, num2, operation)
        print(f"Result: {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
