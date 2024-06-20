# student_grades.py

students = []  # list to store student names and grades as tuples

def add_student():
    """Add a new student to the list"""
    name = input("Enter the student's name: ")
    grade = float(input("Enter the student's grade: "))
    students.append((name, grade))
    print(f"Student '{name}' added with grade {grade:.2f}.")

def remove_student():
    """Remove a student from the list"""
    name = input("Enter the student's name to remove: ")
    for i, (student_name, _) in enumerate(students):
        if student_name == name:
            del students[i]
            print(f"Student '{name}' removed.")
            return
    print(f"Student '{name}' not found.")

def display_students():
    """Display all students with their grades"""
    if not students:
        print("No students in the list.")
    else:
        print("Students and their grades:")
        for student_name, grade in students:
            print(f"  {student_name}: {grade:.2f}")

def main():
    while True:
        print("\nOptions:")
        print("  1. Add a new student")
        print("  2. Remove a student")
        print("  3. Display all students")
        print("  4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            display_students()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
