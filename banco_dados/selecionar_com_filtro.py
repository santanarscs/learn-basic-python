from db import nova_conexao

sql = "SELECT * FROM contatos WHERE tel = '98492-0291'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    for x in cursor:
        print(x)
