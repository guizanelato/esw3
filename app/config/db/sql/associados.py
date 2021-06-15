

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


select_associado_clinica = """
    SELECT c.razao_social, c.endereco
    FROM credenciados as c
    INNER JOIN credenciado_plano as cp on cp.credenciado_id=c.id
    INNER JOIN associados as a on a.plano_id = cp.plano_id
    WHERE a.plano_id = %d

"""
