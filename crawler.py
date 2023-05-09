from bs4 import BeautifulSoup
import requests
from db import db
from models import NekretnineModel, StanoviModel, KuceModel


# Implementiranje koda za smeštanje prikupljenih podataka u bazu podataka
def crawl_nekretnine():
    url = "https://www.nekretnine.rs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Ovde treba da dodam kod za parsiranje HTML-a i dohvatanje informacija o nekretninama
    # na sajtu https://www.nekretnine.rs/
    # Treba da kreiram instance modela NekretnineModel, StanoviModel i KuceModel sa prikupljenim podacima

    # Kreiranje instance modela sa prikupljenim podacima
    nekretnina = NekretnineModel(...)
    stan = StanoviModel(...)
    kuca = KuceModel(...)
    
    # Cuvanje instance u bazi
    db.session.add(nekretnina)
    db.session.add(stan)
    db.session.add(kuca)
    db.session.commit()

# Pozovanje funkcije crawl_nekretnine() da bismo pokrenuli proces preuzimanja podataka i smeštanja u bazu
# main?
if __name__ == "__main__":
    crawl_nekretnine()
