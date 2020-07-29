from app import app
from models import db, Element

db.drop_all()
db.create_all()

h = Element(
    id=1,
    name="Hydrogen",
    symbol="H",
    mass= 1.008
)

he = Element(
    id=2,
    name="Helium",
    symbol="He",
    mass= 4.0026
)

li = Element(
    id=3,
    name="Lithium",
    symbol="Li",
    mass=6.94
)

db.session.add_all([h, he, li])
db.session.commit()