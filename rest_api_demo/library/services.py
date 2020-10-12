from rest_api_demo.database import db
from rest_api_demo.library.models import Author, Book


def create_author(data):
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    author_id = data.get('id')

    author = Author(first_name, last_name)
    if author_id:
        author.id = author_id

    db.session.add(author)
    db.session.commit()


def update_author(author_id, data):
    author = Author.query.filter(Author.id == author_id).one()
    author.first_name = data.get('first_name')
    author.last_name = data.get('last_name')
    db.session.add(author)
    db.session.commit()


def delete_author(author_id):
    author = Author.query.filter(Author.id == author_id).one()
    db.session.delete(author)
    db.session.commit()


def create_book(data):
    title = data.get('title')
    isbn = data.get('isbn')
    number_of_pages = data.get('number_of_pages')
    published_date = data.get('published_date')
    description = data.get('description')
    book_id = data.get('id')
    author_id = data.get('author_id')
    author = Author.query.filter(Author.id == author_id).one()

    book = Book(title, isbn, number_of_pages, description, author, published_date)
    if book_id:
        book.id = book_id

    db.session.add(book)
    db.session.commit()


def update_book(book_id, data):
    book = Book.query.filter(Book.id == book_id).one()
    book.title = data.get('title')
    book.isbn = data.get('isbn')
    book.number_of_pages = data.get('number_of_pages')
    book.published_date = data.get('published_date')
    book.description = data.get('description')
    db.session.add(book)
    db.session.commit()


def delete_book(book_id):
    book = Book.query.filter(Book.id == book_id).one()
    db.session.delete(book)
    db.session.commit()
