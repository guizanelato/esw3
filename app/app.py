
from flask import Flask, render_template
from routes.auth import blueprint as auth


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(auth)


@app.route("/listar_paciente")
def get_pacientes():
    return render_template("listar_paciente.html")

@app.route("/listar_clinica")
def get_clinicas():
    return render_template("listar_clinica.html")

@app.route("/teste")
def get_teste():
    pass

