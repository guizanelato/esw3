

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
    SELECT c.razao_social, c.endereco, c.id
    FROM credenciados as c
    INNER JOIN credenciado_plano as cp on cp.credenciado_id=c.id
    INNER JOIN associados as a on a.plano_id = cp.plano_id
    WHERE a.plano_id = %d

"""


select_agendamentos = """
    SELECT c.razao_social, a.data, a.status, e.nome
    FROM agendamentos as a
    INNER JOIN credenciados as c on c.id=a.credenciado_id
    INNER JOIN associados as ass on ass.cpf=a.associado_id
    INNER JOIN especialidades as e on e.id=a.especialidade_id
    WHERE ass.cpf = %d

"""

select_especialidades = """
    SELECT e.id, e.nome
    FROM especialidades as e 
    INNER JOIN credenciado_especialidades as ce on ce.especialidade_id=e.id
    INNER JOIN credenciados as cd on cd.id=ce.credenciado_id
    INNER JOIN credenciado_plano as cp on cp.credenciado_id = cd.id
    INNER JOIN associados as a on a.plano_id=cp.plano_id
    WHERE a.cpf = %d

"""


