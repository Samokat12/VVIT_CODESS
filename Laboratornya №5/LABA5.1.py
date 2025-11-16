class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
book = Book("Woosh: The First UK Drill Book", "Ian McQuaid, Tim & Barry", 2024)
print(book.get_info())