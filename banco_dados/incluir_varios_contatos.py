from db import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Janice', '99292-0293'),
    ('Luca', '98492-0291'),
    ('Pedro', '97563-0194'),
    ('Babi', '99292-0292'),
    ('Góes', '99293-0290')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'Foram incluidos {cursor.rowcount} registros')
