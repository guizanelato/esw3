
from flask import Blueprint, jsonify, redirect, render_template, request 

from models.Associado import Associado,AssociadoStore

blueprint = Blueprint("associado", __name__)

#login_required
@blueprint.route("/associado", methods = ['GET'])
def associado():
    
    associado = Associado(cpf=int(request.args.get('cpf')))
    
    with AssociadoStore() as associado_store:
        context = associado_store.get_associado_plano(associado)

    return render_template("associado.html", context = context )

@blueprint.route("/associado/clinicas")
def associado_clinicas():

    associado = Associado(cpf=int(request.args.get('cpf')))

    with AssociadoStore() as associado_store:
        context = associado_store.get_associado_clinica(associado)

    return render_template("associado_clinica.html", context = context)
