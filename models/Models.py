from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    contra = db.Column(db.String(45))
    tipo = db.Column(db.String(45))
    direccion = db.Column(db.String(45))
    RFC = db.Column(db.String(45))
    productoInventario = relationship("Producto_inventario", backref="Usuario")
    productoCatalogo = relationship("Producto_catalogo", backref="Usuario")
    pedido = relationship("Pedido", backref="Usuario")
    detallePedido = relationship("DetallePedido", backref="Usuario")

    def __init__(self, idUsuario, nombre, contra, tipo, direccion, RFC):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.contra = contra
        self.tipo = tipo
        self.direccion = direccion
        self.RFC = RFC


class Proveedor(db.Model):
    __tablename__ = 'Proveedor'
    idProveedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    RFC = db.Column(db.String(45))
    telefono = db.Column(db.String(45))
    productoInventario = relationship("Producto_inventario", backref="Proveedor")
    productoCatalogo = relationship("Producto_catalogo", backref="Proveedor")

    def __init__(self, idProveedor, nombre, RFC, telefono):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.RFC = RFC
        self.telefono = telefono


class Producto_inventario(db.Model):
    __tablename__ = "Producto_inventario"
    idProdcuto_inventario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.Integer)
    porcion = db.Column(db.Float)
    descripcion = db.Column(db.String(300))
    fecha_elaboracion = db.Column(db.Date)
    fecha_vencimiento = db.Column(db.Date)
    idProveedor = db.Column(db.Integer, ForeignKey("Proveedor.idProveedor"))
    idUsuario = db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    precio = db.Column(db.Float)
    detallePedido = relationship("DetallePedido", backref="Producto_inventario")

    def __init__(self, idProdcuto_inventario, idProveedor,idUsuario,nombre,cantidad,porcion,descripcion,fecha_elaboracion,fecha_vencimiento,precio):
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


class Producto_catalogo(db.Model):
    __tablename__ = "Producto_catalogo"
    idProducto_catalogo=db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(45))
    porcion = db.Column(db.Float)
    descripcion = db.Column(db.String(300))
    idProveedor = db.Column(db.Integer, ForeignKey("Proveedor.idProveedor"))
    idUsuario = db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    precio = db.Column(db.Float)

    def __init__(self,idProducto_catologo,idProveedor,idUsuario,nombre,porcion,descripcion,precio):
        self.idProducto_catalogo = idProducto_catologo
        self.idUsuario = idUsuario
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.porcion = porcion
        self.descripcion = descripcion
        self.precio = precio


class Pedido(db.Model):
    __tablename__ = "Pedido"
    idPedido = db.Column(db.Integer,primary_key=True)
    idUsuario = db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    total = db.Column(db.Float)
    detallePedido = relationship("DetallePedido", backref="Pedido")

    def __init__(self, idPedido, idUsuario, total):
        self.idPedido = idPedido
        self.idUsuario = idUsuario
        self.total = total


class DetallePedido(db.Model):
    __tablename__ = "DetallePedido"
    idDetallePedido = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    idPedido = db.Column(db.Integer, ForeignKey("Pedido.idPedido"))
    idUsuario = db.Column(db.Integer, ForeignKey("Usuario.idUsuario"))
    idProducto_inventario = db.Column(db.Integer, ForeignKey("Producto_inventario.idProdcuto_inventario"))

    def __init__(self, idDetallePedido, idPedido, idUsuario, idProducto_inventario):
        self.idDetallePedido = idDetallePedido
        self.idPedido = idPedido
        self.idUsuario = idUsuario
        self.idProducto_inventario = idProducto_inventario