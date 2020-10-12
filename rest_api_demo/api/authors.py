import logging

from flask import request
from flask_restx import Resource

from rest_api_demo.api import api, pagination_arguments
from rest_api_demo.api.serializers import author, page_of_authors
from rest_api_demo.library.services import create_author, delete_author, update_author
from rest_api_demo.library.models import Author

log = logging.getLogger(__name__)

ns = api.namespace('authors', description='Operations related to authors')


@ns.route('/')
class AuthorsCollection(Resource):
    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_authors)
    def get(self):
        """
        Returns list of authors in the library.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        authors_query = Author.query
        posts_page = authors_query.paginate(page, per_page, error_out=False)
        return posts_page

    @api.response(201, 'Author successfully created.')
    @api.expect(author)
    def post(self):
        """
        Creates a new author.
        """
        data = request.json
        create_author(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Author not found.')
class AuthorItem(Resource):

    @api.marshal_with(author)
    def get(self, id):
        """
        Returns an author with a given ID.
        """
        return Author.query.filter(Author.id == id).one()

    @api.expect(author)
    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        """
        Updates an author.

        Use this method to change the name of an author.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "first_name": "New First Name",
          "last_name": "New Last Name"
        }
        ```

        * Specify the ID of the author to modify in the request URL path.
        """
        data = request.json
        update_author(id, data)
        return None, 204

    @api.response(204, 'Author successfully deleted.')
    def delete(self, id):
        """
        Deletes an author.
        """
        delete_author(id)
        return None, 204
