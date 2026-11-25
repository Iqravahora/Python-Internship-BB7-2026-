class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        
    def display_info(self):
        print(f"car is {self.year} {self.brand} {self.model}")
        
car1 = Car("Mahindra", "thar", 2024)
car2 =Car("Audi","A6", 2025)
car3 = Car("BMW","X5", 2025)

car1.display_info()
car2.display_info()
car3.display_info()