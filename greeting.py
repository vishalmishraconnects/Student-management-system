def get_user_name():
    """Get the user's name"""
    while True:
        name = input("Please enter your name: ")
        if name.strip():  # Check if the input is not empty
            return name
        else:
            print("Name cannot be empty. Please try again!")

def print_greeting(name):
    """Print a greeting message"""
    print(f"Hello, {name}! Welcome to Python programming.")

def main():
    name = get_user_name()
    print_greeting(name)

if __name__ == '__main__':
    main()
