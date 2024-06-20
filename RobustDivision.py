# robust_division.py

def divide(x, y):
    """Divide two numbers and handle potential errors"""
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Invalid input. Please enter two numbers.")
        return None
    else:
        print(f"Result: {result}")
        return result

def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid input. Please enter two numbers.")
        return

    divide(num1, num2)

if __name__ == '__main__':
    main()
