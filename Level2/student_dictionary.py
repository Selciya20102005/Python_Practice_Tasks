student = {
    "name": "Selciya K",
    "age": 20,
    "grade": "A",
    "subject": "Python"
}
for key, value in student.items():
    print(f"{key}: {value}")

student["passed"] = True

print(student)