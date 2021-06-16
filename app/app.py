
from flask import Flask, render_template, request, jsonify
from routes.auth import blueprint as auth
from routes.associado import blueprint as associado

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(auth)
app.register_blueprint(associado)

@app.route("/teste" , methods = [ 'GET', 'POST'])
def teste():
    if request.method == 'POST':
        return jsonify(request.form)
        

    return render_template("associado_agendamento.html")
