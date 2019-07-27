from flask import Flask, render_template, request, session, flash, redirect, url_for
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/baseDS'  # conexion con la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Cosa extra para evitar notificaciones
from config import *#en el archivo config se encuentran importadas todas las clases, esto para tener menos codigo en el main
from models.shared import db#se importa el objeto de SQLAlchemy para tenerlo en todos los modulos que se necesiten


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    usuario = Usuario.query.filter_by(nombre=request.form['usuario']).first()
    if usuario:
        if usuario.contra == request.form.get("contra"):
            if usuario.tipo == "Administrador":
                return render_template("admin.html")
            elif usuario.tipo == "Empleado":
                return render_template("empleado.html")
            else:
                return render_template("cliente.html")
        else:
            return render_template("index.html")

    else:
        render_template("index.html")


@app.route("/home")
def home():
    return "Esta es home"


@app.route("/almacen")
def almacen():
    return"Este es el almacen"


@app.route("/administrador")
def administrador():
    return render_template("Administrador.html")


@app.route("/insertar")
def insertar():
    usuario = Proveedor("Isra", "RCIO", "7773123")
    db.session.add(usuario)
    db.session.commit()
    return "Usuario ingresado"


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
