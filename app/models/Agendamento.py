
from config.db.Store import Store
from config.db.sql.agendamentos import *

class Agendamento:
    def __init__(self,
        data = '2021-15-10',
        associado_id=1,
        credenciado_id = 1,
        especialidade_id=1,
        status=True

        ):

        self._data = data
        self._credenciado_id = credenciado_id
        self._associado_id = associado_id
        self._especialidade_id = especialidade_id
        self._status = status

    def toTuple(self):
        return tuple(map(lambda x: x, self.__dict__.values()))


class AgendamentoStore(Store):
    def add_agendamento(self, agendamento):
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_into_agendamento, agendamento.toTuple())
        except Exception as e:
            print("Erro as adicionar agendamento -", e)




