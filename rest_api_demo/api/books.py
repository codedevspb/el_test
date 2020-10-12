import logging

from flask import request
from flask_restx import Resource

from rest_api_demo.api import api
from rest_api_demo.api import pagination_arguments
from rest_api_demo.api.serializers import book, page_of_books
from rest_api_demo.library.services import create_book, delete_book, update_book
from rest_api_demo.library.models import Book

log = logging.getLogger(__name__)

ns = api.namespace('books', description='Operations related to books')


@ns.route('/')
class BooksCollection(Resource):
    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_books)
    def get(self):
        """
        Returns list of books in the library.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        books_query = Book.query
        posts_page = books_query.paginate(page, per_page, error_out=False)
        return posts_page

    @api.response(201, 'Book successfully created.')
    @api.expect(book)
    def post(self):
        """
        Creates a new book.
        """
        data = request.json
        create_book(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Book not found.')
class BookItem(Resource):

    @api.marshal_with(book)
    def get(self, id):
        """
        Returns an author with a given ID.
        """
        return Book.query.filter(Book.id == id).one()

    @api.expect(book)
    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        """
        Updates an author.

        Use this method to change the name of an author.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "title": "Book title",
          "isbn": "ISBN of the book",
          "number_of_pages": "Number of pages",
          "published_date": "Publication date",
          "description": "Book description"
        }
        ```

        * Specify the ID of the book to modify in the request URL path.
        """
        data = request.json
        update_book(id, data)
        return None, 204

    @api.response(204, 'Book successfully deleted.')
    def delete(self, id):
        """
        Deletes an author.
        """
        delete_book(id)
        return None, 204
