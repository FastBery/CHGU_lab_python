#Задание 1
class PhoneCall:
    def __init__(self, n = 0, s = 0):
        self.price = s
        self.minutes = n

    def summ(self):
        return self.price * self.minutes

    def __str__(self):
        string = 'Price: ' + str(self.price) + '\n' \
            + 'Minutes: ' + str(self.minutes)
        return string

call = PhoneCall(20, 0.5)

print(call)
print(call.summ())
#Задание 2
from math import sqrt
class Vector2D:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def __str__(self):
        string = f'({self.x1},{self.y1}) : ({self.x2-self.x1}, {self.y2-self.y1})'
        return string
    def double(self):
        self.x2 *= 2
        self.y2 *= 2
    def is45(self):
        cdx = self.x2-self.x1
        cdy = self.y2-self.y1
        l = sqrt(cdx*cdx + cdy*cdy)
        if cdx/l == cdy/l:
            return True
        else:
            return False
    def __del__(self):
        del self
        print('Vector2D deleted')

vec = Vector2D(0,0,1,1)
print(vec.is45())
print(vec)
del vec
