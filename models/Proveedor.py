from sqlalchemy.orm import relationship
from models.shared import db
#db = SQLAlchemy()


class Proveedor(db.Model):
    __tablename__ = 'Proveedor'
    idProveedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    rfc = db.Column(db.String(45))
    telefono = db.Column(db.String(45))
    productoInventario = relationship("ProductoInventario", backref="Proveedor")

    def __init__(self, nombre, rfc, telefono):
        self.nombre = nombre
        self.rfc = rfc
        self.telefono = telefono

