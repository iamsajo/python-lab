num=int(input('enter the number'))
s=0
for i in str(num):
    s+=int(i)**3
print('Armstrong' if s==num else 'not a palindrom')