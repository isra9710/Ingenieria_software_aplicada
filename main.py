from flask import Flask, render_template, request, session, flash, redirect, url_for
import os
app = Flask(__name__)
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
    f = request.files['file']
    folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0:-1]
    f.save('/'.join(folder) + '/static/' + f.filename)
    if request.form.get("nombre") is not None and request.form.get("emple") is not None and request.form.get("proveedor") is not None:
        medicamento = ProductoInventario.query.filter_by(nombre=request.form["nombre"]).first()
    else:
        flash("No seleccionaste empleado o proveedor, no se agrego el medicamento")
        return crudMedicamentos()
    if medicamento is not None and request.form.get("nombre") == medicamento.nombre:
        flash("Ese medicamento ya existe!")
        return crudMedicamentos()
    else:
        administrador = Usuario.query.filter_by(nombre=request.form["emple"]).first()
        proveedor = Proveedor.query.filter_by(nombre=request.form["proveedor"]).first()
        medicamento = ProductoInventario(proveedor.idProveedor, administrador.idUsuario, request.form.get("nombre"),request.form.get("cantidad"), request.form.get("porcion"), request.form.get("descripcion"), request.form.get("fechaE"), request.form.get("fechaV"), request.form.get("precio"), f.filename)
        flash("Se agrego medicamento con exito")
        db.session.add(medicamento)
        db.session.commit()
        return crudMedicamentos()


@app.route("/llenareditar/<string:id>", methods=['GET', 'POST'])#esta parte es para llenar el formulario con los datos traidos de "mostrar universiadades"
def llenareditar(id):
    medicamento = ProductoInventario.query.filter_by(idProducto_inventario=id).first()
    empleado = Usuario.query.filter_by(idUsuario=medicamento.idUsuario).first()
    empleados = Usuario.query.all()
    proveedores = Proveedor.query.all()
    proveedor = Proveedor.query.filter_by(idProveedor=medicamento.idProveedor).first()
    return render_template("editarMedicamentos.html", medicamento=medicamento, empleado=empleado, empleados=empleados, proveedor=proveedor, proveedores=proveedores)


@app.route("/editarMedicamento")
def editarMedicamento():
    medicaO = ProductoInventario.query.filter_by(idProducto_inventario=id).first()
    string ="hola"
    f = request.files['file']
    folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0:-1]
    f.save('/'.join(folder) + '/static/' + f.filename)
    if request.form.get("file") is None:
        string = medicaO.imagen
    else:
        string = f.filename
    if medicaO.nombre == request.form.get("nombre"):
        

    return crudMedicamentos()


@app.route("/prueba")
def prueba():
    return render_template("index.html")


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
