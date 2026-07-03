def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_details(
    Name="Selciya",
    Age=21,
    Department="IT",
    Salary=35000
)