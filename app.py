from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Nekretnina, initialize_db

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sonja123@localhost/db_nekretnine' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

initialize_db(app)
migrate = Migrate(app, db)

# /nekretnine/<int:id> - GET metoda za dohvatanje nekretnine po ID-u.
@app.route('/nekretnine/<int:id>', methods=['GET'])
def get_nekretnina(id):
    nekretnina = Nekretnina.query.get(id)
    if nekretnina:
        return jsonify(nekretnina.serialize())
    else:
        return jsonify({'message': 'Nekretnina nije pronađena'}), 404

# /nekretnine - GET metoda za pretraživanje nekretnina na osnovu zadatih parametara.
@app.route('/nekretnine', methods=['GET'])
def search_nekretnine():
    tip = request.args.get('tip')
    min_kvadratura = request.args.get('min_kvadratura')
    max_kvadratura = request.args.get('max_kvadratura')
    parking = request.args.get('parking')

    page = request.args.get('page', 1, type=int)  # Trenutna stranica (podrazumevana vrednost: 1)
    per_page = request.args.get('per_page', 10, type=int)  # Broj rezultata po stranici (podrazumevana vrednost: 10)

    query = Nekretnina.query

    if tip:
        query = query.filter_by(tipNekretnine=tip)

    if min_kvadratura:
        query = query.filter(Nekretnina.kvadratura >= float(min_kvadratura))

    if max_kvadratura:
        query = query.filter(Nekretnina.kvadratura <= float(max_kvadratura))

    if parking:
        query = query.filter_by(parking=parking)

    paginated_nekretnine = query.paginate(page=page, per_page=per_page)

    nekretnine = paginated_nekretnine.items
    total_pages = paginated_nekretnine.pages

    return jsonify({
        'nekretnine': [nekretnina.serialize() for nekretnina in nekretnine],
        'total_pages': total_pages,
        'current_page': page
    })

# /nekretnine - POST metoda za kreiranje nove nekretnine.
@app.route('/nekretnine', methods=['POST'])
def create_nekretnina():   
    data = request.get_json()
    id = data.get('id')
    tipNekretnine = data.get('tipNekretnine')
    tipPonude = data.get('tipPonude')
    grad = data.get('grad')
    opstina = data.get('opstina')
    kvadratura = data.get('kvadratura')
    godinaIzgradnje = data.get('godinaIzgradnje')
    povrsinaZemljista = data.get('povrsinaZemljista')
    spratnost = data.get('spratnost')
    uknjizenost = data.get('uknjizenost')
    tipGrejanja = data.get('tipGrejanja')
    ukupanBrojSoba = data.get('ukupanBrojSoba')
    ukupnoKupatila = data.get('ukupnoKupatila')
    parking = data.get('parking')
    dodatneKarakteristike = data.get('dodatneKarakteristike')

    nekretnina = Nekretnina(
    id=id,
    tipNekretnine=tipNekretnine,
    tipPonude=tipPonude,
    grad=grad,
    opstina=opstina,
    kvadratura=kvadratura,
    godinaIzgradnje=godinaIzgradnje,
    povrsinaZemljista=povrsinaZemljista,
    spratnost=spratnost,
    uknjizenost=uknjizenost,
    tipGrejanja=tipGrejanja,
    ukupanBrojSoba=ukupanBrojSoba,
    ukupnoKupatila=ukupnoKupatila,
    parking=parking,
    dodatneKarakteristike=dodatneKarakteristike
)

    db.session.add(nekretnina)
    db.session.commit()

    return jsonify({'message': 'Nekretnina je uspešno kreirana'}), 201

# /nekretnine/<int:id> - PUT metoda za ažuriranje podataka nekretnine po ID-u.
@app.route('/nekretnine/int:id', methods=['PUT'])
def update_nekretnina(id):
    nekretnina = Nekretnina.query.get(id)
    if not nekretnina:
        return jsonify({'message': 'Nekretnina nije pronadjena'}), 404
    data = request.get_json()        
    nekretnina.tipNekretnine = data.get('tipNekretnine', nekretnina.tipNekretnine)
    nekretnina.tipPonude = data.get('tipPonude', nekretnina.tipPonude)
    nekretnina.grad = data.get('grad', nekretnina.grad)
    nekretnina.opstina = data.get('opstina', nekretnina.opstina)
    nekretnina.kvadratura = data.get('kvadratura', nekretnina.kvadratura)
    nekretnina.godinaIzgradnje = data.get('godinaIzgradnje', nekretnina.godinaIzgradnje)
    nekretnina.povrsinaZemljista = data.get('povrsinaZemljista', nekretnina.povrsinaZemljista)
    nekretnina.spratnost = data.get('spratnost', nekretnina.spratnost)
    nekretnina.uknjizenost = data.get('uknjizenost', nekretnina.uknjizenost)
    nekretnina.tipGrejanja = data.get('tipGrejanja', nekretnina.tipGrejanja)
    nekretnina.ukupanBrojSoba = data.get('ukupanBrojSoba', nekretnina.ukupanBrojSoba)
    nekretnina.ukupnoKupatila = data.get('ukupnoKupatila', nekretnina.ukupnoKupatila)
    nekretnina.parking = data.get('parking', nekretnina.parking)
    nekretnina.dodatneKarakteristike = data.get('dodatneKarakteristike', nekretnina.dodatneKarakteristike)

    db.session.commit()

    return jsonify({'message': 'Nekretnina je uspešno ažurirana'})
    
# /nekretnine/<int:id> - DELETE metoda za brisanje nekretnine po ID-u.
#@app.route('/nekretnine/<int:id>', methods=['DELETE'])
#def delete_nekretnina(id):
#    nekretnina = Nekretnina.query.get(id)
#    if nekretnina:
#        db.session.delete(nekretnina)
#        db.session.commit()
#        return jsonify({'message': 'Nekretnina je uspešno obrisana'})
#    else:
#        return jsonify({'message': 'Nekretnina nije pronađena'}), 404
   
if __name__ == '__main__':
    app.run()
