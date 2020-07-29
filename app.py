"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Element

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///elements'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def show_homepage():
    return render_template('index.html')