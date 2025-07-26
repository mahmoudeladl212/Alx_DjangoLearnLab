# Alx_DjangoLearnLab/django-models/relationship_app/query_samples.py

import os
import django
import sys # Import sys

# Get the path to the Django project root (where manage.py is)
# This assumes query_samples.py is in 'relationship_app' and 'relationship_app' is in the project root.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root) # Add the project root to the Python path

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_sample_queries():
    # Clean up previous data (optional, for fresh runs)
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create sample data
    author1 = Author.objects.create(name="Jane Doe")
    author2 = Author.objects.create(name="John Smith")

    book1 = Book.objects.create(title="The First Book", author=author1)
    book2 = Book.objects.create(title="The Second Book", author=author1)
    book3 = Book.objects.create(title="Another Book", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book3)

    library2 = Library.objects.create(name="Community Library")
    library2.books.add(book2)

    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Williams", library=library2)


    print("\n--- Sample Queries ---")

    # Query all books by a specific author.
    print("\n1. Books by Jane Doe:")
    jane_doe_books = Book.objects.filter(author=author1)
    for book in jane_doe_books:
        print(f"- {book.title} (Author: {book.author.name})")

    # List all books in a library.
    print("\n2. Books in Central Library:")
    central_library_books = library1.books.all()
    for book in central_library_books:
        print(f"- {book.title}")

    # Retrieve the librarian for a library.
    print("\n3. Librarian for Central Library:")
    try:
        central_librarian = library1.librarian
        print(f"- {central_librarian.name}")
    except Librarian.DoesNotExist:
        print("No librarian found for Central Library.")

    print("\n4. Librarian for Community Library:")
    try:
        community_librarian = library2.librarian
        print(f"- {community_librarian.name}")
    except Librarian.DoesNotExist:
        print("No librarian found for Community Library.")

if __name__ == '__main__':
    run_sample_queries()