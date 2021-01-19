from db import nova_conexao
from mysql.connector import ProgrammingError

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('SHOW TABLES')
        for i, table in enumerate(cursor, start=1):
            print(f'Tabela {i}: {table[0]}')
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
