from sqlalchemy.orm import relationship
from models.shared import db
#db = SQLAlchemy()


class Estado(db.Model):
    __tablename__ = 'Estado'
    idEstado = db.Column(db.Integer, primary_key=True)
    nombreEstado = db.Column(db.String(20))
    numEstado = db.Column(db.Integer)
    zona = db.Column(db.String(10))

    usuario = relationship("usuario", backref="Estado")

    def __init__(self, nombreEstado, numEstado, zona):
        self.nombreEstado = nombreEstado
        self.numEstado = numEstado
        self.zona = zona

    def __repr__(self):
        return ''