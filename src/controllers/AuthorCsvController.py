import json

from flask import request, Response, jsonify
from flask.views import MethodView

from src.models.Author import AuthorModel
from src.database.db import db

class AuthorCsvController(MethodView):

  def post(self):
    if not 'file' in request.files:
      return Response(json.dumps(
        {'error': 'No file part'}
      ), mimetype='application/json', status=400)
    
    file = request.files.get('file')

    if file.filename == '':
      return Response(json.dumps(
        {'error': 'No selected file'}
      ), mimetype='application/json', status=400)

    string_file = file.read().decode("utf-8")
    splited_lines = string_file.split(',\n')
    authors = splited_lines[1:]

    for author in authors:
      if not author:
        continue
      db.session.add(AuthorModel(name=author))
    
    db.session.commit()

    return jsonify([i.serialize for i in AuthorModel.query.all()])

  