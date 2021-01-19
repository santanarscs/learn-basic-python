#!python3
try:
    from mysql import connector
except ModuleNotFoundError:
    print('Mysql conector nao esta instaldo')
else:
    print('Mysql connector instalado e pronto')
