class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __eq__(self, other): #compresed both coordinate
        return self.a == other.a and self.b == other.b
    
    def __str__(self):#display the point as(x,y)
        return "(" + str(self.a) +", " + str(self.b) + ")"

p1 = Point(2,3)#x and y is equal return true
p2 = Point(2,3)

print(p1 == p2)
print(p1)


