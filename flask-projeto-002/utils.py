from models import Pessoas


def insere_pessoa():
    pessoa = Pessoas(nome="Felipe", idade="20")
    print(pessoa)
    pessoa.save()


def consulta_pessoa():
    pessoas = Pessoas.query.all()
    for p in pessoas:
        print(f'{p.nome} - {p.idade}')


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Raphael').first()
    pessoa.idade = 34
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Felipe').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoa()
    consulta_pessoa()
    # altera_pessoa()
    # exclui_pessoa()
