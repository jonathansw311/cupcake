from models import Cupcake, db, connect_db
from app import app

db.drop_all()
db.create_all()

c1=Cupcake(flavor='chocolate', size='large', rating=4.5)
c2=Cupcake(flavor='Vanilla', size='large', rating=4.54)
c3=Cupcake(flavor='Bacon', size='x-large', rating=3.33)
db.session.add_all([c1,c2, c3])
db.session.commit()