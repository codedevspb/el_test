import logging

from flask import request
from flask_restx import Resource

from rest_api_demo.api import api
from rest_api_demo.api import pagination_arguments
from rest_api_demo.api.serializers import page_of_books
from rest_api_demo.library.models import Book, Author

log = logging.getLogger(__name__)

ns = api.namespace('library', description='Operations related to books')


@ns.route('/books/title/<string:title>')
class BooksTitleSearchCollection(Resource):
    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_books)
    def get(self, title):
        """
        Returns list of books in the library by title
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        books_query = Book.query.filter(Book.title.ilike(f'%{title}%'))
        posts_page = books_query.paginate(page, per_page, error_out=False)
        return posts_page


@ns.route('/books/author/name/<string:name>')
class BooksAuthorSearchCollection(Resource):
    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_books)
    def get(self, name):
        """
        Returns list of books in the library by author last name
        """

        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        books_query = Book.query.filter(Book.author_id == Author.id).filter(
            (Author.first_name + ' ' + Author.last_name).ilike(f'%{name}%'))
        posts_page = books_query.paginate(page, per_page, error_out=False)
        return posts_page

