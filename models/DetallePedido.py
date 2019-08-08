from models.shared import db


class DetallePedido(db.Model):
    __tablename__ = "DetallePedido"
    idDetallePedido = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    idPedido = db.Column('idPedido', db.Integer, db.ForeignKey("Pedido.idPedido"))
    subTotal = db.Column(db.Float)
    idMedicamento = db.Column('idMedicamento', db.Integer, db.ForeignKey("Medicamento.idMedicamento"))
    nombreMedicamento = db.Column('nombre', db.String(45), db.ForeignKey("Medicamento.nombre"))

    def __init__(self, idPedido, idMedicamento, nombreMedicamento):
        self.idPedido = idPedido
        self.idMedicamento = idMedicamento
        self.nombreMedicamento = nombreMedicamento

    def __repr__(self):
        return ''
