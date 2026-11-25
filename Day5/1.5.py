class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        
    @property
    def celsius(self):
        return self._celcius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15 C .that's Zero")
        self._celcius = value
        
    @property
    def kelvin(self):
        return self._celcius + 273.15
    
    
s1 = Temperature(25)
print(s1.celsius)
print(s1.kelvin)
        
        
        
    
