new=('qwertyy','abcde','python','java','django')
a='0'
for i in new:
    a=i if len(i)>len(a) else a
print(a)
