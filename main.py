from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
app = Flask(__name__)
SECRET_KEY = "my_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/baseDS'  # conexion con la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Cosa extra para evitar notificaciones
from config import * #en el archivo config se encuentran importadas todas las clases, esto para tener menos codigo en el main
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


@app.route("/mostrarMedicamentos")
def crudMedicamentos():
    medicamentos = ProductoInventario.query.all()
    administradores = Usuario.query.filter_by(tipo="Administrador")
    proveedores = Proveedor.query.all()
    return render_template("mostrarMedicamentos.html", medicamentos=medicamentos, administradores=administradores, proveedores=proveedores)


@app.route("/agregarMedicamento", methods=['GET', 'POST'])
def agregarMedicamento():
    #if "username" in session:
   if request.method == "POST":
        nombre = request.form.get("nombre")
        emple = request.form.get("emple")
        proveedor = request.form.get("proveedor")
        cantidad = request.form.get("cantidad")
        porcion = request.form.get("porcion")
        descripcion = request.form.get("descripcion")
        fechaE = request.form.get("fechaE")
        fechaV = request.form.get("fechaV")
        precio = request.form.get("precio")
        f = request.files['file']
        folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0:-1]
        f.save('/'.join(folder) + '/static/' + f.filename)
        nombreAux = None
        if nombre is not None:
            medicamentos = ProductoInventario.query.filter_by(nombre=nombre)
            if medicamentos is not None:
                for e in medicamentos:
                    nombreAux = e.nombre
        else:
            flash("Selecciona el nombre de un administrador, no se agrego la universidad")
            return crudMedicamentos()
        if nombre == nombreAux:
            flash("Ese medicamento ya existe!")
            return crudMedicamentos()
        else:
            print("Estas procediendo a registrarla")
            administrador = Usuario.query.filter_by(nombre=emple).first()
            proveedor = Proveedor.query.filter_by(nombre=proveedor).first()
            medicamento = ProductoInventario(proveedor.idProveedor, administrador.idUsuario, nombre, cantidad, porcion, descripcion, fechaE, fechaV, precio, f.filename)
            flash("Se agrego medicamento con exito")
            db.session.add(medicamento)
            db.session.commit()
            return crudMedicamentos()





@app.route("/prueba")
def prueba():
    return render_template("index.html")
if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
