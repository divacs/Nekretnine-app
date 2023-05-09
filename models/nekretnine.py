from db import db

class NekretnineModel(db.Model):
    __tablename__ = "nekretnina"
    
    idNekretnine = db.Column(db.Integer, primary_key = True)
    tipNekretnine = db.Column(db.String(100), nullable = False)
    tipPonude = db.Column(db.String(100), nullable = False)
    grad = db.Column(db.String(100), nullable = False)
    opstina = db.Column(db.String(100), nullable = False)
    kvadratura = db.Column(db.Double, nullable = False)
    godinaIzgradnje = db.Column(db.Date, nullable = False)
    uknjizenost = db.Column(db.String(20), nullable = False)
    tipGrejanja = db.Column(db.String(50), nullable = False)
    ukupanBrojSoba = db.Column(db.Float, nullable = False)
    ukupnoKupatila = db.Column(db.Integer)
    parking = db.Column(db.String(20))