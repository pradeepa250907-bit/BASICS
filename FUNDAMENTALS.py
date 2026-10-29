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

print("\n--- MINI PROJECT ---")

students = ["A", "B", "C", "D", "E"]
scores = [85, 90, 78, 92, 88]

for i in range(len(students)):
    print(students[i], ":", scores[i])

print("Total Marks:", sum(scores))
print("Average:", sum(scores)/len(scores))
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))

print("\nMODULE 01 COMPLETED SUCCESSFULLY!")
