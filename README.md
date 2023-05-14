# Nekretnine-app

## Zadatak

- Potrebno je realizovati web indekser (web crawler) koji prikuplja informacije o nekretninama koje se izdaju ili prodaju u Srbiji. Bazu realizovati u tehnologiji MySQL ili PostgreSQL.

- Cilj web indeksera je da se poveže na određenu web stranu i da preuzme njen sadržaj. Parsiranjem date strane možemo naći linkove, koji vode na neke druge strane, na koje web-indekser ponovo može da uđe i da ponovi celu proceduru. Pored otkrivanja linkova, parser može da prepozna i druge sadržaje koje web strana ima. (div, span, li, …)

- Potrebno je prikupiti informacije o svim nekretninama sa web stranice https://www.nekretnine.rs/ i sačuvati ih u bazi – tip nekretnine (stan ili kuća), tip ponude (prodaja ili iznajmljivanje), lokacija - grad i deo grada gde se lokacija nalazi, kvadratura nekretnine, godina izgradnje, površina zemljišta (samo za kuće), spratnost (ukupna i sprat na kojoj se nalazi, samo za stanove), uknjiženost (da/ne), tip grejanja, ukupan broj soba, ukupan broj kupatila (toaleta), podaci o parkingu (da/ne) i ostale dodatne informacije (da li ima lift u zgradi, da li ima terasu/lođu/balkon). Podaci koji nisu dostupni u oglasu, u bazi treba da ostanu praznog polja.

- Realizovati mini-aplikaciju u Flask framework-u u Python-u. Aplikacija treba da obezbedi:
  - API za dohvatanje nekretnine po id-ju nekretnine iz baze.
  - API za pretraživanje nekretnina na osnovu zadatih parametara:
    - tip – kuca/stan
    - minimalna kvadratura nekretnine – sve nekretnine koje imaju veću kvadraturu od zadate
    - maksimalna kvadratura nekretnine – sve nekretnine koje imaju manju kvadraturu od zadate
    - parking – Da/Ne
  - API za kreiranje nove nekretnine za prodaju/izdavanje
  - API za promenu podataka (izabrati podatke po želji) nekretnine

- Voditi računa da se pretraživanje nekretnina može vršiti na osnovu nekoliko parametara (ne samo jednog) ili nijednog parametra.

- Realizovati paginaciju za API pretraživanje nekretnina
- Za komunikaciju sa bazom koristiti ORM SQLAlchemy ili Flask-SQLAlchemy
