# Student Grade Tracker - Version 2
# Added: letter grade conversion, remove student, highest/lowest grade

students = {}

def add_student(name, grade):
    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        return
    students[name] = grade
    print(f"Added {name} with grade {grade} ({get_letter_grade(grade)})")

def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def remove_student(name):
    if name in students:
        del students[name]
        print(f"Removed {name}.")
    else:
        print(f"Student '{name}' not found.")

def view_grades():
    if not students:
        print("No students added yet.")
        return
    print("\n--- Student Grades ---")
    for name, grade in students.items():
        print(f"{name}: {grade} ({get_letter_grade(grade)})")

def average_grade():
    if not students:
        print("No students to calculate average.")
        return
    avg = sum(students.values()) / len(students)
    print(f"\nClass Average: {avg:.2f} ({get_letter_grade(avg)})")

def best_and_worst():
    if not students:
        print("No students available.")
        return
    best = max(students, key=students.get)
    worst = min(students, key=students.get)
    print(f"Highest: {best} ({students[best]})")
    print(f"Lowest:  {worst} ({students[worst]})")

def main():
    while True:
        print("\n1. Add Student")
        print("2. Remove Student")
        print("3. View Grades")
        print("4. Show Average")
        print("5. Best & Worst Student")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student name: ")
            grade = float(input("Grade (0-100): "))
            add_student(name, grade)
        elif choice == "2":
            name = input("Student name to remove: ")
            remove_student(name)
        elif choice == "3":
            view_grades()
        elif choice == "4":
            average_grade()
        elif choice == "5":
            best_and_worst()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()