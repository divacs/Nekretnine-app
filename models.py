from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Nekretnina(db.Model):
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
    
    # veza izmedju tabela
    stan = db.relationship('Stan', uselist=False, backref='nekretnina')
    kuca = db.relationship('Kuca', uselist=False, backref='nekretnina')


    # inicijalizujemo kolone
    def __init__(self, idNekretnine, tipNekretnine, tipPonude, grad, opstina, kvadratura, godinaIzgradnje, uknjizenost, tipGrejanja, ukupanBrojSoba, ukupnoKupatila, parking):
        self.idNekretnine = idNekretnine
        self.tipNekretnine = tipNekretnine
        self.tipPonude = tipPonude
        self.grad = grad
        self.opstina = opstina
        self.kvadratura = kvadratura
        self.godinaIzgradnje = godinaIzgradnje
        self.uknjizenost = uknjizenost
        self.tipGrejanja = tipGrejanja
        self.ukupanBrojSoba = ukupanBrojSoba
        self.ukupnoKupatila = ukupnoKupatila
        self.parking = parking
        

    def serialize(self):
        return {
        'idNekretnine': self.idNekretnine,
        'tipNekretnine': self.tipNekretnine,
        'tipPonude': self.tipPonude,
        'grad': self.grad,
        'opstina': self.opstina,
        'kvadratura': self.kvadratura,
        'godinaIzgradnje': self.godinaIzgradnje,
        'uknjizenost': self.uknjizenost,
        'tipGrejanja': self.tipGrejanja,
        'ukupanBrojSoba': self.ukupanBrojSoba,
        'ukupnoKupatila': self.ukupnoKupatila,
        'parking': self.parking
    }


class Stan(db.Model):
    idStana = db.Column(db.Integer, primary_key=True)
    idNekretnine = db.Column(db.Integer, db.ForeignKey('nekretnina.idNekretnine'))
    sprat = db.Column(db.Integer, nullable=False)
    dodatneKarakteristike = db.Column(db.String(255))
    
    nekretnina = db.relationship('Nekretnina', backref='stan', uselist=False)

    def __init__(self, idStana, idNekretnine, sprat, dodatneKarakteristike):
        self.idStana = idStana
        self.idNekretnine = idNekretnine
        self.sprat = sprat
        self.dodatneKarakteristike = dodatneKarakteristike

    def serialize(self):
        return {
            'idStana': self.idStana,
            'idNekretnine': self.idNekretnine,
            'sprat': self.sprat,
            'dodatneKarakteristike': self.dodatneKarakteristike
        }


class Kuca(db.Model):
    idKuce = db.Column(db.Integer, primary_key=True)
    idNekretnine = db.Column(db.Integer, db.ForeignKey('nekretnina.idNekretnine'))
    spratnost = db.Column(db.Integer, nullable=False)
    dodatneKarakteristike = db.Column(db.String(255))
    
    nekretnina = db.relationship('Nekretnina', backref='kuca', uselist=False)

    def __init__(self, idKuce, idNekretnine, spratnost, dodatneKarakteristike):
        self.idKuce = idKuce
        self.idNekretnine = idNekretnine
        self.spratnost = spratnost
        self.dodatneKarakteristike = dodatneKarakteristike

    def serialize(self):
        return {
            'idKuce': self.idKuce,
            'idNekretnine': self.idNekretnine,
            'spratnost': self.spratnost,
            'dodatneKarakteristike': self.dodatneKarakteristike
        }
