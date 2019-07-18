from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,Integer,Date
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class Producto_inventario(db.Model):
    __tablename__ = "Producto_inventario"
    idProdcuto_inventario = db.Column(db.Integer, primary_key=True)
    idProveedor = db.Column(db.Integer, ForeignKey("Proveedor.idProveedor"))
    idUsuario = db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.Integer)
    porcion = db.Column(db.Float)
    descripcion = db.Column(db.String(300))
    fecha_elaboracion = db.Column(db.Date)
    fecha_vencimiento = db.Column(db.Date)
    precio = db.Column(db.Float)
    pedido = relationship("Pedido", backref="Producto_inventario")
    detallePedido = relationship("DetallePedido", backref="Producto_inventario")

    def __init__(self, idProdcuto_inventario, idProveedor,idUsuario,nombre,cantidad,porcion,descripcion,fecha_elaboracion,fecha_vencimiento,precio):
        self.idProdcuto_inventario=idProdcuto_inventario
        self.idProveedor=idProveedor
        self.idUsuario=idUsuario
        self.nombre=nombre
        self.cantidad=cantidad
        self.porcion=porcion
        self.descripcion=descripcion
        self.fecha_elaboracion=fecha_elaboracion
        self.fecha_vencimiento=fecha_vencimiento
        self.precio=precio

