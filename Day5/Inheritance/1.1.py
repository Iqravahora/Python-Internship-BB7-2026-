class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
        
    def study(self):
        print(self.name,"is studying", self.course)
        
s1 = Student("Iqra", 20, "Python")
s1.show()
s1.study()