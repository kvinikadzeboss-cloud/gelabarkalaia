# Student Grade Tracker - Version 3
# Added: multiple subjects per student, save/load data to file, grade report

import json
import os

DATA_FILE = "grades.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)
    print("Data saved.")

def get_letter_grade(grade):
    if grade >= 90: return "A"
    elif grade >= 80: return "B"
    elif grade >= 70: return "C"
    elif grade >= 60: return "D"
    else: return "F"

def add_grade(students, name, subject, grade):
    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        return
    if name not in students:
        students[name] = {}
    students[name][subject] = grade
    print(f"Added {subject} grade {grade} ({get_letter_grade(grade)}) for {name}.")

def remove_student(students, name):
    if name in students:
        del students[name]
        print(f"Removed {name}.")
    else:
        print(f"Student '{name}' not found.")

def view_grades(students):
    if not students:
        print("No students added yet.")
        return
    print("\n========= Grade Report =========")
    for name, subjects in students.items():
        if subjects:
            avg = sum(subjects.values()) / len(subjects)
            print(f"\n{name} (Average: {avg:.2f} | {get_letter_grade(avg)})")
            for subject, grade in subjects.items():
                print(f"   {subject:<15} {grade:>6}  ({get_letter_grade(grade)})")
        else:
            print(f"\n{name}: No grades recorded.")
    print("================================")

def class_summary(students):
    all_averages = []
    for subjects in students.values():
        if subjects:
            avg = sum(subjects.values()) / len(subjects)
            all_averages.append(avg)
    if not all_averages:
        print("No data available.")
        return
    class_avg = sum(all_averages) / len(all_averages)
    print(f"\nTotal Students : {len(students)}")
    print(f"Class Average  : {class_avg:.2f} ({get_letter_grade(class_avg)})")
    best = max(students, key=lambda n: sum(students[n].values()) / len(students[n]) if students[n] else 0)
    worst = min(students, key=lambda n: sum(students[n].values()) / len(students[n]) if students[n] else 100)
    print(f"Top Student    : {best}")
    print(f"Needs Support  : {worst}")

def main():
    students = load_data()
    print("=== Student Grade Tracker v3 ===")

    while True:
        print("\n1. Add Grade")
        print("2. Remove Student")
        print("3. View All Grades")
        print("4. Class Summary")
        print("5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Student name: ")
            subject = input("Subject: ")
            grade = float(input("Grade (0-100): "))
            add_grade(students, name, subject, grade)
        elif choice == "2":
            name = input("Student name to remove: ")
            remove_student(students, name)
        elif choice == "3":
            view_grades(students)
        elif choice == "4":
            class_summary(students)
        elif choice == "5":
            save_data(students)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()