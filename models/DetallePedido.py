from models.shared import db
#db = SQLAlchemy()


class DetallePedido(db.Model):
    __tablename__ = "DetallePedido"
    idDetallePedido = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    idPedido = db.Column('idPedido', db.Integer, db.ForeignKey("Pedido.idPedido"))
    idUsuario = db.Column('idUsuario', db.Integer, db.ForeignKey("Usuario.idUsuario"))
    idProducto_inventario = db.Column('idProducto_inventario', db.Integer, db.ForeignKey("Producto_inventario.idProducto_inventario"))

    def __init__(self, idPedido, idUsuario, idProducto_inventario):
        self.idPedido = idPedido
        self.idUsuario = idUsuario
        self.idProducto_inventario = idProducto_inventario
