# Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to
# compare the area of 2 rectangles. 

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def __lt__(self, other):
        return self.area() < other.area()

    def area(self):
        return self._length * self._width
    
    def __add__(self, other):
        return self.area() - other.area()
    
l=int(input("enter the length: "))
w=int(input("enter the width: "))
l1=int(input("enter the length: "))
w1=int(input("enter the width: "))
r1=Rectangle(l,w)
r2=Rectangle(l1,w1)
print(r1<r2)




