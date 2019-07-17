from app import db

class Usuario(db.Model):
    __tablename__="Usuario"
    idUsuario=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(45))
    contra=db.Column(db.String(45))
    tipo=db.Column(db.String(45))
    direccion=db.Column(db.String(45))
    RFC=db.Column(db.String(45))

    def __init__(self,idUsuario,nombre,contra,tipo,direccion,RFC):
        self.idUsuario=idUsuario
        self.nombre=nombre
        self.contra=contra
        self.tipo=tipo
        self.direccion=direccion
        self.RFC=RFC