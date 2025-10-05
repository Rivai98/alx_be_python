import unittest
from library_management import Book, Library


class TestBook(unittest.TestCase):
    """Test cases for the Book class."""

    def setUp(self):
        """Set up a Book instance before each test."""
        self.book = Book("1984", "George Orwell")

    def test_book_initialization(self):
        """Test that a book is initialized with correct attributes."""
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertTrue(self.book.is_available())

    def test_check_out(self):
        """Test checking out a book."""
        self.book.check_out()
        self.assertFalse(self.book.is_available())

    def test_return_book(self):
        """Test returning a book."""
        self.book.check_out()
        self.assertFalse(self.book.is_available())
        self.book.return_book()
        self.assertTrue(self.book.is_available())

    def test_multiple_checkouts(self):
        """Test multiple check out and return operations."""
        # Check out
        self.book.check_out()
        self.assertFalse(self.book.is_available())
        
        # Check out again (should still be checked out)
        self.book.check_out()
        self.assertFalse(self.book.is_available())
        
        # Return
        self.book.return_book()
        self.assertTrue(self.book.is_available())
        
        # Return again (should still be available)
        self.book.return_book()
        self.assertTrue(self.book.is_available())


class TestLibrary(unittest.TestCase):
    """Test cases for the Library class."""

    def setUp(self):
        """Set up a Library instance before each test."""
        self.library = Library()
        self.book1 = Book("1984", "George Orwell")
        self.book2 = Book("Brave New World", "Aldous Huxley")
        self.book3 = Book("Animal Farm", "George Orwell")

    def test_library_initialization(self):
        """Test that a library is initialized with an empty collection."""
        # The library should start empty
        self.assertEqual(len(self.library._books), 0)

    def test_add_book(self):
        """Test adding books to the library."""
        self.library.add_book(self.book1)
        self.assertEqual(len(self.library._books), 1)
        
        self.library.add_book(self.book2)
        self.assertEqual(len(self.library._books), 2)

    def test_add_multiple_books(self):
        """Test adding multiple books to the library."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        self.assertEqual(len(self.library._books), 3)

    def test_check_out_book(self):
        """Test checking out a book from the library."""
        self.library.add_book(self.book1)
        self.library.check_out_book("1984")
        self.assertFalse(self.book1.is_available())

    def test_check_out_nonexistent_book(self):
        """Test checking out a book that doesn't exist."""
        self.library.add_book(self.book1)
        # Should not raise an error, just print a message
        self.library.check_out_book("Nonexistent Book")

    def test_check_out_already_checked_out_book(self):
        """Test checking out a book that's already checked out."""
        self.library.add_book(self.book1)
        self.library.check_out_book("1984")
        # Try to check out again
        self.library.check_out_book("1984")
        self.assertFalse(self.book1.is_available())

    def test_return_book(self):
        """Test returning a book to the library."""
        self.library.add_book(self.book1)
        self.library.check_out_book("1984")
        self.assertFalse(self.book1.is_available())
        
        self.library.return_book("1984")
        self.assertTrue(self.book1.is_available())

    def test_return_nonexistent_book(self):
        """Test returning a book that doesn't exist."""
        self.library.add_book(self.book1)
        # Should not raise an error, just print a message
        self.library.return_book("Nonexistent Book")

    def test_return_available_book(self):
        """Test returning a book that wasn't checked out."""
        self.library.add_book(self.book1)
        # Book is available, try to return it
        self.library.return_book("1984")
        self.assertTrue(self.book1.is_available())

    def test_list_available_books(self):
        """Test listing available books."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        
        # All books should be available initially
        # This test verifies the method runs without error
        self.library.list_available_books()

    def test_list_available_books_with_checked_out(self):
        """Test listing available books when some are checked out."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        
        # Check out one book
        self.library.check_out_book("1984")
        
        # Count available books
        available_books = [book for book in self.library._books if book.is_available()]
        self.assertEqual(len(available_books), 2)

    def test_list_available_books_all_checked_out(self):
        """Test listing available books when all are checked out."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        
        # Check out all books
        self.library.check_out_book("1984")
        self.library.check_out_book("Brave New World")
        
        # Count available books
        available_books = [book for book in self.library._books if book.is_available()]
        self.assertEqual(len(available_books), 0)

    def test_workflow(self):
        """Test a complete workflow of library operations."""
        # Add books
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        
        # Check out a book
        self.library.check_out_book("1984")
        self.assertFalse(self.book1.is_available())
        self.assertTrue(self.book2.is_available())
        
        # Return the book
        self.library.return_book("1984")
        self.assertTrue(self.book1.is_available())
        self.assertTrue(self.book2.is_available())
        
        # Check out another book
        self.library.check_out_book("Brave New World")
        self.assertTrue(self.book1.is_available())
        self.assertFalse(self.book2.is_available())


if __name__ == '__main__':
    unittest.main()
