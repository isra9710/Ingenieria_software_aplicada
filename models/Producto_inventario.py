from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,Integer,Date
from sqlalchemy.orm import relationship

db=SQLAlchemy()

class Producto_inventario(db.Model):
    __tablename__ = "Producto_inventario"
    idProdcuto_inventario= db.Column(db.Integer, primary_key=True)
    idProveedor = db.Column(db.Integer, ForeignKey("Proveedor.idProveedor"))
    idUsuario=db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    nombre = db.Column(db.String(45))
    cantidad=db.Column(db.Integer)
    porcion=db.Column(db.Float)
    descripcion=db.Column(db.String(300))
    fecha_elaboracion=db.Column(db.Date)
    fecha_vencimiento=db.Column(db.Date)
    precio=db.Column(db.Float)
    pedido=relationship("Pedido", back_populates="Producto_inventario")
    detallePedido=relationship("DetallePedido", back_populates="Producto_inventario")
