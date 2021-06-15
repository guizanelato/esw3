

select_planos = """

    SELECT * from planos

"""

insert_into_planos = """

    INSERT INTO planos(id, nome, desc, preco)
    VALUES (?, ?, ?, ?)

"""
