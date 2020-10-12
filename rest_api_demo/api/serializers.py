from flask_restx import fields
from rest_api_demo.api import api

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

author = api.model('Author', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an author'),
    'first_name': fields.String(required=True, description='First name of the author'),
    'last_name': fields.String(required=True, description='Last name of the author')
})

page_of_authors = api.inherit('Page of authors list', pagination, {
    'items': fields.List(fields.Nested(author))
})

book = api.model('Book', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the book'),
    'title': fields.String(required=True, description='Book title'),
    'isbn': fields.String(required=True, description='Book\'s ISBN'),
    'number_of_pages': fields.Integer(required=False),
    'published_date': fields.DateTime,
    'description': fields.String(required=True, description='Book\'s description'),
    'author_id': fields.Integer(attribute='author.id'),
    'author': fields.String(attribute='author')
})

page_of_books = api.inherit('Page of books list', pagination, {
    'items': fields.List(fields.Nested(book))
})
