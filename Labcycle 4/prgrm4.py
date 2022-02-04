# Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
# find sum of 2 time. 

class Time:
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second
        
    def __add__(self, other):
        return 'time is: ' + str(self._hour + other._hour) + ':' + str(self._minute + other._minute) + ':' + str(self._second + other._second)
    

h=int(input("enter the hour: "))
m=int(input("enter the minute: "))
s=int(input("enter the second: "))
h1=int(input("enter the hour: "))
m1=int(input("enter the minute: "))
s1=int(input("enter the second: "))
t1=Time(h,m,s)
t2=Time(h1,m1,s1)
print(t1+t2)