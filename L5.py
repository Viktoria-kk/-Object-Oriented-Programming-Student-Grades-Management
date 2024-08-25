#Student class
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):

        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0

    def __str__(self):
        average = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {average:.2f}"

# Classroom class
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):

        sorted_students = sorted(self.students, key=lambda ave: ave.get_average_grade(), reverse=True)
        return sorted_students[:3]

    def get_failed_students(self):
        return [student for student in self.students if student.get_average_grade() < 51]
