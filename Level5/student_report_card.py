class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def get_average(self):
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return average

    def report(self):
       
        print(f"Name : {self.name}")
        print(f"ID   : {self.student_id}")

        print("\nSubjects")

        for subject, score in self.grades.items():
            print(subject, ":", score)

        print(f"\nAverage : {self.get_average():.2f}")


student = Student("John", 101)

student.add_grade("Math", 90)
student.add_grade("Science", 85)
student.add_grade("English", 95)

student.report()