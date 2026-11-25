class vehicle:
    def __init__(self, brand):
        self.brand = brand
        
class Car(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed
        
    def show_into(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Top Speed:", self.top_speed)
        
s1 = SportsCar("BMW", "M4", "290 km/h")
s1.show_into()