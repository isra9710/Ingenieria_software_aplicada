from sqlalchemy.orm import relationship
from models.shared import db


class Medicamento(db.Model):
    __tablename__ = "Medicamento"
    idMedicamento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), unique=True)
    cantidad = db.Column(db.Integer)
    porcion = db.Column(db.Float)
    descripcion = db.Column(db.String(250))
    fechaE = db.Column(db.Date)
    fechaV = db.Column(db.Date)
    idProveedor = db.Column('idProveedor', db.Integer, db.ForeignKey("Proveedor.idProveedor"))
    idUsuario = db.Column('idUsuario', db.Integer, db.ForeignKey("Usuario.idUsuario"))
    precio = db.Column(db.Float)
    imagen = db.Column(db.String(300))
    detallePedido = relationship("DetallePedido", backref="Medicamento")

    def __init__(self, idProveedor, idUsuario, nombre, cantidad, porcion, descripcion, fechaE, fechaV, precio, imagen):
        self.idProveedor = idProveedor
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.cantidad = cantidad
        self.porcion = porcion
        self.descripcion = descripcion
        self.fechaE = fechaE
        self.fechaV = fechaV
        self.precio = precio
        self.imagen = imagen

    def __repr__(self):
        return ''
