class Cliente(db.Model):
    __tablename__ = 'Usuario'
    idCliente = db.Column(db.Integer, primary_key=True)
    idUsuario=db.Column(db.Integer,db.ForeignKey("Usuario.idUsuario"))
    RFC = db.Column(db.String(45))
    direccion = db.Column(db.String(45))
    nombre = db.Column(db.String(45))
    apellidoP = db.Column(db.String(45))
    pedido = relationship("Pedido", backref="Usuario")

    def __init__(self, idCliente, RFC, direccion, tipo, direccion, RFC):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.contra = contra
        self.tipo = tipo
        self.direccion = direccion
        self.RFC = RFC
