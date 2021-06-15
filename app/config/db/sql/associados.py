

select_all_associados = """
    SELECT * FROM associados

"""


insert_into_associados = """
    INSERT INTO ASSOCIADOS (cpf, nome, data_nasc, status, plano_id)
    VALUES (?,?,?,?,?)
"""

select_associado_com_plano = """
    SELECT a.cpf, a.nome, a.data_nasc, a.status, p.nome
    FROM associados as a
    INNER JOIN planos as p ON a.plano_id=p.id
    WHERE a.cpf = %d

"""
