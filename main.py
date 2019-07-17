from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app= Flask(__name__)
app.config= "sqlite:///"+"Proyecto_final/Ingenieria_software_aplicada/Base/"
db=SQLAlchemy(app)
@app.route("/home")
def index():
    return "Esta es home"

@app.route("/almacen")
def almacen():
    return"Este es el almacen"

if __name__ == "__main__":
    app.run()