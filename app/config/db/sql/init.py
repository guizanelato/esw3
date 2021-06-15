

create_table_especialidades = """
    CREATE TABLE especialidades(
        id integer primary key not null,
        nome text,
        descricao
    );


"""

create_table_planos = """
    CREATE TABLE planos(
        id integer primary key,
        nome text,
        desc text,
        preco real
    );
"""

create_table_credenciados = """
    CREATE TABLE credenciados(
        id integer primary key not null,
        razao_social text,
        endereco text,
        especialidade_id integer,
        FOREIGN KEY(especialidade_id) REFERENCES especialidades(id)
        
    );

"""
create_table_associados = """
    CREATE TABLE associados(
        cpf integer primary key not null,
        nome text,
        data_nasc text,
        status boolean,
        plano_id integer,
        FOREIGN KEY(plano_id) references planos(id)
    );

"""
create_table_users = """
    CREATE TABLE users(
        id integer primary key autoincrement,
        login text,
        senha text,
        tipo text,
        cpf integer,
        FOREIGN KEY(cpf) references associados(cpf)
    

    );

"""


create_table_credenciado_planos = """
    CREATE TABLE credenciado_plano(
        plano_id integer not null,
        credenciado_id integer not null,
        FOREIGN KEY(plano_id) REFERENCES planos(id),
        FOREIGN KEY(credenciado_id) REFERENCES credenciados(id)

    );
"""

create_table_agendamentos = """
    CREATE TABLE agendamentos(
        id integer primary key not null,
        data text,
        credenciado_id integer not null,
        associado_id integer not null,
        especialidade_id integer not null,
        status boolean,
        FOREIGN KEY(credenciado_id) REFERENCES credenciados(id),
        FOREIGN KEY(associado_id) REFERENCES associados(id),
        FOREIGN KEY(especialidade_id) REFERENCES especialidades(id)
    );

"""


create_table_prontuarios = """
    CREATE TABLE prontuarios(
        id integer primary key not null,
        agendamento_id integer,
        associado_id integer,
        peso real,
        altura real,
        temperatura real,
        pressao real,
        anamnese text,
        diagnostico text,
        tratamento text,
        FOREIGN KEY(agendamento_id) REFERENCES agendamentos(id),
        FOREIGN KEY(associado_id) REFERENCES associados(id)

    );

"""

create_table_tratamento_item = """
    CREATE TABLE tratamento_item (
        id integer primary key not null,
        nome text,
        desc text,
        preco text

    );

"""


create_table_tratamentos = """
    CREATE TABLE tratamentos(
        id integer primary key not null,
        prontuario_id integer not null,
        tratamento_item_id not null,
        FOREIGN KEY(prontuario_id) REFERENCES prontuarios(id),
        FOREIGN KEY(tratamento_item_id) REFERENCES tratamentos(id)
    );

"""
