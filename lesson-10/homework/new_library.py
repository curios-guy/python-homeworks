import json
import random

def create_unique_user_id():
    try:
        file = open("member_ids.txt", "r")
        member_ids = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        member_ids = []

    unique_id = random.randint(1000, 10000)

    while unique_id in member_ids:
        unique_id = random.randint(1000, 10000)

    member_ids.append(f"u{unique_id}")

    file = open("member_ids.txt", "w")
    json.dump(member_ids, file)

    return f"u{unique_id}"

def create_unique_book_id():
    try:
        file = open("book_ids.txt", "r")
        book_ids = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        book_ids = []

    unique_id = random.randint(1000, 10000)

    while unique_id in book_ids:
        unique_id = random.randint(1000, 10000)

    book_ids.append(f"b{unique_id}")

    file = open("book_ids.txt", "w")
    json.dump(book_ids, file)

    return f"b{unique_id}"

def file_saver(file_path, lst):
    file = open(str(file_path), "w")
    json.dump(lst, file, indent=4)

class Member():
    def __init__(self, uid, name, surname, borrowed_books = []):
        self.uid = uid
        self.name = name
        self.surname = surname
        self.borrowed_books = borrowed_books

class Book():
    def __init__(self, uid, title, author, is_borrowed = False):
        self.uid= uid
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class LibrarySystem():
    def add_member(self, uid, name, surname, borrowed_books = []):
        
        try:
            file = open("members.json", "r")
            members = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            members ={}

        member = Member(uid, name, surname, borrowed_books)

        members[member.uid] = {
            "name": member.name,
            "surname": member.surname,
            "borrowed_books": member.borrowed_books
        }

        file = open("members.json", "w")
        json.dump(members, file, indent=4)

    def add_book(self, uid, title, author, is_borrowed = False):
        
        try:
            file = open("books.json", "r")
            books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            books = {}

        book = Book(uid, title, author, is_borrowed)

        books[book.uid] = {
            "title": book.title,
            "author": book.author,
            "is_borrowed": book.is_borrowed
        }

        file_saver("books.json", books)


    def borrow_book(self, user_id, book_id):
        try:
            file = open("members.json", "r")
            members = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("\'Users\' Database is empty")

        try: 
            file = open("books.json", "r")
            books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("\'Books\' Database is empty")

        if user_id in members and book_id in books:
            if len(members[user_id]['borrowed_books']) >= 3:
                raise MemberLimitExceededException("User already borrowed 3 books")
            else:
                if books[book_id]["is_borrowed"] == True:
                    raise BookAlreadyBorrowedException(f"{book_id} has taken")
                else:
                    members[user_id]['borrowed_books'].append(f"{book_id}")
                    books[book_id]["is_borrowed"] = True
        elif user_id not in members:
            print(f"{user_id} not found") #user not found error
        elif book_id not in books:
            raise BookNotFoundException(f"{book_id} not found")

        file_saver("members.json", members)
        file_saver("books.json", books)
    
    def return_book(self, user_id, book_id):
        try:
            file = open("members.json", "r")
            members = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("\'Users\' Database is empty")

        try: 
            file = open("books.json", "r")
            books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("\'Books\' Database is empty")

        if user_id in members and book_id in books:
            if len(members[user_id]['borrowed_books']) == 0:
                print("User has no borrowed books") #enough books error
            else:
                if book_id in members[user_id]['borrowed_books']:
                    members[user_id]['borrowed_books'].remove(f"{book_id}")
                    books[book_id]["is_borrowed"] = False
                else: raise BookNotFoundException(message="Book not found on user")
        elif user_id not in members:
            print(f"{user_id} not found") #user not found error
        elif book_id not in books:
            raise BookNotFoundException(f"{book_id} not found")

        file_saver("members.json", members)
        file_saver("books.json", books)

class BookNotFoundException(Exception):
    def __init__(self, message = "Book not found"):
        super().__init__(message)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, message = "Book already taken"):
        super().__init__(message)

class MemberLimitExceededException(Exception):
    def __init__(self, message = "user has taken enough books"):
        super().__init__(message)


library = LibrarySystem()

while True:
    choice = int(input(f"\nChoose wisely:\n1. Add Member\n2. Add Book\n3. Borrowing book\n4. Returning book\n5. Quit\nChoose: "))

    if choice in [1,2,3,4,5]:
        if choice == 1:
            name = input("Name: ")
            surname = input("Surname: ")
            library.add_member(create_unique_user_id(), name, surname)
            print(f"\nMember added successfully!!!")

        elif choice == 2:
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(create_unique_book_id(), title, author)
            print("\nBook added successfully!!!")

        elif choice == 3:
            try:
                user_id = input("User ID: ")
                book_id = input("Book ID: ")
                library.borrow_book(user_id, book_id)
            except(BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as err:
                print(err)

        elif choice == 4:
            try: 
                user_id = input("User ID: ")
                book_id = input("Book ID: ")
                library.return_book(user_id, book_id)
            except(BookNotFoundException, BookAlreadyBorrowedException) as err:
                print(err)

        elif choice == 5:
            print("Thank you")
            break
    else: print("\nInvalid input. Choose wisely please!!!")
