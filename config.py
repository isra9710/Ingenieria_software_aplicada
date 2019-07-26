
##Este es el archivo que contiene la importancia de clases y algunas configuraciones que tienen que ir en el main, esto con la finalidad de reducir codigo
import os
from models.Usuario import Usuario
from models.Proveedor import Proveedor
from models.ProductoInventario import Producto_inventario
from models.Pedido import Pedido
from models.DetallePedido import DetallePedido
from models.Cliente import Cliente

class Config(object):
    SECRET_KEY = "my_secret_key"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/baseDS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
