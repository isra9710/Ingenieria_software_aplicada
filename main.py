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
                session['username'] = request.form['usuario']
                return redirect((url_for('administrador')))
            elif usuario.tipo == "Empleado":
                session['username'] = request.form['usuario']
                return redirect((url_for('empleado')))
            else:
                session['username'] = request.form['usuario']
                return redirect((url_for('cliente')))
        else:
            return render_template("index.html")

    else:
        render_template("index.html")

#Inicio de las funciones de paginas principales de los 3 tipos de usuario, cliente, empleado, administrador#
@app.route("/cliente")
def cliente():
    return render_template("cliente/cliente.html")


@app.route("/empleado")
def empleado():
    return render_template("empleado/empleado.html")


@app.route("/administrador")
def administrador():
    return render_template("administrador/admin.html")
#Fin de las funciones de paginas principales de los 3 tipos de usuario, cliente, empleado, administrador#


#Aqui empiezan los CRUD#
@app.route("/mostrarMedicamentos")
def mostrarMedicamentos():
    medicamentos = Medicamento.query.all()
    administradores = Usuario.query.filter_by(tipo="Administrador")
    proveedores = Proveedor.query.all()
    return render_template("administrador/mostrarMedicamentos.html", medicamentos=medicamentos, administradores=administradores, proveedores=proveedores)


@app.route("/agregarMedicamento", methods=['GET', 'POST'])
def agregarMedicamento():
 if request.method == "POST":
    f = request.files['file']
    folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0:-1]
    f.save('/'.join(folder) + '/static/' + f.filename)
    if request.form.get("nombre") is not None and request.form.get("emple") is not None and request.form.get("proveedor") is not None:
        medicamento = Medicamento.query.filter_by(nombre=request.form["nombre"]).first()
    else:
        flash("No seleccionaste empleado o proveedor, no se agrego el medicamento")
        return redirect((url_for('mostrarMedicamentos')))
    if medicamento is not None and request.form.get("nombre") == medicamento.nombre:
        flash("Ese medicamento ya existe!")
        return redirect((url_for('mostrarMedicamentos')))
    else:
        administrador = Usuario.query.filter_by(nombre=request.form["emple"]).first()
        proveedor = Proveedor.query.filter_by(nombre=request.form["proveedor"]).first()
        medicamento = Medicamento(proveedor.idProveedor, administrador.idUsuario, request.form.get("nombre"), request.form.get("cantidad"), request.form.get("porcion"), request.form.get("descripcion"), request.form.get("fechaE"), request.form.get("fechaV"), request.form.get("precio"), f.filename)
        flash("Se agrego medicamento con exito")
        db.session.add(medicamento)
        db.session.commit()
        return redirect((url_for('mostrarMedicamentos')))


@app.route("/llenareditar/<string:id>", methods=['GET', 'POST'])#esta parte es para llenar el formulario con los datos traidos
def llenareditar(id):
    medicamento = Medicamento.query.filter_by(idMedicamento=id).first()
    empleado = Usuario.query.filter_by(idUsuario=medicamento.idUsuario).first()
    empleados = Usuario.query.all()
    proveedores = Proveedor.query.all()
    proveedor = Proveedor.query.filter_by(idProveedor=medicamento.idProveedor).first()
    return render_template("administrador/editarMedicamentos.html", medicamento=medicamento, empleado=empleado, empleados=empleados, proveedor=proveedor, proveedores=proveedores)


@app.route("/editarMedicamento", methods=['GET', 'POST'])
def editarMedicamento():
    if request.method == "POST":
        medicaO = Medicamento.query.filter_by(idMedicamento=request.form['idMedicamento']).first()
        proveedor = Proveedor.query.filter_by(nombre=request.form["proveedor"]).first()
        usuario = Usuario.query.filter_by(nombre=request.form["usuario"]).first()
        if validarNombreM(medicaO.nombre, request.form['nombre']):
            medicaO.idProveedor = proveedor.idProveedor
            medicaO.idUsuario = usuario.idUsuario
            medicaO.nombre = request.form['nombre']
            medicaO.cantidad = request.form['cantidad']
            medicaO.porcion = request.form['porcion']
            medicaO.descripcion = request.form['descripcion']
            medicaO.fechaE = request.form['fechaE']
            medicaO.fechaV = request.form['FechaV']
            db.commit()
            flash("Medicamento editado con exito")
            return redirect((url_for('mostrarMedicamentos')))
        else:
            flash("Ocurrio un problema al editar")
            return redirect((url_for('mostrarMedicamentos')))


def validarNombreM(nombreO, nombreN):
    medicamentoO = Medicamento.query.filter_by(nombre=nombreO).first()
    if nombreO == nombreN:
        return True
    else:
        medicamentoN = Usuario.query.filter(Medicamento.idMedicamento != medicamentoO.idUsuario, Medicamento.nombre == nombreN).all()
        if medicamentoN:
            return False
        else:
            return True


@app.route('/eliminarMedicamento/<string:id>', methods=['GET', 'POST'])
def eliminarMedicamento(id):
    medica = Medicamento.query.filter_by(idMedicamento=id).first()
    db.session.delete(medica)
    db.session.commit()
    flash("Medicamento eliminado con exito")
    return redirect((url_for('mostrarMedicamentos')))


@app.route('/mostrarEmpleados')
def mostrarEmpleados():
    empleados = Usuario.query.filter_by(tipo="Empleado")
    estados = Estado.query.all()
    return render_template("administrador/mostrarEmpleados.html", empleados=empleados, estados=estados)


@app.route("/agregarEmpleado", methods=['GET', 'POST'])
def agregarEmpleado():
    usuario = Usuario.query.filter_by(nombre=request.form['nombre']).all()
    if usuario:
        flash("Ese usuario ya existe")
        return redirect((url_for('mostrarEmpleados')))
    elif request.form['estado'] is not None:
        estado = Estado.query.filter_by(nombreEstado=request.form['estado']).first()
        empleado = Usuario(request.form['nombre'], request.form['contra'], "Empleado", estado.idEstado)
        db.session.add(empleado)
        db.session.commit()
        flash("Usuario registrado correctamente, pidale al mismo que cambie su contraseña")
        return redirect((url_for('mostrarEmpleados')))
    else:
        flash("Ingresaste un dato erroneo")
        return redirect((url_for('mostrarEmpleados')))


@app.route("/llenareditarEmpleado/<string:id>", methods=['GET', 'POST'])#esta parte es para llenar el formulario con los datos solicitados
def llenareditarEmpleado(id):
    empleado = Usuario.query.filter_by(idUsuario=id).first()
    estadoO = Estado.query.filter_by(idEstado=empleado.idEstado).first()
    estados = Estado.query.all()
    return render_template("administrador/editarEmpleados.html", empleado=empleado, estadoO=estadoO, estados=estados)



@app.route("/editarEmpleado", methods=['GET', 'POST'])
def editarEmpleado():
    usuario = Usuario.query.filter_by(idUsuario=request.form["idUsuario"]).first()
    estado = Estado.query.filter_by(nombreEstado=request.form['estado']).first()
    if validarNombreU(usuario.nombre, request.form['nombre']) is True:
        usuario.nombre = request.form['nombre']
        usuario.idEstado = estado.idEstado
        usuario.contra = request.form['contra']
        db.session.commit()
        flash("Empleado editado")
        return redirect((url_for('mostrarEmpleados')))
    else:
        flash("Ocurrio un error, quiza el nombre que editaste ya existe o ingresaste algun otro dato erroneo")
        return redirect((url_for('mostrarEmpleados')))


def validarNombreU(nombreO,nombreN):
    usuarioO = Usuario.query.filter_by(nombre=nombreO).first()
    if nombreO == nombreN:
        return True
    else:
        usuarioN = Usuario.query.filter(Usuario.idUsuario != usuarioO.idUsuario, Usuario.nombre == nombreN).all()
        if usuarioN:
            return False
        else:
            return True


@app.route('/eliminarEmpleado/<string:id>', methods=['GET', 'POST'])
def eliminarEmpleado(id):
    empleado = Usuario.query.filter_by(idUsuario=id).first()
    db.session.delete(empleado)
    db.session.commit()
    flash("Empleado eliminado con exito")
    return redirect((url_for('mostrarEmpleados')))


@app.route('/mostrarProveedores')
def mostrarProveedores():
    proveedores = Proveedor.query.all()
    return render_template("administrador/mostrarProveedores.html", proveedores=proveedores)


@app.route("/agregarProveedor", methods=['GET', 'POST'])
def agregarProveedor():
    pro = Proveedor.query.filter_by(nombre=request.form['nombre']).all()
    if pro:
        flash("Ese proveedor ya esta registrado con nosotros")
        return redirect((url_for('mostrarProveedores')))
    pro = Proveedor.query.filter_by(rfc=request.form['rfc'])
    clien = Cliente.query.filter_by(rfc=request.form['rfc'])
    if pro or clien:
        flash("Ese rfc ya se encuentra registrado")
        return redirect((url_for('mostrarProveedores')))
    else:
        proveedor = Proveedor(request.form.get["nombre"], request.form.get["rfc"], request.form.get["tel"])
        db.session.add(proveedor)
        db.session.commit()
        flash("Proveedor registrado correctamente")
        return redirect((url_for('mostrarProveedores')))


@app.route("/llenareditarProveedor/<string:id>", methods=['GET', 'POST'])#esta parte es para llenar el formulario con los datos traidos
def llenareditarProveedor(id):
    proveedor = Proveedor.query.filter_by(idProveedor=id).first()
    return render_template("administrador/editarProveedores.html", proveedor=proveedor)


@app.route("/editarProveedor", methods=['GET', 'POST'])
def editarProveedor():
    usuario = Usuario.query.filter_by(idUsuario=request.form["idUsuario"]).first()
    estado = Estado.query.filter_by(nombreEstado=request.form['estado']).first()
    if validarNombreU(usuario.nombre, request.form['nombre']) is True:
        usuario.nombre = request.form['nombre']
        usuario.idEstado = estado.idEstado
        usuario.contra = request.form['contra']
        db.session.commit()
        flash("Empleado editado")
        return redirect((url_for('mostrarProveedores')))
    else:
        flash("Ocurrio un error, quiza el nombre que editaste ya existe o ingresaste algun otro dato erroneo")
        return redirect((url_for('mostrarProveedores')))


def validarNombreP(nombreO, nombreN):
    proveeO = Proveedor.query.filter_by(nombre=nombreO).first()
    if nombreO == nombreN:
        return True
    else:
        proveeN = Proveedor.query.filter(Proveedor.idProveedor != proveeO.idProveedor, Proveedor.nombre == nombreN).all()
        if proveeN:
            return False
        else:
            return True

@app.route('/eliminarProveedor/<string:id>', methods=['GET', 'POST'])
def eliminarEmpleado(id):
    proveedor= Proveedor.query.filter_by(idProveedor=id).first()
    db.session.delete(proveedor)
    db.session.commit()
    flash("Empleado eliminado con exito")
    return redirect((url_for('mostrarProveedores')))
#Aqui terminan los CRUD


@app.route("/catalogo")
def prueba():
    medicamentos = Medicamento.query.all()
    return render_template("cliente/catalogo.html", medicamentos=medicamentos)

@app.route("/aniadirC/<string:id>")
def aniadirC(id):
    nombre = session['username']
    usuario = Usuario.query.filter_by(nombre=nombre)
    if 'carrito' not in session:
        pedido = Pedido(usuario.idUsuario, 0.0)
        db.session.add(pedido)
        db.session.commit()
        session['carrito'] = pedido.idPedido
    idPedido = session['carrito']
    medicamento = Medicamento.query.filter_by(idMedicamento=id).first()
    subTotal = medicamento.precio*request.form.get('cantidad')
    detalleP = DetallePedido(idPedido, id, subTotal)
    db.session.add(detalleP)
    db.session.commit()
    consulta = DetallePedido.query.filterby(idPedido=idPedido)
    return render_template("/cliente/carrito.html", consulta=consulta)


@app.route("/eliminarC/<string:id>")
def eliminarC(id):
    idPedido = session['carrito']
    detalleP = DetallePedido.query.filter(idPedido=idPedido, idMedicamento=id).first()
    db.session.delete(detalleP)
    db.session.commit()


@app.route("/terminarC")
def terminarC():
    session.pop('carrito')
    return redirect((url_for('cliente')))


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()

