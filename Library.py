import os

class Library:
    def __init__(self):
       self.file = open("books.txt", "a+", encoding="utf-8")
       self.file.seek(0)

    
    def Addbook(self,booktitle,bookauthor,bookreleaseyear,bookpagenumber):
        self.file.write(booktitle+","+bookauthor+","+bookreleaseyear+","+bookpagenumber+"\n")


    def ListBook(self):
        bookdetails = self.file.read().splitlines()        
        for book in bookdetails:
             bookdetail= book.split(",")
             print ("Book name:",bookdetail[0]+","+" Book author:",bookdetail[1])           
               

    def RemoveBook(self,booktitle):
        bookdetailes = self.file.read().splitlines()
        for book in bookdetailes:
            bookdetail= book.split(",")
            if bookdetail[0] == booktitle:
                bookdetailes.remove(book)
                self.file.close()
                os.remove("books.txt")     
                for book in bookdetailes:
                    self.file = open("books.txt", "a+", encoding="utf-8")
                    self.file.seek(0)
                    self.file.write(book+"\n")                   

    def __del__(self):
        self.file.close()



while True:
    lib = Library()
    print("*****MENU*****")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.ListBook()
        print("******************************************************\n"+"Books are listed successfully") #true or false?
    elif choice == '2':
        book_name = input("Input a book name: ")
        book_author = input("Input a book author: ")
        book_release_year = input("Input a book release year: ")
        book_page_number = input("Input a book page number: ")
        lib.Addbook(book_name,book_author,book_release_year,book_page_number)
        print("******************************************************\n"+"The book is added successfully")
    elif choice == '3':
        book_name = input("Input a book name to delete: ")
        lib.RemoveBook(book_name)
        print("******************************************************\n"+"The book is deleted successfully")
    elif choice == 'q':
        exit()
    else:
        print("******************************************************\n"+"Invalid choice")

