import requests
from bs4 import BeautifulSoup
import pymysql
import uuid

# Funkcija za prikupljanje informacija o nekretninama sa zadate stranice
db = pymysql.connect(host='localhost', user='root', password='sonja123', database='db_nekretnine')
cursor = db.cursor()

# Funkcija za prikupljanje informacija o nekretninama sa zadate stranice
def crawl_page(url):
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    
    # Provera države
    drzava_element = soup.find('div', class_='text-truncate d-inline-block w-100')
    drzava = drzava_element.text.strip() if drzava_element else ''
    
    if drzava.lower() != 'srbija':
        return  # Prekid izvršavanja ako nije u Srbiji
    
    # Pretraga linkova ka oglasima nekretnina
    links = soup.find_all('a', class_='btn-list-item')
    
    for link in links:
        href = link.get('href')
        if href:            
            # Generisanje jedinstvenog ID-a
            id = str(uuid.uuid4())
            
            # Prikupljanje informacija o nekretnini
            tipNekretnine = link.find('div', class_='text-truncate d-inline-block w-100').text.strip()
            tipPonude = link.find('label', class_='form-check-label').text.strip()
            grad = link.find('input', class_='form-control').get('value', '').strip()
            opstina = link.find('div', class_='form-control filter-multi-citypart-dropdown').text.strip()
            # Pronalaženje elementa <li> za kvadraturu
            li_kvadratura = link.find('li', text='Kvadratura:')
            kvadratura = li_kvadratura.find_next('strong').text.strip()

            # Prikupljanje dodatnih informacija o nekretnini
            li_godina_izgradnje = link.find('li', text='Godina izgradnje:')
            godinaIzgradnje = li_godina_izgradnje.find_next('strong').text.strip() if li_godina_izgradnje else ''
            
            li_povrsina_zemljista = link.find('li', text='Površina zemljišta:')
            povrsinaZemljista = li_povrsina_zemljista.find_next('strong').text.strip() if li_povrsina_zemljista else ''
            
            li_spratnost = link.find('li', text='Spratnost:')
            spratnost = li_spratnost.find_next('strong').text.strip() if li_spratnost else ''
            
            li_uknjizenost = link.find('li', text='Uknjiženo:')
            uknjizenost = li_uknjizenost.find_next('strong').text.strip() if li_uknjizenost else ''
            
            li_tip_grejanja = link.find('li', text='Tip grejanja:')
            tipGrejanja = li_tip_grejanja.find_next('strong').text.strip() if li_tip_grejanja else ''
            
            li_ukupan_broj_soba = link.find('li', text='Ukupan broj soba:')
            ukupanBrojSoba = li_ukupan_broj_soba.find_next('strong').text.strip() if li_ukupan_broj_soba else ''
            
            li_ukupno_kupatila = link.find('li', text='Broj kupatila:')
            ukupnoKupatila = li_ukupno_kupatila.find_next('strong').text.strip() if li_ukupno_kupatila else ''

            li_parking = link.find('li', text='Parking:')
            parking = li_parking.find_next('strong').text.strip() if li_parking else ''

            h3_dodatna_opremljenost = soup.find('h3', text='Dodatna opremljenost')
            ul_dodatna_opremljenost = h3_dodatna_opremljenost.find_next('ul') if h3_dodatna_opremljenost else None
            karakteristike = [li.text.strip() for li in ul_dodatna_opremljenost.find_all('li')] if ul_dodatna_opremljenost else []
            dodatneKarakteristike = ', '.join(karakteristike)

            # Unos podataka u bazu
            sql = "INSERT INTO Nekretnina (id, tipNekretnine, tipPonude, grad, opstina, kvadratura, godinaIzgradnje, povrsinaZemljista, spratnost, uknjizenost, tipGrejanja, ukupanBrojSoba, ukupnoKupatila, parking, dodatneKarakteristike) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            try:
                cursor.execute(sql, (id, tipNekretnine, tipPonude, grad, opstina, kvadratura, godinaIzgradnje, povrsinaZemljista, spratnost, uknjizenost, tipGrejanja, ukupanBrojSoba, ukupnoKupatila, parking, dodatneKarakteristike))
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

