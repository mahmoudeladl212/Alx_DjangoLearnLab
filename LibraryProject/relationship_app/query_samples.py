#!/usr/bin/env python3
"""Sample queries for relationship_app models."""

import os
import sys
import django

# Add the project directory to the Python path
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Helper function to create sample data for testing."""
    # Clear existing data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")

    # Create books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter", author=author2)

    # Create library
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2, book3)

    # Create librarian
    librarian = Librarian.objects.create(name="John Doe", library=library)

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")
        return None

def query_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name} library:")
        for book in books:
            print(f"- {book.title} (by {book.author.name})")
        return books
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
        return None

def query_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for library: {library_name}")
        return None

if __name__ == '__main__':
    # Create sample data (run only once)
    print("Creating sample data...")
    create_sample_data()
    
    # Example queries
    print("\n=== Query 1: Books by George Orwell ===")
    query_books_by_author("George Orwell")

    print("\n=== Query 2: Books in Central Library ===")
    query_books_in_library("Central Library")

    print("\n=== Query 3: Librarian for Central Library ===")
    query_librarian_for_library("Central Library")