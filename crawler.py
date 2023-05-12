from models import Nekretnina, Stan, Kuca
import requests
from bs4 import BeautifulSoup
from models import db

# fja za preuzimanje sadrzaja stranie
# koristite biblioteku requests za slanje HTTP zahteva i dobijanje HTML sadržaja.
def crawl_page(url):
    response = requests.get(url)
    return response.content

# parsiranje HTML sadržaja stranice i izvlacenje informacije o nekretninama
def parse_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # ovde dodajemo kod za izvlačenje informacija o nekretninama iz HTML-a stranice
    # koristimo metode poput soup.find(), soup.find_all() i slično
    # primer:
    property_divs = soup.find_all('div', class_='property')

    for property_div in property_divs:
        # ovde izvlacimo informacije o svakoj nekretnini i cuvamo ih u bazi
        # primer:
        title = property_div.find('h2').text
        price = property_div.find('span', class_='price').text

        # cuvamo informacije u bazi podataka
        

 
# poretanje indeksiranja       
def run_crawler():
    url = 'https://www.nekretnine.rs/'
    html_content = crawl_page(url)
    parse_page(html_content)


# dodajemo poziv fje kako bismo pokrenuli indekser prilikom izvrsavanja
if __name__ == '__main__':
    run_crawler()
