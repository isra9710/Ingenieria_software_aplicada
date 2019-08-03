from sqlalchemy.orm import relationship
from models.shared import db


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    idEstado = db.Column('idEstado', db.Integer, db.ForeignKey("Estado.idEstado"))
    nombre = db.Column(db.String(15), unique=True)
    contra = db.Column(db.String(10))
    tipo = db.Column(db.String(15))
    cliente = relationship("Cliente", backref="Usuario")
    productoI = relationship("Medicamento", backref="Usuario")

    def __init__(self, nombre, contra, tipo, idEstado):

        self.nombre = nombre
        self.contra = contra
        self.tipo = tipo
        self.idEstado = idEstado

    def __repr__(self):
        return ''