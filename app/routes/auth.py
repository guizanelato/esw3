
from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from models.User import User,UserStore

blueprint = Blueprint("auth", __name__)

@blueprint.route("/", methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        u = User(
            login=request.form.get('email'),
            senha=request.form.get('password'),
            tipo='associado'
        )    
    
        with UserStore() as user_store:
            result = user_store.get_user_by_login(u)

        if 'error-code' not in result:
            login = result[0]['login']
            senha = result[0]['senha']
            credenciais = u.login == login and u.senha == senha
            
            if credenciais:
                if u.tipo == 'associado':
                    return  redirect(url_for('associado.associado', cpf=result[0]['cpf']))
                return redirect('/credenciado')
            
            return jsonify({'mensagem:': 'Usuário ou Senha Inválidos', 'error-code': 1})
    
    return render_template("sign_in.html")



