from sqlalchemy.orm import relationship
from models.shared import db
#db = SQLAlchemy()


class Pedido(db.Model):
    __tablename__ = "Pedido"
    idPedido = db.Column(db.Integer, primary_key=True)
    idCliente = db.Column('idCliente', db.Integer, db.ForeignKey("Cliente.idCliente"))
    total = db.Column(db.Float)
    detallePedido = relationship("DetallePedido", backref="Pedido")

    def __init__(self, idUsuario, total):
        self.idUsuario = idUsuario
        self.total = total
