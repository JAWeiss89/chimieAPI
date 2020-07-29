from app import app
from models import db, Element

db.drop_all()
db.create_all()

h = Element(
    name="Hydrogen"
)

h2 = Element(
    name="Helium"
)

al = Element(
    name="Aluminum"
)

db.session.add_all([h, h2, al])
db.session.commit()