
from config.db.Store import Store
from config.db.sql.planos import *


class Plano:
    def __init__(self,
            codigo = '99',
            nome = 'ACME Silver',
            desc = 'Plano Intermediário',
            preco = 129.99
            ):

        self._id = codigo
        self._nome = nome
        self._desc = desc
        self._preco = preco

    def toTuple(self):
        return tuple(map(lambda x: x, self.__dict__.values()))

    @property
    def codigo(self):
        return self._id

    @codigo.setter
    def codigo(self, codigo):
        self._id = codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError('Preço Inválido')
        self._preco = preco


class PlanoStore(Store):
    def add_plano(self, plano):
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_into_planos, plano.toTuple())
        except Exception as e:
            print('Erro ao adicionar plano:', e)


    def get_planos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_planos)
            result = cursor.fetchall()
        except Exception as e:
            print("Erro ao buscar planos")
        else:
            return [
                    {
                        'codigo': p[0],
                        'nome': p[1],
                        'desc': p[2],
                        'preco': p[3]
                    } for p in result
            ]


