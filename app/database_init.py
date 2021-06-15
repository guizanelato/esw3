
from models.Associado import Associado,AssociadoStore
from models.User import User,UserStore
from models.Plano import Plano,PlanoStore
from models.Credenciado import Credenciado,CredenciadoStore


if __name__ == '__main__':
    a = Associado()
    u = User()
    p = Plano()
    c = Credenciado()

    with PlanoStore() as plano_store:
        plano_store.add_plano(p)
        plano_store.complete()

    with AssociadoStore() as associado_store:
        associado_store.add_associado(a)
        associado_store.complete()
    

    with UserStore() as user_store:
        user_store.add_user(u)
        user_store.complete()

    with CredenciadoStore() as credenciado_store:
        credenciado_store.add_credenciado(c)
        credenciado_store.complete()


