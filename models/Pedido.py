from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,Integer,Date
from sqlalchemy.orm import relationship
db=SQLAlchemy()

class Pedido(db.Model):
    __tablename__ = "Pedido"
    idPedido=db.Column(db.Integer,primary_key=True)
    idUsuario=db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    total=db.Column(db.Float)
    detallePedido=relationship("DetallePedido", back_populates="Pedido")