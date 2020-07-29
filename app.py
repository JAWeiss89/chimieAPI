"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Element

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URL'
app.config['DATABASE_URL'] = 'postgres://gdxpkgfpsfxfbd:20542176e7530dd981d6d7be61bb84f5ab97080a36b87f9cd8587ce0cbe5b335@ec2-3-215-83-17.compute-1.amazonaws.com:5432/d896frbt90l7ru'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def show_homepage():
    return render_template('index.html')