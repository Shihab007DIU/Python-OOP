class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department

    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Email:", self.__email)
        print("Age:", self.age)
        print("Department:", self.department)

    def calculate_result(self, *marks):
        if len(marks) == 0:
            return 0

        total = sum(marks)
        average = total / len(marks)
        return average

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print("Semester:", self.semester)


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print("Research Topic:", self.research_topic)


student1 = UndergraduateStudent(
    "Rahim",
    "SWE101",
    "rahim@gmail.com",
    21,
    "Software Engineering",
    5
)

student2 = GraduateStudent(
    "Karim",
    "SWE201",
    "karim@gmail.com",
    25,
    "Software Engineering",
    "Artificial Intelligence"
)


print("Undergraduate Student")
student1.display_info()
print("Student Type:", student1.get_student_type())

print("\nGraduate Student")
student2.display_info()
print("Student Type:", student2.get_student_type())


print("\nResult Calculation")

result1 = student1.calculate_result(80, 75, 90)
print("Undergraduate Average:", result1)

result2 = student2.calculate_result(85, 88, 92, 90)
print("Graduate Average:", result2)


print("\nPolymorphism")

students = [student1, student2]

for student in students:
    print(student.get_student_type())