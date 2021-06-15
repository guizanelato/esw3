
from config.db.Store import Store
from config.db.sql.credenciados import *

class Credenciado:
    def __init__(self,
            codigo = 1,
            razao_social = 'Clínica ACME',
            endereco = 'Rua Arlindo Cruz Medeiros Esteves, 552',
            ):
        self._id = codigo
        self._razao_social = razao_social
        self._endereco = endereco

    def toTuple(self):
        return tuple(map(lambda x: x, self.__dict__.values())) 
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, _id):
        self._id = _id

    @property
    def razao_social(self):
        return self._razao_social

    @razao_social.setter
    def razao_social(self, razao_social):
        self._razao_social = razao_social

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, data_nasc ):
        self._data_nasc = data_nasc

class CredenciadoStore(Store):
    def add_credenciado(self, credenciado):
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_into_credenciados, credenciado.toTuple())
        except Exception as e:
            print('Erro ao adicionar registro de associado:', e)

            
    def get_credenciados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_all_credenciados)
            result = cursor.fetchall()
        except Exception as e:
            print("Erro ao selecionar registros de associados:", e)
        else:
           return [ 
                {
                    'id': credenciado[0],
                    'razao_social': credenciado[1],
                    'endereco': credenciado[2],

                } for credenciado in result
           ]
    

