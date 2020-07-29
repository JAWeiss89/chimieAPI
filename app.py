"""Flask app for Elements"""

from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Element
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', "postgresql:///elements")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey512')

connect_db(app)

def serialize(element):
    """ Serializes SQLAlchemy object so that it can be JSONified """
    return {
        "atomic_number" : element.id,
        "name": element.name,
        "symbol": element.symbol,
        "mass": element.mass
    }

def serialize_detail(element):
    """ Serializes SQLAlchemy object with all available data to be JSONIFIED """
    return {
        "atomic_number" : element.id,
        "name": element.name,
        "symbol": element.symbol,
        "mass": element.mass,
        "group": element.group,
        "year_discovered": element.year,
        "melting_point": element.melting,
        "boiling_point": element.boiling
    }

@app.route('/')
def show_homepage():
    return render_template('index.html')

@app.route('/api/elements')
def list_all_elements():
    elements = Element.query.all()
    all_elements = []
    for element in elements:
        all_elements.append(serialize(element))
    return jsonify(elements= all_elements)

@app.route('/api/elements/<int:id>')
def get_one_element(id):
    element = Element.query.get_or_404(id)
    return jsonify(element= serialize_detail(element))

@app.route('/api/elements', methods=['POST'])
def create_element():
    id = request.json["id"]
    name = request.json["name"]
    symbol = request.json["symbol"]
    mass = request.json["mass"]
    new_element = Element(id=id, name=name, symbol=symbol, mass=mass)

    db.session.add(new_element)
    db.session.commit()

    response_json = jsonify(message="Element Created!", element=serialize_detail(new_element))
    return (response_json, 201)

@app.route('/api/elements/<int:id>', methods=['PATCH'])
def update_element(id):
    element = Element.query.get_or_404(id)

    element.id = request.json.get('id', element.id)
    element.name = request.json.get('name', element.name)
    element.symbol = request.json.get('symbol', element.symbol)
    element.mass = request.json.get('mass', element.mass)

    db.session.add(element)
    db.session.commit()

    return jsonify(message="Updated Element", element=serialize_detail(element))

@app.route('/api/elements/<int:id>', methods=['DELETE'])
def delete_element(id):
    element = Element.query.get_or_404(id)

    db.session.delete(element)
    db.session.commit()
    return jsonify(message=f"Deleted Element of ID: {id}")


