tu=(234,678,433,22,44)

#add items
lst=list(tu)
lst.append(100)
tuple(lst)
print(lst)
print(len(lst))
for i in lst:
    if 433==i:
        print('Item found')
        break
print(lst[3])