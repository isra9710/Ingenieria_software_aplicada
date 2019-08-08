from models.shared import db


class DetallePedido(db.Model):
    __tablename__ = "DetallePedido"
    idDetallePedido = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    idPedido = db.Column('idPedido', db.Integer, db.ForeignKey("Pedido.idPedido"))
    subTotal = db.Column(db.Float)
    nombreMedicamento = db.Column('nombreMedicamento', db.String(45), db.ForeignKey("Medicamento.nombre"))

    def __init__(self, idPedido, nombreMedicamento, subTotal, cantidad):
        self.idPedido = idPedido
        self.nombreMedicamento = nombreMedicamento
        self.subTotal = subTotal
        self.cantidad = cantidad

    def __repr__(self):
        return ''
