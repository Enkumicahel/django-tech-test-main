import json

from marshmallow import ValidationError
from django.views.generic import View

from techtest.authors.models import Author
from techtest.authors.schemas import AuthorSchema
from techtest.utils import json_response


class AuthorsListView(View):
    def get(self, request, *args, **kwargs):
        return json_response(AuthorSchema().dump(Author.objects.all(), many=True))

    def post(self, request, *args, **kwargs):
        try:
            author = AuthorSchema().load(json.loads(request.body))
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(AuthorSchema().dump(author), 201)

class AuthorView(View):
    def dispatch(self, request, article_id, *args, **kwargs):
        try:
            self.article = Author.objects.get(pk=article_id)
        except Author.DoesNotExist:
            return json_response({"error": "No Author matches the given query"}, 404)
        self.data = request.body and dict(json.loads(request.body), id=self.article.id)
        return super(AuthorView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return json_response(AuthorSchema().dump(self.article))

    def put(self, request, *args, **kwargs):
        try:
            self.article = AuthorSchema().load(self.data)
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(AuthorSchema().dump(self.article))

    def delete(self, request, *args, **kwargs):
        self.article.delete()
        return json_response()
