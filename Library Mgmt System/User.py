# -*- coding: utf-8 -*-
#from Book import Book
from Catalog import Catalog
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.books = []
        self.different_book_count = 0
        self.total_count = 0
        self.isbn = ''
        self.rack = ''
        self.book_item = []
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,days=10):
        pass
    
    #assume name is unique
    def returnBook(self,name):
        pass
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
  
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages):
        b = Catalog.addBook(self,name,author,publish_date,pages)
        return b
    
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
        
    # This will help to see the books added 
    def seeBooksInCatalog(self):
        Catalog.displayAllBooks(self)
        
    
    def removeBook(self,name):
        book_name_exist= [(book,book.name) for book in self.books if name == book.name]
        if book_name_exist:
            self.books.remove(book_name_exist[0][0])
            print('The books remaining after removal are:-')
            Librarian.seeBooksInCatalog(self)
        else:
            print('This book does not exist.')
        
        
        
        



                
        
        
    
    
        