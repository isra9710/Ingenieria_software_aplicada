from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,Integer,Date
from sqlalchemy.orm import relationship
db=SQLAlchemy()

class Proveedor(db.Model):
    __tablename__="Proveedor"
    idProveedor=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(45))
    RFC=db.Column(db.String(45))
    telefono=db.Column(db.String(45))
    productoInventario = relationship("Producto_inventario", back_populates="Proveedor")
    productoCatalogo = relationship("Producto_catalogo", back_populates="Proveedor")

    def __init__(self,idProveedor,nombre,RFC,telefono):
        self.idProveedor=idProveedor
        self.nombre=nombre
        self.RFC=RFC
        self.telefono=telefono

