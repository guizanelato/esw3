

insert_into_users = """
    INSERT INTO users (login, senha, tipo)
    VALUES (? , ? , ? )

"""

select_user_by_login = """
    SELECT * from users 
    WHERE login = '%s'

"""

