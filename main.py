from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from Usuario import Usuario,db

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/baseDS'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Pagina principal"



@app.route("/home")
def home():
    return "Esta es home"


@app.route("/almacen")
def almacen():
    return"Este es el almacen"


if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
