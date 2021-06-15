

select_all_associados = """
    SELECT * FROM associados

"""


insert_into_associados = """
    INSERT INTO ASSOCIADOS (cpf, nome, data_nasc, status, plano_id)
    VALUES (?,?,?,?,?)
"""
