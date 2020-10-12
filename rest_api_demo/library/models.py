# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from rest_api_demo.database import db


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    fullname = db.column_property(first_name + " " + last_name)

    # books = db.relationship('Book', back_populates='author', cascade='all, delete-orphan')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(13), nullable=False, unique=True)
    number_of_pages = db.Column(db.Integer, nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    # author = db.relationship('Author', back_populates='books')

    # author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    # author = db.relationship('Author', back_populates='books')
    author = db.relationship('Author', backref=db.backref('books', lazy='dynamic'))

    def __init__(self, title, isbn, number_of_pages, description, author, published_date=None):
        self.title = title
        self.isbn = isbn
        self.number_of_pages = number_of_pages
        self.description = description
        self.author = author
        if published_date is None:
            self.published_date = datetime.utcnow()

    def __repr__(self):
        return f'{self.title} - {self.author.first_name} {self.author.last_name}'

    @staticmethod
    def additional_validation(param: str, value: str) -> str:
        return value
