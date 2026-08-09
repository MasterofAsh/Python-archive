# Exercise 6
# Library Management System

# Instructions:
"""
1. Make a Library Class with 2 instance variables; no_of_books(int) and books(list)
2. Check to see if the length of no_of_books is equal to length of books.
3. Make a proper working library, that allows for;
- Storing of a Book(s)
- Taking a book(s)
- Updating the number of books after storing or taking
4. Check to see that the books stored in the program, get reset after starting the program again
5. Create a Library class, that allows for library objects to be made, and every object shares the same
features; storing, taking and updating number of books.
"""

# class Library:
#     quitLibrary = False
#     bookList = ["Book1", "Book2", "Book3"]
#     totalBooks = 3
#     print("Welcome to the library. \nWhat would you like to do?")
#     Input = input("Take a Book \nStore a Book \nQuit \nAction(T / S / Quit): ")

#     def takeBook(self):
#         bookTaken = False
#         print(f"Which book would you like to take?")
#         userBook = input(f"Books: {self.bookList}\nSelect a book by the corresponding number.\n")
#         while (bookTaken == False):
#             if (userBook == "1"):
#                 print("Book 1 Chosen")
#                 bookTaken = True
#                 self.bookList.pop(0)

#             elif (userBook == "2"):
#                 print("Book 2 Chosen")
#                 bookTaken = True
#                 self.bookList.pop(1)

#             elif (userBook == "3"):
#                 print("Book 3 Chosen")
#                 bookTaken = True
#                 self.bookList.pop(2)

#             else:
#                 print("Choose a book from the list.\n")
#                 self.quitLibrary = True
#                 break

#         if (bookTaken == True):
#             self.totalBooks = self.totalBooks - 1
#             print(f"Books remaining now: {self.bookList}")
#             print(f"Number of books left: {self.totalBooks}\n")
#             self.quitLibrary = True

#     def storeBook(self):
#         bookName = input("What is the book you want to store? \nBook: ")
#         self.bookList.append(bookName)
#         print("Books in Library now: ", self.bookList)
#         self.totalBooks = self.totalBooks + 1
#         print("Number of books now: ", self.totalBooks)
#         self.quitLibrary = True

#     def showInfo(self):
#         print("Showing information about Library \n")
#         print(f"Length of bookList: {len(self.bookList)}\nTotal Books: {self.totalBooks}")
        
# a = Library()

# while (a.quitLibrary == False):
#     if (a.Input == "T"):
#         a.takeBook()
#         # break
#     elif (a.Input == "S"):
#         a.storeBook()
#         # break
# a.showInfo()

# b = Library()
# b.showInfo()


class Library:
    def __init__(self):
        self.totalBooks = 0
        self.Books = []

    def addBook(self, book):
        self.Books.append(book)
        self.totalBooks = len(self.Books)

    def showInfo(self):
        print(f"The library has {self.totalBooks} book(s)")

    def displayBooks(self):
        for x in self.Books:
            print(x)

l1 = Library()
l1.addBook("Amongus")
l1.addBook("Sugoma")
l1.displayBooks()
l1.showInfo()

l2 = Library()
l2.addBook("Sigma Balls")
l2.displayBooks()
l2.showInfo()

# exampleList = [1, 2, 3, 4, 5]
# for x in exampleList:
#     print(x)