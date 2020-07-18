from src.database.db import db

class AuthorModel(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return f"<Author {self.name}>"
    
    @property
    def serialize(self):
       return {
           'id': self.id,
           'name': self.name,
       }    