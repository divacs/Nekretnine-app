from db import db
from sqlalchemy import ForeignKey

class KuceModel(db.Model):
    __tablename__ = "kuca"
    
    idKuce = db.Column(db.Integer, primary_key = True)
    idNekretnine = db.Column(db.Integer, ForeignKey('nekretnina.idNekretnine'))
    spratnost = db.Column(db.Integer, nullable = False)
    dodatneKarakteristike = db.Column(db.String(255))