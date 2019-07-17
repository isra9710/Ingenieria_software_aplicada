from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Producto_catalogo(db.Model):
    idProducto_catalogo=db.Column(db.Integer, primary_key= True)
