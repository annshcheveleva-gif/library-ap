from client import Client

api = Client()

def get_books():
    return api.get_books()

def get_book(book_id):
    return api.get_book(book_id)

def create_book(data):
    return api.create_book(data)

def delete_book(book_id):
    return api.delete_book(book_id)