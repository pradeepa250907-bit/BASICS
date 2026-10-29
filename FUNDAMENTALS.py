print("WELCOME TO PYTHON AND DATA SCIENCE")
#VARIABLES
name = "Student"
age = 19
department = "AI and Data Science"
cgpa = 7.61
print("\n--- STUDENT DETAILS ---")
print("Name:", name)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)

#DATA TYPES
print("\n--- DATA TYPES ---")
print(type(name))
print(type(age))
print(type(cgpa))

#LISTS
print("\n--- LISTS ---")

marks = [85, 90, 78, 92, 88]

print("Marks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))

#DICTIONARY
print("\n--- DICTIONARY ---")

student = {
    "Name": "Student",
    "Department": "AI & DS",
    "Year": 2
}

print(student)

#CONDITIONAL STATEMENT
print("\n--- IF ELSE ---")

average = sum(marks) / len(marks)

if average >= 80:
    print("Excellent Performance")
else:
    print("Keep Improving")

#FOR LOOP
print("\n--- FOR LOOP ---")

for mark in marks:
    print(mark)

#WHILE LOOP
print("\n--- WHILE LOOP ---")

count = 1

while count <= 5:
    print(count)
    count += 1

#FUNCTIONS
print("\n--- FUNCTIONS ---")

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

result = calculate_average(marks)

print("Average Marks:", result)

#FILE HANDLING
print("\n--- FILE HANDLING ---")

with open("student_report.txt", "w") as file:
    file.write("STUDENT PERFORMANCE REPORT\n")
    file.write("Average Marks: " + str(result))

with open("student_report.txt", "r") as file:
    print(file.read())

# MINI PROJECT
# STUDENT PERFORMANCE ANALYSIS
"""EduTrack: Student Performance and Academic Analytics (Python 3.10+)."""
import csv
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).resolve().parent
DATA = BASE / 'students.csv'
REPORTS = BASE / 'reports'
SUBJECTS = ['Python', 'Mathematics', 'Data Structures', 'Statistics', 'Database']
FIELDS = ['register_no', 'name', 'attended', 'conducted'] + SUBJECTS


def ask_int(prompt, low=0, high=100):
    while True:
        try:
            value = int(input(prompt).strip())
            if low <= value <= high:
                return value
        except ValueError:
            pass
        print(f'Please enter a whole number from {low} to {high}.')


def load():
    if not DATA.exists():
        return []
    with DATA.open('r', newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def save(rows):
    with DATA.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def average(s):
    return sum(int(s[x]) for x in SUBJECTS) / len(SUBJECTS)


def attendance(s):
    conducted = int(s['conducted'])
    return 100 * int(s['attended']) / conducted if conducted else 0.0


def grade(score):
    if score >= 90: return 'O'
    if score >= 80: return 'A+'
    if score >= 70: return 'A'
    if score >= 60: return 'B+'
    if score >= 50: return 'B'
    if score >= 40: return 'C'
    return 'F'


def find(rows):
    key = input('Enter register number: ').strip().upper()
    return next((s for s in rows if s['register_no'].upper() == key), None)


def show_student(s):
    print('\n' + '=' * 48)
    print(f"{s['name']} | Register No: {s['register_no']}")
    print('-' * 48)
    for subject in SUBJECTS:
        print(f'{subject:<22}: {s[subject]}/100')
    print(f"Total marks           : {sum(int(s[x]) for x in SUBJECTS)}/{len(SUBJECTS)*100}")
    print(f'Average / Percentage  : {average(s):.2f}%')
    print(f'Grade                 : {grade(average(s))}')
    print(f'Attendance            : {attendance(s):.2f}%')
    print('Attendance status     :', 'Low (<75%)' if attendance(s) < 75 else 'Satisfactory')
    print('=' * 48)


def add_student(rows):
    reg = input('Register number: ').strip().upper()
    if not reg or any(s['register_no'].upper() == reg for s in rows):
        print('Register number is empty or already exists.'); return
    name = input('Student name: ').strip()
    if not name:
        print('Name cannot be empty.'); return
    s = {'register_no': reg, 'name': name}
    for subject in SUBJECTS:
        s[subject] = ask_int(f'{subject} marks (0-100): ')
    conducted = ask_int('Total classes conducted: ', 1, 100000)
    attended = ask_int('Classes attended: ', 0, conducted)
    s.update(attended=attended, conducted=conducted)
    rows.append(s)
    save(rows)
    print('Student saved successfully!')


def list_students(rows):
    if not rows:
        print('No student records found.'); return
