import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sonja123@localhost/db_nekretnine' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Nekretnina(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tipNekretnine = db.Column(db.String(100), nullable = False)
    tipPonude = db.Column(db.String(100), nullable = False)
    grad = db.Column(db.String(100), nullable = False)
    opstina = db.Column(db.String(100), nullable = False)
    kvadratura = db.Column(db.Double, nullable = False)
    godinaIzgradnje = db.Column(db.Date, nullable = False)
    povrsinaZemljista = db.Column(db.Double) # moze biti nullable jer stan nema ovaj podatak
    spratnost = db.Column(db.Integer, nullable = False)
    uknjizenost = db.Column(db.String(20), nullable = False)
    tipGrejanja = db.Column(db.String(50), nullable = False)
    ukupanBrojSoba = db.Column(db.Float, nullable = False)
    ukupnoKupatila = db.Column(db.Integer, nullable = False)
    parking = db.Column(db.String(20))
    dodatneKarakteristike = db.Column(db.String(255)) # moze biti nullable jer moze biti da u opisu nema dodatnih karakteristika


    # inicijalizujemo kolone
    def __init__(self, id, tipNekretnine, tipPonude, grad, opstina, 
                 kvadratura, godinaIzgradnje, povrsinaZemljista, spratnost, 
                 uknjizenost, tipGrejanja, ukupanBrojSoba, ukupnoKupatila, parking,
                 dodatneKarakteristike):
        self.id = id
        self.tipNekretnine = self._validate_tip_nekretnine(tipNekretnine)
        self.tipPonude = self._validate_tip_ponude(tipPonude)
        self.grad = grad
        self.opstina = opstina
        self.kvadratura = kvadratura
        self.godinaIzgradnje = godinaIzgradnje
        self.povrsinaZemljista = self._validate_povrsina_zemljista(povrsinaZemljista, tipNekretnine)
        self.spratnost = spratnost
        self.uknjizenost = self._validate_uknjizenost(uknjizenost)
        self.tipGrejanja = tipGrejanja
        self.ukupanBrojSoba = ukupanBrojSoba
        self.ukupnoKupatila = ukupnoKupatila
        self.parking = self._validate_parking(parking)
        self.dodatneKarakteristike = dodatneKarakteristike
        
    # serialize() u klasi se koristi za pretvaranje objekta nekretnine u JSON format
    def serialize(self):
        return {
        'id': self.id,
        'tipNekretnine': self.tipNekretnine,
        'tipPonude': self.tipPonude,
        'grad': self.grad,
        'opstina': self.opstina,
        'kvadratura': self.kvadratura,
        'godinaIzgradnje': self.godinaIzgradnje,
        'povrsinaZemljista': self.povrsinaZemljista,
        'spratnost': self.spratnost,
        'uknjizenost': self.uknjizenost,
        'tipGrejanja': self.tipGrejanja,
        'ukupanBrojSoba': self.ukupanBrojSoba,
        'ukupnoKupatila': self.ukupnoKupatila,
        'parking': self.parking,
        'dodatneKarakteristike': self.dodatneKarakteristike
    }
# Proverava da li je tipNekretnine ispravna vrednost
# dozvoljene vrednosti su "stan" i "kuća"
def _validate_tip_nekretnine(self, tipNekretnine):
        valid_values = ["stan", "kuća"]
        if tipNekretnine in valid_values:
            return tipNekretnine
        else:
            raise ValueError(f"Neispravna tipNekretnine vrednost. Ispravne vrednosti su {', '.join(valid_values)}")

# Proverava da li je tipPonude ispravna vrednost
# dozvoljene vrednosti su "prodaja" i "iznajmljivanje"
def _validate_tip_ponude(self, tipPonude):
        valid_values = ["prodaja", "iznajmljivanje"]
        if tipPonude in valid_values:
            return tipPonude
        else:
            raise ValueError(f"Neispravna tipPonude vrednost. Ispravne vrednosti su {', '.join(valid_values)}")

# Proverava da li je povrsinaZemljista ispravna vrednost za kuću
# ako je tipNekretnine "kuća", povrsinaZemljista je obavezna
# ako je tipNekretnine "stan", povrsinaZemljista je None
def _validate_povrsina_zemljista(self, povrsinaZemljista, tipNekretnine):
        if tipNekretnine == "kuća":
            if povrsinaZemljista is None:
                raise ValueError("povrsinaZemljista je obavezna za kuću.")
            else:
                return povrsinaZemljista
        else:
            return None
        
# Proverava da li je uknjizenost ispravna vrednost
# dozvoljene vrednosti su "da" i "ne"
def _validate_uknjizenost(self, uknjizenost):
        valid_values = ["da", "ne"]
        if uknjizenost in valid_values:
            return uknjizenost
        else:
            raise ValueError(f"Neispravna uknjizenost vrednost. Ispravne vrednosti su {', '.join(valid_values)}")

# Proverava da li je parking ispravna vrednost
# dozvoljene vrednosti su "da" i "ne"
def _validate_parking(self, parking):
        valid_values = ["da", "ne"]
        if parking in valid_values:
            return parking
        else:
            raise ValueError(f"Neispravna parking vrednost. Ispravne vrednosti su {', '.join(valid_values)}")
        
migrate = Migrate(app, db)