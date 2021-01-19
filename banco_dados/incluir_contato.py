from db import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Raphael', '99292-0293')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'1 registro incluido: {cursor.lastrowid}')
