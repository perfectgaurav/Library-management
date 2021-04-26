class Library:
    def __init__(self, List_of_books):
        self.books = List_of_books

    def display(self):
        print("list of books are")
        for book in self.books:
            print("* "+book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print("Ur book has been issued")
            self.books.remove(bookname)
            return True
        else:
            print("book is not available")
            return False

    def returnbook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:

    def requestbook(self):
        print("enter name of book")
        self.books = input()
        return self.books

    def returnbook(self):
        print("enter name of book")
        self.books = input()
        return self.books


obj = Library(["Data Structure", "Digital Electronics","Software Engg.", "Python"])
              

ob = Student()


while(True):

    msg = '''***********Welcome TO Central Library**************
    Plz Choose a option:
    1.List Of Books
    2.Borrow a book
    3.Return/Add a book
    4.Exit Library'''
    print(msg)
    choice = int(input("enter a option: "))
    if choice == 1:
        obj.display()
    elif choice == 2:
        obj.borrowbook(ob.requestbook())
    elif choice == 3:
        obj.returnbook(ob.returnbook())
    elif choice == 4:
        exit()
    else:
        print("valid input")
