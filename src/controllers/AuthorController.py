import json

from flask import request, Response, jsonify
from flask.views import MethodView

from src.models.Author import AuthorModel
from src.database.db import db

class Author(MethodView):

  def get(self, author_id):
    if author_id is None:
      return jsonify([i.serialize for i in AuthorModel.query.all()])
    else:
      author = AuthorModel.query.get(author_id)

      if not author:
        return Response(json.dumps(
          {'error': 'Author not find'}
        ), mimetype='application/json', status=400)
      
      return jsonify(author.serialize)
