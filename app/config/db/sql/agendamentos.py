
insert_into_agendamento = """
    INSERT INTO agendamentos (data, credenciado_id, associado_id, especialidade_id, status)
    VALUES (? , ? , ? ,  ? , ?)

"""
