import math

class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def length(self):
        return math.sqrt(self.x2*self.x2 - self.x1*self.x1)
    
    def __str__(self):
        return str(f"({self.x1}, {self.y1}, {self.x2}, {self.y2})")
    
class Vectors2(Vector):

    def __init__(self, x1,y1,x2,y2,x3,y3):
        super().__init__(x1,y1,x2,y2)
        self.x3 = x3
        self.y3 = y3
 
    
    def summ(self):
        result = Vector(self.x1,self.y1, self.x2+self.x3, self.y2+self.y3) 
        return result
    
vec1 = Vector(0,0,1,1)
vec2 = Vector(0,0,1,1)

print(vec1)

vector_2 = Vectors2(0,0,1,1,2,0)

print(vector_2.summ())