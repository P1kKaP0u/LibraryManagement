class Library:
    def __init__(self, filename):
       self.file = open(filename+".txt", "a+")
       self.file.seek(0)

       
    
    def Addbook(self,booktitle,bookauthor,bookreleaseyear,bookpagenumber):
        self.file.write(f"\n{booktitle}\n{bookauthor}\n{bookreleaseyear}\n{bookpagenumber}")


    def ListBook(self):
        print(self.file.read())

lib = Library("books")

        

book_name = input("Input a book name: ")
book_author = input("Input a book author: ")
book_release_year = input("Input a book release year: ")
book_page_number = input("Input a book page number: ")
lib.Addbook(book_name,book_author,book_release_year,book_page_number)

lib.ListBook()