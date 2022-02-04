# Create a class Publisher (name). Derive class Book from Publisher with attributes title and
# author. Derive class Python from Book with attributes price and no_of_pages. Write a
# program that displays information about a Python book. Use base class constructor invocation and
# method overriding. 

class Publisher:
    def __init__(self, name):
        self._name = name
        
    def display(self):
        print("Name of the publisher is: ", self._name)
    
    
class Book(Publisher):
    def __init__(self, title, author):
        Publisher.__init__(self, name)
        self._title = title
        self._author = author
    def display(self):
        print("Title of the book is: ", self._title)
        print("Author of the book is: ", self._author)
        Publisher.display(self)

class Python(Book):
    def __init__(self, price, no_of_pages):
        Book.__init__(self, title, author)
        self._price = price
        self._no_of_pages = no_of_pages
    def display(self):
        Publisher.display(self)
        Book.display(self)
        print("Price of the book is: ", self._price)
        print("Number of pages of the book is: ", self._no_of_pages)


name=input("Enter the name of the publisher: ")
title=input("Enter the title of the book: ")
author=input("Enter the author of the book: ")
price=int(input("Enter the price of the book: "))
no_of_pages=int(input("Enter the number of pages of the book: "))
print("----------------------------------------------------------------")

c1=Publisher(name)
c2=Book(title,author)
c3=Python(price,no_of_pages)
# c1.display()
# c2.display()
c3.display()



