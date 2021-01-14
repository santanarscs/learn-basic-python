#!/usr/bin/python3
def tag_bloco(text, classe='success'):
    return f'<div class="{classe}">{text}</div>'


if __name__ == '__main__':
    assert tag_bloco('Incluído com sucesso') == \
        '<div class="success">Incluído com sucesso</div>'
    assert tag_bloco('Impossivel excluir', 'error') == \
        '<div class="error">Impossivel excluir</div>'
