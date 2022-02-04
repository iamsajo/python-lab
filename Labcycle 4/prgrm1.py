
class Rectangle:
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)


l=float(input("Enter length of rectangle: "))
b=float(input("Enter breadth of rectangle: "))
rect=Rectangle(l,b)
print("Area of rectangle is: ",rect.area())
print("Perimeter of rectangle is: ",rect.perimeter())
