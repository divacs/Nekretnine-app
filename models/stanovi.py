from db import db
from sqlalchemy import ForeignKey

class StanoviModel(db.Model):
    __tablename__ = "stan"
    
    idStana = db.Column(db.Integer, primary_key = True)
    idNekretnine = db.Column(db.Integer, ForeignKey('nekretnina.idNekretnine'))
    sprat = db.Column(db.Integer, nullable = False)
    dodatneKarakteristike = db.Column(db.String(255))