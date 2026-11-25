class Bird:
    def fly(self):
        print("Birds is flying")
        
class Airplane:
    def fly(self):
        print("Airplane is flying")
        
class Drone:
    def fly(self):
        print("Drone is flying")
        
        
def flying(obj):
     obj.fly()       
        
a = Bird()
b = Airplane()
c = Drone()

flying(a)
flying(b)
flying(c)        
        
