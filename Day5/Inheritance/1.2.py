class Employee:
    def calculate_salary(self):
        return 40000
    
class Developer(Employee):
    def calculate_salary(self):
        salary = super().calculate_salary()
        bonus = 10000
        return salary + bonus

class Designer(Employee):
    def calculate_salary(self):
        salary = super().calculate_salary()
        bonus = 5000
        return salary + bonus

d = Developer()
print("Developer Salary:", d.calculate_salary())

s = Designer()
print("Designer Salary:", s.calculate_salary())