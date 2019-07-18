from models.shared import db
#db = SQLAlchemy()


class Producto_catalogo(db.Model):
    __tablename__ = "Producto_catalogo"
    idProducto_catalogo=db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(45))
    porcion = db.Column(db.Float)
    descripcion = db.Column(db.String(300))
    idProveedor = db.Column('idProveedor', db.Integer, db.ForeignKey("Proveedor.idProveedor"))
    idUsuario = db.Column('idUsuario', db.Integer, db.ForeignKey("Usuario.idUsuario"))
    precio = db.Column(db.Float)

    def __init__(self,idProducto_catologo,idProveedor,idUsuario,nombre,porcion,descripcion,precio):
        self.idProducto_catalogo = idProducto_catologo
        self.idUsuario = idUsuario
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.porcion = porcion
        self.descripcion = descripcion
        self.precio = precio
