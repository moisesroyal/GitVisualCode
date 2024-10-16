class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hola, soy una persona")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"hola mi ID de estudiante es {self.student_id}")

student = Student("Luis", 20, "S123")
student.greet()
    
    