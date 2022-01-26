def max_num(a,b,c):
    if a<b and a<c:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)

a=int(input('enter the 1st number'))
b=int(input('enter the 2nd number'))
c=int(input('enter the 3rd number'))
max_num(a,b,c)