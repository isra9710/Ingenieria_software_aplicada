from sqlalchemy.orm import relationship
from models.shared import db
#db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    contra = db.Column(db.String(45))
    tipo = db.Column(db.String(45))
    direccion = db.Column(db.String(45))
    RFC = db.Column(db.String(45))
    productoInventario = relationship("Producto_inventario", backref="Usuario")
    productoCatalogo = relationship("Producto_catalogo", backref="Usuario")
    pedido = relationship("Pedido", backref="Usuario")
    detallePedido = relationship("DetallePedido", backref="Usuario")

    def __init__(self, nombre, contra, tipo, direccion, RFC):

        self.nombre = nombre
        self.contra = contra
        self.tipo = tipo
        self.direccion = direccion
        self.RFC = RFC