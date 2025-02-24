class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa/cls.count}"

student1 = Student("Spogebob", 3.2)
student2 = Student("Patrick", 2.2)

students = [student1, student2]

print(Student.get_average_gpa())
print(Student.get_count())

for student in students:
    print(student.get_info())