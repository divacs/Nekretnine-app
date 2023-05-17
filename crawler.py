import requests
from bs4 import BeautifulSoup
import pymysql

# Povezivanje s bazom podataka
db = pymysql.connect(host='localhost', user='root', password='sonja123', database='db_nekretnine')
cursor = db.cursor()

# Funkcija za prikupljanje informacija o nekretninama sa zadate stranice
def crawl_page(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    
    # Pretraga linkova ka oglasima nekretnina
    links = soup.find_all('a', class_='btn-list-item')
    
    for link in links:
        href = link.get('href')
        if href:
            # Prikupljanje informacija o nekretnini
            id = link.get('data-id')
            tipNekretnine = link.find('div', class_='text-truncate d-inline-block w-100').text.strip()
            tipPonude = link.find('label', class_='form-check-label').text.strip()
            grad = link.find('span', class_='grad').text.strip()
            opstina = link.find('span', class_='opstina').text.strip()
            kvadratura = link.find('span', class_='kvadratura').text.strip()
            godinaIzgradnje = link.find('span', class_='godina_izgradnje').text.strip()
            povrsinaZemljista = link.find('span', class_='povrsina_zemljista')
            if povrsinaZemljista:
                povrsinaZemljista = povrsinaZemljista.text.strip()
            spratnost = link.find('span', class_='spratnost').text.strip()
            uknjizenost = link.find('span', class_='uknjizenost').text.strip()
            tipGrejanja = link.find('span', class_='tip_grejanja').text.strip()
            ukupanBrojSoba = link.find('span', class_='ukupan_broj_soba').text.strip()
            ukupnoKupatila = link.find('span', class_='ukupno_kupatila').text.strip()
            parking = link.find('span', class_='parking')
            if parking:
                parking = parking.text.strip()
            dodatneKarakteristike = link.find('span', class_='dodatne_karakteristike')
            if dodatneKarakteristike:
                dodatneKarakteristike = dodatneKarakteristike.text.strip()

            # Unos podataka u bazu
            sql = "INSERT INTO Nekretnina (id, tipNekretnine, tipPonude, grad, opstina, kvadratura, godinaIzgradnje, povrsinaZemljista, spratnost, uknjizenost, tipGrejanja, ukupanBrojSoba, ukupnoKupatila, parking, dodatneKarakteristike) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            try:
                cursor.execute(sql, (id, tipNekretnine, tipPonude, grad, opstina, kvadratura, 
                                     godinaIzgradnje, povrsinaZemljista,
                                                                          spratnost, uknjizenost, 
                                     tipGrejanja, ukupanBrojSoba, ukupnoKupatila, 
                                     parking, dodatneKarakteristike))

                db.commit()
            except Exception as e:
                print(f"Greska prilikom ubacivanja podataka u bazu: {str(e)}")
                db.rollback()

# Glavna funkcija za pretragu
def search_nekretnine():
    base_url = 'https://www.nekretnine.rs/'
    num_pages = 10  # Broj stranica koje želimo da pretražimo

    for page in range(1, num_pages + 1):
        url = f'{base_url}?page={page}'
        crawl_page(url)

    print("Pretraga je završena.")

# Pokretanje pretrage
search_nekretnine()

# Zatvaranje veze s bazom podataka
db.close()

