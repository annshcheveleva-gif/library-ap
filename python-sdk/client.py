import requests

class Client:
    def __init__(self, base_url="https://example.com/api"):
        self.base_url = base_url

    def get_books(self):
        response = requests.get(f"{self.base_url}/books")
        return response.json()

    def get_book(self, book_id):
        response = requests.get(f"{self.base_url}/books/{book_id}")
        return response.json()

    def create_book(self, data):
        response = requests.post(f"{self.base_url}/books", json=data)
        return response.json()

    def delete_book(self, book_id):
        response = requests.delete(f"{self.base_url}/books/{book_id}")
        return response.json()