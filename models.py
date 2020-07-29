"""Models for Element app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Element(db.Model):
    """ Element model """

    __tablename__ = "elements"


    id = db.Column(
        db.Integer,
        primary_key=True
        )
    name = db.Column(
        db.String(20),
        nullable=False
        )
    symbol = db.Column(
        db.String(2),
        unique=True,
        nullable=False
        )
    mass = db.Column(
        db.Float()
        )
    group = db.Column(
        db.String(15)
    )
    year = db.Column(
        db.Integer()
    )
    melting = db.Column(
        db.Float()
    )
    boiling = db.Column(
        db.Float()
    )

