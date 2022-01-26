from math import pi

def area_peri(r):
    print('area of a circle is : ',(pi*r)**2)
    print('perimeter of a circle is : ',2*pi*r)

r=int(input('enter the radius'))
area_peri(r)