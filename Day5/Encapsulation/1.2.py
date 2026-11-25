class Fraction:
    def __init__(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator =denomerator
        
                
    def __add__(self, other):
        n = self.numerator * other.denomerator + other.numerator * self.denomerator
        d = self.denomerator * other.denomerator 
        return Fraction(n , d)
    
    def __str__(self):
        return f"{self.numerator} / {self.denomerator}"
    
f1 = Fraction(1,4)
f2 = Fraction(1,3)

f3 = f1 + f2
print(f3)
    
        
        
        
        
        
        
        