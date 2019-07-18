from sqlalchemy.orm import relationship
from models.shared import db
#db = SQLAlchemy()


class Producto_inventario(db.Model):
    __tablename__ = "Producto_inventario"
    idProducto_inventario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.Integer)
    porcion = db.Column(db.Float)
    descripcion = db.Column(db.String(300))
    fecha_elaboracion = db.Column(db.Date)
    fecha_vencimiento = db.Column(db.Date)
    idProveedor = db.Column('idProveedor', db.Integer, db.ForeignKey("Proveedor.idProveedor"))
    idUsuario = db.Column('idUsuario', db.Integer, db.ForeignKey("Usuario.idUsuario"))
    precio = db.Column(db.Float)
    detallePedido = relationship("DetallePedido", backref="Producto_inventario")

    def __init__(self, idProdcuto_inventario, idProveedor, idUsuario, nombre, cantidad, porcion, descripcion, fecha_elaboracion, fecha_vencimiento, precio):
        self.idProdcuto_inventario = idProdcuto_inventario
        self.idProveedor = idProveedor
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.cantidad = cantidad
        self.porcion = porcion
        self.descripcion = descripcion
        self.fecha_elaboracion = fecha_elaboracion
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio

