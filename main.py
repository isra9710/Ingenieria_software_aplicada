from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.Usuario import db, Usuario
from models.Proveedor import db,Proveedor
from models.Producto_inventario import  db,Producto_inventario
from models.Producto_catalogo import db, Prod
from models.Pedido import db
from models.DetallePedido import db

import os
app= Flask(__name__)


@app.route("/home")
def index():
    return "Esta es home"

@app.route("/almacen")
def almacen():
    return"Este es el almacen"

if __name__ == "__main__":
    app.run()