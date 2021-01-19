from db import nova_conexao
from mysql.connector import ProgrammingError
excluir_emails = """
  DROP TABLE IF EXISTS emails
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(excluir_emails)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
