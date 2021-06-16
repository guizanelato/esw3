
from flask import Flask, render_template
from routes.auth import blueprint as auth
from routes.associado import blueprint as associado

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(auth)
app.register_blueprint(associado)


