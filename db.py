from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.kuce import KuceModel
from models.nekretnine import NekretnineModel
from models.stanovi import StanoviModel

# Konfiguracija SQLAlchemy konekcije sa bazom podataka
engine = create_engine('mysql+mysqlconnector://username:password@localhost:3306/database') # prilagoditi connection string

# Kreiranje sesije
Session = sessionmaker(bind=engine)
session = Session()

# Kreiranje tabele u bazi podataka
def create_tables():
    KuceModel.__table__.create(bind=engine, checkfirst=True)
    NekretnineModel.__table__.create(bind=engine, checkfirst=True)
    StanoviModel.__table__.create(bind=engine, checkfirst=True)

if __name__ == '__main__':
    create_tables()