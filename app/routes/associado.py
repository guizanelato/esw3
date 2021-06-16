
from flask import Blueprint, jsonify, redirect, render_template, request, url_for 

from models.Associado import Associado,AssociadoStore
from models.Agendamento import Agendamento,AgendamentoStore

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

@blueprint.route("/associado/agendamentos", methods=['GET', 'POST'])
def associado_agendamentos():

    if request.method == 'POST':
    #if request.form is None:
        
        agendamento = Agendamento(
                data = request.form.get('data'),
                associado_id= 111111111,
                credenciado_id = request.form.get('clinica'),
                especialidade_id = request.form.get('especialidade_id'),
                status=True)
        

        with AgendamentoStore() as agendamento_store:
            agendamento_store.add_agendamento(agendamento)
            agendamento_store.complete()

        return redirect(url_for('associado.associado_agendamentos', cpf=111111111))

    
    associado = Associado(cpf=int(request.args.get('cpf')))
    associado_2 = Associado(cpf=int(request.args.get('cpf')))
    associado_3 = Associado(cpf=int(request.args.get('cpf')))
    

    with AssociadoStore() as associado_store:
        clinicas = associado_store.get_associado_clinica(associado)
        especialidades = associado_store.get_especialidades(associado_2)
        agendamentos = associado_store.get_agendamentos(associado_3)



    context = {
        'clinica': clinicas,
        'especialidade': especialidades,
        'agendamento': agendamentos

    }
    
    #return jsonify(context)
    return render_template("associado_agendamentos.html", context = context)



