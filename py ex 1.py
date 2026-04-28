#1.student
students = [("A", 85), ("B", 40), ("C", 72), ("D", 30)]
passed_students = []
for name, marks in students:
    if marks >= 50:
        passed_students.append(name)
print("Passed Students:", passed_students)
total_marks = 0
for name, marks in students:
    total_marks += marks
average = total_marks / len(students)
print("Average Marks:", average)
topper_name = students[0][0]
max_marks = students[0][1]
for name, marks in students:
    if marks > max_marks:
        max_marks = marks
        topper_name = name

print("Topper:", topper_name, "with", max_marks, "marks")


#2.password
def check_password(password):
    upper = False
    lower = False
    digit = False
    special = False
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        else:
            special = True
    if len(password) >= 8 and upper and lower and digit and special:
        return "Strong"
    else:
        return "Weak"
password = "Abc@1234"
print("Password Strength:", check_password(password))
