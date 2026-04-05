# Student Grade Tracker - Version 1
# Basic version: add students and their grades, view average
# Updated in dev-branch
students = {}

def add_student(name, grade):
    students[name] = grade
    print(f"Added {name} with grade {grade}")

def view_grades():
    if not students:
        print("No students added yet.")
        return
    print("\n--- Student Grades ---")
    for name, grade in students.items():
        print(f"{name}: {grade}")

def average_grade():
    if not students:
        print("No students to calculate average.")
        return
    avg = sum(students.values()) / len(students)
    print(f"\nClass Average: {avg:.2f}")

def main():
    while True:
        print("\n1. Add Student")
        print("2. View Grades")
        print("3. Show Average")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student name: ")
            grade = float(input("Grade (0-100): "))
            add_student(name, grade)
        elif choice == "2":
            view_grades()
        elif choice == "3":
            average_grade()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()