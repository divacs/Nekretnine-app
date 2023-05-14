from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Nekretnina, Stan, Kuca

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nekretnine.db'  # treba da promenim na odgovarajući URL za MySQL ili PostgreSQL
db = SQLAlchemy(app)


# /nekretnine/<int:id> - GET metoda za dohvatanje nekretnine po ID-u.
@app.route('/nekretnine/<int:id>', methods=['GET'])
def get_nekretnina(id):
    nekretnina = Nekretnina.query.get(id)
    if nekretnina:
        return jsonify(nekretnina.serialize())
    else:
        return jsonify({'message': 'Nekretnina not found'}), 404

# /nekretnine - GET metoda za pretraživanje nekretnina na osnovu zadatih parametara.
@app.route('/nekretnine', methods=['GET'])
def search_nekretnine():
    tip = request.args.get('tip')
    min_kvadratura = request.args.get('min_kvadratura')
    max_kvadratura = request.args.get('max_kvadratura')
    parking = request.args.get('parking')

    query = Nekretnina.query

    if tip:
        query = query.filter_by(tipNekretnine=tip)

    if min_kvadratura:
        query = query.filter(Nekretnina.kvadratura >= float(min_kvadratura))

    if max_kvadratura:
        query = query.filter(Nekretnina.kvadratura <= float(max_kvadratura))

    if parking:
        query = query.filter_by(parking=parking)

    nekretnine = query.all()
    return jsonify([nekretnina.serialize() for nekretnina in nekretnine])

# /nekretnine - POST metoda za kreiranje nove nekretnine.
@app.route('/nekretnine', methods=['POST'])
def create_nekretnina():
    data = request.get_json()
    idNekretnine = data.get('idNekretnine')
    tipNekretnine = data.get('tipNekretnine')
    tipPonude = data.get('tipPonude')
    grad = data.get('grad')
    opstina = data.get('opstina')
    kvadratura = data.get('kvadratura')
    godinaIzgradnje = data.get('godinaIzgradnje')
    uknjizenost = data.get('uknjizenost')
    tipGrejanja = data.get('tipGrejanja')
    ukupanBrojSoba = data.get('ukupanBrojSoba')
    ukupnoKupatila = data.get('ukupnoKupatila')
    parking = data.get('parking')

    nekretnina = Nekretnina(
    idNekretnine=idNekretnine,
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

    db.session.add(nekretnina)
    db.session.commit()

    return jsonify({'message': 'Nekretnina created successfully'}), 201
# /nekretnine/<int:id> - PUT metoda za ažuriranje podataka nekretnine po ID-u.
@app.route('/nekretnine/int:id', methods=['PUT'])
def update_nekretnina(id):
    nekretnina = Nekretnina.query.get(id)
    if not nekretnina:
        return jsonify({'message': 'Nekretnina not found'}), 404
    data = request.get_json()

    nekretnina.tipNekretnine = data.get('tipNekretnine', nekretnina.tipNekretnine)
    nekretnina.tipPonude = data.get('tipPonude', nekretnina.tipPonude)
    nekretnina.grad = data.get('grad', nekretnina.grad)
    nekretnina.opstina = data.get('opstina', nekretnina.opstina)
    nekretnina.kvadratura = data.get('kvadratura', nekretnina.kvadratura)
    nekretnina.godinaIzgradnje = data.get('godinaIzgradnje', nekretnina.godinaIzgradnje)
    nekretnina.uknjizenost = data.get('uknjizenost', nekretnina.uknjizenost)
    nekretnina.tipGrejanja = data.get('tipGrejanja', nekretnina.tipGrejanja)
    nekretnina.ukupanBrojSoba = data.get('ukupanBrojSoba', nekretnina.ukupanBrojSoba)
    nekretnina.ukupnoKupatila = data.get('ukupnoKupatila', nekretnina.ukupnoKupatila)
    nekretnina.parking = data.get('parking', nekretnina.parking)

    db.session.commit()

    return jsonify({'message': 'Nekretnina updated successfully'})
    
if __name__ == '__main__':
    app.run()