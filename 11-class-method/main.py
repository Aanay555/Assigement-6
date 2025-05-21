class Book():
    total_books = 0  # class variable

    @classmethod
    def increament_book_count(cls):
        cls.total_books +=1

if __name__ == "__main__":
    Book.increament_book_count()
    Book.increament_book_count()
    Book.increament_book_count()
    
    print(f"Total BOOKS ADDED: {Book.total_books}")        