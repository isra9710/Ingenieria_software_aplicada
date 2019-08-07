from models.shared import db
#db = SQLAlchemy()


class DetallePedido(db.Model):
    __tablename__ = "DetallePedido"
    idDetallePedido = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    idPedido = db.Column('idPedido', db.Integer, db.ForeignKey("Pedido.idPedido"))
    idProducto_inventario = db.Column('idMedicamento', db.Integer, db.ForeignKey("Medicamento.idMedicamento"))

    def __init__(self, idPedido, idMedicamento):
        self.idPedido = idPedido
        self.idProducto_inventario = idProducto_inventario
        self.idProducto_inventario = idProducto_inventario

    def __repr__(self):
        return ''
