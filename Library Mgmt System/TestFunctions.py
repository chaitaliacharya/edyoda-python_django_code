# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

b1 = Book('Shoe Dog','Phil Knight', '2015',312)
b1.addBookItem('123hg','H1B2')
b1.addBookItem('124hg','H1B3')

b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

catalog.displayAllBooks()

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
print (m1)
print (librarian)

#m1.issueBook

#Adding the book -> by Librarian
librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
b1 = Librarian.addBook(librarian ,'Handmaids Tale','Margaret Attwood',2018, 300)
Librarian.addBookItem(librarian,b1,'411HS','A1B1')
Librarian.addBookItem(librarian,b1,'412HS','A1B2')
Librarian.addBookItem(librarian,b1,'413HS','A1B3')
Librarian.addBookItem(librarian,b1,'414HS','A1B4')


b2 = Librarian.addBook(librarian ,'MyGita','Devdutt Patnaik',2017, 300)
Librarian.addBookItem(librarian,b2,'415HS','A1B5')
Librarian.addBookItem(librarian,b2,'416HS','A1B6')

Librarian.seeBooksInCatalog(librarian)

#Remove Book 

Librarian.removeBook(librarian,'MyGit')
Librarian.removeBook(librarian,'MyGit')


catalog = Catalog()
b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

catalog.searchByName(b,'MyGita')







