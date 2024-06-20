# student_info.py

student_dict = {}  # dictionary to store student IDs and details
student_ids = set()  # set to ensure no duplicate IDs

def add_student():
    """Add a new student to the dictionary"""
    student_id = input("Enter the student's ID: ")
    if student_id in student_ids:
        print("Student ID already exists. Please try again.")
        return
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grade = float(input("Enter the student's grade: "))
    student_dict[student_id] = {"name": name, "age": age, "grade": grade}
    student_ids.add(student_id)
    print(f"Student '{name}' added with ID {student_id}.")

def update_student():
    """Update an existing student's details"""
    student_id = input("Enter the student's ID to update: ")
    if student_id not in student_ids:
        print("Student ID not found. Please try again.")
        return
    name = input("Enter the student's new name: ")
    age = int(input("Enter the student's new age: "))
    grade = float(input("Enter the student's new grade: "))
    student_dict[student_id] = {"name": name, "age": age, "grade": grade}
    print(f"Student '{name}' updated with ID {student_id}.")

def retrieve_student():
    """Retrieve a student's details"""
    student_id = input("Enter the student's ID to retrieve: ")
    if student_id not in student_ids:
        print("Student ID not found. Please try again.")
        return
    student_details = student_dict[student_id]
    print(f"Student '{student_details['name']}' details:")
    print(f"  ID: {student_id}")
    print(f"  Age: {student_details['age']}")
    print(f"  Grade: {student_details['grade']}")

def delete_student():
    """Delete a student's details"""
    student_id = input("Enter the student's ID to delete: ")
    if student_id not in student_ids:
        print("Student ID not found. Please try again.")
        return
    del student_dict[student_id]
    student_ids.remove(student_id)
    print(f"Student with ID {student_id} deleted.")

def main():
    while True:
        print("\nOptions:")
        print("  1. Add a new student")
        print("  2. Update a student")
        print("  3. Retrieve a student")
        print("  4. Delete a student")
        print("  5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            retrieve_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
