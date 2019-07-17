from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,Integer,Date
from sqlalchemy.orm import relationship
db=SQLAlchemy()

class Usuario(db.Model):
    __tablename__="Usuario"
    idUsuario=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(45))
    contra=db.Column(db.String(45))
    tipo=db.Column(db.String(45))
    direccion=db.Column(db.String(45))
    RFC=db.Column(db.String(45))
    productoInventario=relationship("Producto_inventario", back_populates="Usuario")
    productoCatalogo=relationship("Producto_catalogo", back_populates="Usuario")
    pedido=relationship("Pedido", back_pupulates="Usuario")
    detallePedido=relationship("DetallePedido", back_populates="Usuario")

    def __init__(self,idUsuario,nombre,contra,tipo,direccion,RFC):
        self.idUsuario=idUsuario
        self.nombre=nombre
        self.contra=contra
        self.tipo=tipo
        self.direccion=direccion
        self.RFC=RFC