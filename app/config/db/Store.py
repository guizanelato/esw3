
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Store:
    def __init__(self, database='data/acme.db'):
        try:
            self.conn = sqlite3.connect(database)
            #self.conn.row_factory = dict_factory
            self._complete = False
        except Exception as e:
            self.conn = None
            print("Não foi possível conectar ao banco de dados")
        
    
    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.close()

    def complete(self):
        self._complete = True

    def close(self):
        if self.conn is not None:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                print(e)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    print("Conexão não inciada -", e)


if __name__ == '__main__':
    from sql.init import *
    with Store() as store:
        try:
            print('Initializing database schemas...')
            cursor = store.conn.cursor()
            cursor.execute(create_table_especialidades)
            cursor.execute(create_table_planos)
            cursor.execute(create_table_credenciados)
            cursor.execute(create_table_associados)
            cursor.execute(create_table_credenciado_planos)
            cursor.execute(create_table_agendamentos)
            cursor.execute(create_table_prontuarios)
            cursor.execute(create_table_tratamento_item)
            cursor.execute(create_table_tratamentos)
            cursor.execute(create_table_users)
            store.complete()
        except Exception as e:
            print(e)
        finally:
            print('Tables in database:')
            for result in cursor.execute("select name from sqlite_master where type = 'table';"):
                if not result[0].startswith('sqlite'): print(result[0])




