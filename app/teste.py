
import sqlite3
from estoult import *

db = SQLiteDatabase(database='acme')


class Associado(db.Schema):
    __tablename__ = 'associados'

    cpf = Field(int)
    nome = Field(str)
    data_de_nascimento = Field(str)
    plano_id = Field(int)




associado = {
        'cpf': 99999999999, 
        'nome': 'Guilherme Zanelato Corrêa',
        'data_de_nascimento': '1988-12-20',
        'plano_id': 1
}


#associado = Associado.insert(associado)

associado = (
    Query(Associado)
    .get()
    .execute()
)



