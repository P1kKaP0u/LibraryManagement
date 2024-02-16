class Library:
    def __init__(self, filename):
       self.file = open(filename+".txt", "a+")
       self.file.seek(0)

       
    
    def Addbook(self,booktitle,bookauthor,bookreleaseyear,bookpagenumber):
        self.file.write(booktitle+","+bookauthor+","+bookreleaseyear+","+bookpagenumber+"\n")


    def ListBook(self):
        bookdetails = self.file.read().splitlines()        
        for book in bookdetails:
             bookdetail= book.split(",")
             print ("Book name:",bookdetail[0]+","+" Book author:",bookdetail[1])           
        


    

    def __del__(self):
        self.file.close()




while True:
    lib = Library("books")
    print("*****MENU*****")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.ListBook()
        print("******************************************************\n"+"Kitaplar başarılı bir şekilde listelendi")
    elif choice == '2':
        book_name = input("Input a book name: ")
        book_author = input("Input a book author: ")
        book_release_year = input("Input a book release year: ")
        book_page_number = input("Input a book page number: ")
        lib.Addbook(book_name,book_author,book_release_year,book_page_number)
        print("******************************************************\n"+"Kitap başarılı bir şekilde eklendi")
    elif choice == 'q':
        exit()
    else:
        print("Invalid choice")

