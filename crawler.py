import dbm
from bs4 import BeautifulSoup
import requests
from models.kuce import KuceModel
from models.stanovi import StanoviModel
from models.nekretnine import NekretnineModel

# Implementiranje koda za smeštanje prikupljenih podataka u bazu podataka
def crawl_nekretnine():
    url = "https://www.nekretnine.rs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Ovde treba da dodam kod za parsiranje HTML-a i dohvatanje informacija o nekretninama
    # na sajtu https://www.nekretnine.rs/
    # Treba da kreiram instance modela NekretnineModel, StanoviModel i KuceModel sa prikupljenim podacima

    linkovi = []
    for linkovi in soup.find_all('a'):
        href = linkovi.get('href')
        if href:
            linkovi.append(href)
    
    drugi_sadrzaj = []
    for tag in ['div', 'span', 'li']:
        contents = soup.find_all(tag)
        drugi_sadrzaj.extend(contents)

    return linkovi, drugi_sadrzaj

def insert_data_into_database(session, data):
    # Ubacivanje podataka u tabelu Nekretnina
    for item in data:
        tipNekretnine = item.get('tipNekretnine')
        tipPonude = item.get('tipPonude')
        grad = item.get('grad')
        opstina = item.get('opstina')
        kvadratura = item.get('kvadratura')
        godinaIzgradnje = item.get('godinaIzgradnje')
        uknjizenost = item.get('uknjizenost')
        tipGrejanja = item.get('tipGrejanja')
        ukupanBrojSoba = item.get('ukupanBrojSoba')
        ukupnoKupatila = item.get('ukupnoKupatila')
        parking = item.get('parking')

        # Kreiranje instance modela NekretnineModel sa prikupljenim podacima
        nekretnina = NekretnineModel(
            tipNekretnine=tipNekretnine,
            tipPonude=tipPonude,
            grad=grad,
            opstina=opstina,
            kvadratura=kvadratura,
            godinaIzgradnje=godinaIzgradnje,
            uknjizenost=uknjizenost,
            tipGrejanja=tipGrejanja,
            ukupanBrojSoba=ukupanBrojSoba,
            ukupnoKupatila=ukupnoKupatila,
            parking=parking
        )

        # Ubacivanje instance modela NekretnineModel u bazu
        session.add(nekretnina)
        session.flush()

        idNekretnine = nekretnina.idNekretnine

        # Provjera tipa nekretnine i ubacivanje podataka u odgovarajuću tabelu
        if tipNekretnine == 'Stan':
            sprat = item.get('sprat')
            dodatneKarakteristike = item.get('dodatneKarakteristike')

            # Kreiranje instance modela StanoviModel sa prikupljenim podacima
            stan = StanoviModel(
                idNekretnine=idNekretnine,
                sprat=sprat,
                dodatneKarakteristike=dodatneKarakteristike
            )

            # Ubacivanje instance modela StanoviModel u bazu
            session.add(stan)
        elif tipNekretnine == 'Kuca':
            spratnost = item.get('spratnost')
            dodatneKarakteristike = item.get('dodatneKarakteristike')

            # Kreiranje instance modela KuceModel sa prikupljenim podacima
            kuca = KuceModel(
                idNekretnine=idNekretnine,
                spratnost=spratnost,
                dodatneKarakteristike=dodatneKarakteristike
            )

            # Ubacivanje instance modela KuceModel u bazu
            session.add(kuca)

    # Potvrda promena u bazi
    session.commit()

def main():
    # Kreiranje sesije
    session = dbm.session() # db umesto dbm

    # Preuzimanje podataka sa web stranice
    linkovi, drugi_sadrzaj = crawl_nekretnine()

    # Pretvaranje podataka u format koji može biti ubačen u bazu
    data = []
    for link in linkovi:
        data.append({'tipNekretnine': 'Link', 'link': link})

    for content in drugi_sadrzaj:
        data.append({'tipNekretnine': content.name, 'sadrzaj': content.get_text()})

    # Ubacivanje podataka u bazu
    insert_data_into_database(session, data)

    # Zatvaranje sesije
    session.close()

if __name__ == "__main__":
    main()