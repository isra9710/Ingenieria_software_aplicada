from sqlalchemy.orm import relationship
from models.shared import db


class Proveedor(db.Model):
    __tablename__ = 'Proveedor'
    idProveedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), unique=True)
    rfc = db.Column(db.String(13))
    telefono = db.Column(db.String(10))
    medcamento = relationship("Medicamento", backref="Proveedor")

    def __init__(self, nombre, rfc, telefono):
        self.nombre = nombre
        self.rfc = rfc
        self.telefono = telefono

    def __repr__(self):
        return ''