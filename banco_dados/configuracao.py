from mysql.connector import connect

conexao = connect(
    host='127.0.0.1',
    user='root',
    password='mysql',
)

print(conexao)
