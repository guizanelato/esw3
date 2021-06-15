
from flask import Flask, render_template
from routes.auth import blueprint as auth
from routes.associado import blueprint as associado

from models.Associado import Associado, AssociadoStore
from models.Plano import Plano, PlanoStore
from models.User import User,UserStore

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(auth)
app.register_blueprint(associado)


@app.route("/teste")
def teste():
    return render_template("listar_clinica.html")
