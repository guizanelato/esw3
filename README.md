# Projeto de Engenharia de Software III

Repositório destinado ao trabalho final da disciplina ESW3.

## Sobre o Projeto

Este projeto faz parte dos critérios de avaliação da disciplina Engenharia de Software III da FATEC Carapicuíba.

Trata-se de um MVP para um sistema de clínica médica:

```
A AQME administravários consultórios Médicos na GrandeSP, atendendo em diferentes especialidades e aceitando diferentes convênios e seguros médicos (obs: não há atendimento com pagamento direto, fora de convênio). As consultas são marcadas de forma centralizada, permitindo ao paciente escolher o local e o horário convenientemente. Ao comparecer no Consultório opaciente é inicialmente recepcionado pelo corpo de atendentes e técnicos para realização de procedimentos preparatórios e atualização de cadastro e confirmações com o convênio/seguro médico (obs.: Não há atendimento de emergência). Após realização dos procedimentos preparatórios o paciente é conduzido para a consulta médica agendada. O médico deve confirmar os dados de prontuário do paciente, proceder a consulta, atualizar prontuário inclusive com as prescrições de medicamentos e exames. A AQME precisa contabilizar os recebimentos faturados pelos convênios e pagamento aos Médicos que são contratados em regime de PJ, recebendo por cada consulta.

```



## Como utilizar 

Tendo em vista que se trata de um MVP, optou-se por utilizar o micro-framework Flask, integrante do ecossistema de pacotes da comunidade Python.

Para simular localmente o sistema, efetue o clone deste repositório:

```
>$ git clone https://github.com/guizanelato/esw3.git
>$ cd esw3/app
>$ pip install -r requirements.txt
>$ flask run
```

Depois de executar tais tarefas, acesse em seu navegador no endereço `localhost:5000/`.

Para acessar o sistema utilize as seguintes credenciais:

```yaml
username: guilherme.zanelato@gmail.com
senha: 123qwe123
```

