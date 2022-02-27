# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)

#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Library:
    def __init__(self,list,name):
        self.booksList=list
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self,user,book):
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print("Lender-Book database has been updated.You can take the book now")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added successfully")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    arpan=Library(["CookBook","How To Do Sex","Rich Dad Poor Dad","Harry Potter"],"ArpanMaheshwari")

    while(True):
        print(f"Welcome to the {arpan.name} library.Enter your choice to continue: ")
        print("1. Display Books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            arpan.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            arpan.lendBook(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            arpan.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book which you want to return:")
            arpan.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = " "     #input() function returns a string
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            if user_choice2 == "c":
                continue


                #or

# class Library:
#     dict = {}
#     def __init__(self, lst,ln):
#         self.lst = lst.split(",")
#         self.ln = ln
#         print(f"Your library is created by name of {self.ln} and you have Following Books: {self.lst}")
#     def see_option_again(self):
#         print("1.To see all these options again(Remember 1 for future use)")
#         print("2.To see all issued book")
#         print("3.To see all unissued books")
#         print("4.To add new Book")
#         print("5.To retun Book")
#         print("6.To lend-Book")
#         print("7.To exit")
#     def issuedBooks(self):
#         if not bool(self.dict):
#             print("\nNo book is issued yet")
#         else:
#             print("\nFollowing are all issued books with their owner ")
#             for key,values in self.dict.items():
#                print(values,":",key)
#     def unissuedBooks(self):
#         print("\n Following are all unissued Books:")
#         print(self.lst)
#     def addBook(self):
#         book = input("Add the name of Book which you want to add into the library:")
#         if book in self.lst:
#            print("The book is already present in library")
#         else:
#          self.lst.append(book)
#          print("\nNew Book is successfully added")
#     def returnBook(self):
#         owner = input("Enter the name of owner:")
#         book = input("Enter the name of Book")
#         if book in self.dict and owner in self.dict.values():
#             self.lst.append(book)
#             del self.dict[book]
#             print("\nYour Book is successfully returned")
#         else:
#             print("\nSorry,Book is not issued to you")
#     def lendBook(self):
#         book = input("Enter the name of book which you want to issue:")
#         t = 0
#         if book in self.lst:
#                 t =1
#         if t == 1:
#             owner = input("Enter the name of person who want issue this book")
#             self.dict.update({book:owner})
#             self.lst.remove(book)
#             print("\nBook is successfully issued to a person")
#         if t == 0:
#             for key,values in self.dict.items():
#                 if key == book:
#                     print(f"\nThe book is already issued to {values}")
#                     t = 1
#         if t == 0:
#             print("\nSorry the library does not have this book and  not issued to anyone")
#
# print("Hello lets create our own online Library")
# ln = input("Enter the name of your library")
# lst = input("Enter the list of books which you want to place (separated by comma, donot enter books of same name):")
# lib = Library(lst,ln)
# print("\n")
# lib.see_option_again()
# print("\n")
# i = int(input("Enter your Choice"))
# while i != 7:
#     if i == 1:
#         lib.see_option_again()
#     elif i == 2:
#         lib.issuedBooks()
#     elif i == 3:
#         lib.unissuedBooks()
#     elif i == 4:
#         lib.addBook()
#     elif i == 5:
#         lib.returnBook()
#     elif i == 6:
#         lib.lendBook()
#     elif i == 7:
#         break
#     else:
#         print("Please Enter valid choice\n")
#     i = int(input("\nEnter your choice"))
# print("Thanks for using it!!")