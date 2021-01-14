#!/usr/bin/python3
def tag_bloco(text, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{text}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline bloco', 'info', True))
    print(tag_bloco('inline', inline=True))
