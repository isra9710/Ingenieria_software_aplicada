from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,Integer,Date
from sqlalchemy.orm import relationship
db = SQLAlchemy()


class DetallePedido(db.Model):
    __tablename__ = "DetallePedido"
    idDetallePedido = db.Column(db.Integer, primary_key=True)
    idPedido = db.Column(db.Integer, ForeignKey="Pedido.idPedido")
    idUsuario = db.Column(db.Integer, ForeignKey="Usuario.idUsuario")
    idProducto_inventario = db.Column(db.Integer, ForeignKey="Producto_inventario.idProducto_inventario")

    def __init__(self, idDetallePedido, idPedido, idUsuario, idProducto_inventario):
        self.idDetallePedido = idDetallePedido
        self.idPedido = idPedido
        self.idUsuario = idUsuario
        self.idProducto_inventario = idProducto_inventario
