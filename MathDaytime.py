# math_datetime_utility.py

import math
import datetime

def calculate_math_utilities(num):
    """Calculate the square root and factorial of a number"""
    try:
        num = float(num)
        sqrt = math.sqrt(num)
        factorial = math.factorial(int(num))
        print(f"Square root of {num}: {sqrt}")
        print(f"Factorial of {num}: {factorial}")
    except ValueError:
        print("Error: Invalid input. Please enter a non-negative number.")
    except OverflowError:
        print("Error: Factorial of a large number is not supported.")

def display_current_datetime():
    """Display the current date and time in a formatted string"""
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def main():
    num = input("Enter a number: ")
    calculate_math_utilities(num)
    display_current_datetime()

if __name__ == '__main__':
    main()
