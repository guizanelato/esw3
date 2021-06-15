
from config.db.Store import Store
from config.db.sql.users import *

class User:
    def __init__(self,
            login = 'guilherme.zanelato@gmail.com',
            senha = '123qwe123',
            tipo = 'associado',
            cpf = 111111111
            ):

        self._login = login
        self._senha = senha
        self._tipo = tipo
        self._cpf = cpf

    def toTuple(self):
        return tuple(map(lambda x: x, self.__dict__.values()))

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        if '@' not in login:
            raise ValueError('Informe um e-mail válido')
        self._login = login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        if tipo not in ['associado', 'credenciado']:
            raise ValueError('Tipo informado inválido')
        self._tipo = tipo

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

        
class UserStore(Store):
    def add_user(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_into_users, user.toTuple())
        except Exception as e:
            print('Não foi possível inserir o usuário -', e)
    
    def get_user_by_login(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_user_by_login % user.toTuple()[0])
            result = cursor.fetchone()
        except Exception as e:
            print('Erro ao buscar usuário -', e)

        else:
            if result is not None:
                return [
                    {
                        'login': result[1],
                        'senha': result[2],
                        'tipo': result[3],
                        'cpf': result[4]
                    }
                ]
            return {
                'mensagem': 'usuário ou senha inválidos',
                'error-code': 1
            }

