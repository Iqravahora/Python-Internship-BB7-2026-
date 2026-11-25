class Employee:
    def __init__(self, salary):
        self._salary = salary
        
    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        if salary > self._salary:
            self._salary = salary
            print("Salary increased")
        else:
            print("Salary cannot be decreased")
            
e = Employee(20000)
print("Old Salary:", e.get_salary())

e.set_salary(25000)
print("New Salary:", e.get_salary())

e.set_salary(15000)
print("Final Salary:", e.get_salary())

    