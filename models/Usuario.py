from sqlalchemy.orm import relationship
from models.shared import db


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    contra = db.Column(db.String(45))
    tipo = db.Column(db.String(45))
    cliente = relationship("Cliente", backref="Usuario")
    productoI = relationship("ProductoInventario", backref="Usuario")

    def __init__(self, nombre, contra, tipo):

        self.nombre = nombre
        self.contra = contra
        self.tipo = tipo
