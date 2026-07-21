import json

class Book:
    def __init__(self,book_id,title,author,quantity):
        self.book_id= book_id
        self.title= title
        self.author= author
        self.quantity = quantity
            

class Library:
    def __init__(self):
        self.books = {}
            
            
    def add_book(self):
        book_id = input("\nEnter book id :- ")
        if book_id in self.books:
            print("Book id already exists")
            return
            
        title= input("Enter title :- ")
        author= input("Enter author name :- ")
        quantity = int(input("Enter quantity :- "))
        if quantity <= 0:
            print("please enter valid data")
            return
            
        book1 = Book(book_id,title,author,quantity)
            
        self.books[book_id]= book1
            
    def view_book(self):
        if len(self.books)== 0:
            print("No Books is available")
        
        else:
            print("Book id     Title          Author name      Quantity")
            print("------------------------------------------------------\n")
            for Book in self.books.values():
                print(f"{Book.book_id:<12}{Book.title:<15}{Book.author:<15}{Book.quantity}")
            
            
    def search_book(self):
        user_p= input("\nEnter book id :- ")
        
        if user_p in self.books:
            Book= self.books[user_p]
            print(f"\nBook id = {Book.book_id}")
            print(f"Title = {Book.title}")
            print(f"Author name = {Book.author}")
            print(f"Quantity = {Book.quantity}")
            
        else:
            print("No book is available")
            
            
    def update_book(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        self.view_book()

        user_pp = input("\nEnter book id to update: ")

        if user_pp in self.books:
            book = self.books[user_pp]

            new_book_id = input("Enter new book id: ")
            title = input("Enter new title: ")
            author = input("Enter new author name: ")
            quantity = int(input("Enter new quantity: "))

            # Update dictionary key if book ID changes
            if new_book_id != user_pp:
                self.books[new_book_id] = self.books.pop(user_pp)

            # Update object attributes
            book.book_id = new_book_id
            book.title = title
            book.author = author
            book.quantity = quantity

            print("Book updated successfully.")

        else:
            print("No book found.")
               
    def delete_book(self):
        if len(self.books)== 0:
            print("No book is available")
            
        else:
            self.view_book()
            user_sp= input("\nEnter book id for delete :- ")
            if user_sp in self.books:
                self.books.pop(user_sp)
                print("\nBook deleted successfully")
                
            else:
                print("\nNo book found")
                    
        
            
        
        
            
user= Library()

while True:
    print("Press 1 for Add book :- ")
    print("Press 2 for View book :- ")
    print("Press 3 for Search book :- ")
    print("Press 4 for update book :- ")
    print("Press 5 for delete book :- ")
    print("Press 6 for issue book :- ")
    print("Press 7 for return book :- ")

    check = int(input("Enter, what to do :- "))


       

            
    if check == 1:
        user.add_book()
        
    elif check ==2 :
        user.view_book()
        
    elif check == 3:
        user.search_book()
        
    elif check == 4:
        user.update_book()
        
    elif check == 5:
        user.delete_book()
        
        
    user_l =input("do you want to do again [yes/no]:- ").lower() .strip()
    
    if user_l == "yes":
        continue

    elif user_l== "no":
        print("THANKS for using library management program")
        break
    else:
        print("Invalid input! please enter only 'yes' or 'no'.")