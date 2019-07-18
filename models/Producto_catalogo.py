from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,Integer,Date
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class Producto_catalogo(db.Model):
    __tablename__ = "Producto_catalogo"
    idProducto_catalogo=db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(45))
    idProveedor = db.Column(db.Integer, ForeignKey("Proveedor.idProveedor"))
    idUsuario = db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    porcion = db.Column(db.Float)
    descripcion = db.Column(db.String(300))
    precio = db.Column(db.Float)

    def __init__(self,idProducto_catologo,idProveedor,idUsuario,nombre,porcion,descripcion,precio):
        self.idProducto_catalogo = idProducto_catologo
        self.idUsuario = idUsuario
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.porcion = porcion
        self.descripcion = descripcion
        self.precio = precio
