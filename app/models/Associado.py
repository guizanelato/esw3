
from config.db.Store import Store
from config.db.sql.associados import *
from models.Plano import Plano

class Associado:
    def __init__(self,
            cpf = 111111111,
            nome = 'Fulano da Silva',
            data_nasc = '1988-12-20',
            status = True,
            plano = Plano()
            ):
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc
        self._status = status
        self._plano = plano

    def toTuple(self):
        obj = self.__dict__
        obj['_plano'] = obj['_plano'].__dict__.get('_id')

        return tuple( [ obj[key] for key in obj.keys() if not key.endswith("__") ]) 
    
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def data_nasc(self):
        return self._data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc ):
        self._data_nasc = data_nasc
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status ):
        self._status = status
    
    @property
    def plano(self):
        return self._plano

    @plano.setter
    def data_nasc(self, plano ):
        self._plano = plano

    

class AssociadoStore(Store):
    def add_associado(self, associado):
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_into_associados, associado.toTuple())
        except Exception as e:
            print('Erro ao adicionar registro de associado:', e)

            
    def get_associados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_all_associados)
            result = cursor.fetchall()
        except Exception as e:
            print("Erro ao selecionar registros de associados:", e)
        else:
           return [ 
                {
                    'cpf': associado[0],
                    'nome': associado[1],
                    'data_nasc': associado[2],
                    'status': associado[3],
                    'plano_id': associado[4]

                } for associado in result
           ]

    def get_associado_plano(self, associado):
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_associado_com_plano % associado.toTuple()[0])
            result = cursor.fetchone()
        except Exception as e:
            print("Erro ao selecionar registros de associados:", e)
        else:
            return {
                    'cpf': result[0],
                    'nome': result[1],
                    'data_nasc': result[2],
                    'status': 'Ativo' if result[3] == 1 else 'Inativo',
                    'plano': result[4]
            } 

    def get_associado_clinica(self, associado):
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_associado_clinica % int(associado.toTuple()[-1]))
            result = cursor.fetchone()
        except Exception as e:
            print("Erro ao selecionar registros de associados:", e)
        else:
            return {
                    'razao_social': result[0],
                    'endereco': result[1]
            } 
