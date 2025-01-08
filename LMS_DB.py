import mysql.connector

class Library:
    def __init__(self):
        # Connect to MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="library_db"
        )
        self.cursor = self.conn.cursor()
        self.list_books = []
        self.no_of_books = 0
        self.issued_books = []
    
    def fetch_books(self):
        # Fetch all books from the database
        self.cursor.execute("SELECT name FROM books WHERE issued = 0")
        self.list_books = [row[0] for row in self.cursor.fetchall()]
        self.no_of_books = len(self.list_books)
    
    def enter_new_book(self):
        book_name = input("ENTER BOOK NAME: ")
        # Insert new book into database
        query = "INSERT INTO books (name, issued) VALUES (%s, %s)"
        self.cursor.execute(query, (book_name, 0))
        self.conn.commit()
        print(f"Book '{book_name}' has been added.")
        self.fetch_books()
    
    def issue_book(self):
        book_name = input("ENTER BOOK NAME TO ISSUE: ")
        # Check if book exists and is available
        self.cursor.execute("SELECT * FROM books WHERE name = %s AND issued = 0", (book_name,))
        book = self.cursor.fetchone()
        
        if book:
            # Mark the book as issued
            query = "UPDATE books SET issued = 1 WHERE name = %s"
            self.cursor.execute(query, (book_name,))
            self.conn.commit()
            print(f"Book '{book_name}' has been issued.")
            self.fetch_books()
        else:
            print("Book is not available or already issued.")
    
    def search_book(self):
        book_name = input("ENTER BOOK NAME TO SEARCH: ")
        # Check if the book exists in the database
        self.cursor.execute("SELECT * FROM books WHERE name = %s", (book_name,))
        book = self.cursor.fetchone()
        
        if book:
            issued_status = "Issued" if book[2] else "Available"
            print(f"Book '{book_name}' is {issued_status}.")
        else:
            print(f"Book '{book_name}' is NOT AVAILABLE.")

# Main Program
print("!!!!!!!WELCOME TO LIBRARY MANAGEMENT SYSTEM!!!!!!!!!!!")
print("*****OPERATION*****")
print("1. ENTER NEW BOOK\n2. ISSUE BOOK\n3. SEARCH BOOK")
print("|****************************************|")
option = input("ENTER: ").capitalize()

# Create Library object
library = Library()
library.fetch_books()

# Match user input with operations
match option:
    case "1":
        library.enter_new_book()
    case "2":
        library.issue_book()
    case "3":
        library.search_book()
    case _:
        print("Invalid Option!")

# Close connection
library.cursor.close()
library.conn.close()
