# username_generator.py

def generate_username():
    """Generate a username from a user's full name"""
    full_name = input("Enter your full name: ")
    names = full_name.split()
    first_name = names[0]
    last_name = "#".join(names[1:])
    username = (first_name[0] + last_name).lower()
    print(f"Your generated username is: {username}")

def main():
    generate_username()

if __name__ == '__main__':
    main()
