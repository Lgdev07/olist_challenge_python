from src.controllers.AuthorController import AuthorController
from src.controllers.AuthorCsvController import AuthorCsvController
from src import app

def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, view_func=view_func, defaults={pk: None},
    methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                    methods=['GET', 'PUT', 'DELETE'])  

def initalize_routes():
    register_api(AuthorController, 'author', '/authors/', pk='author_id') 
    register_api(AuthorCsvController, 'author_csv', '/authors/csv/') 
