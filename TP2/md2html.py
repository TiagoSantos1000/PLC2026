import re
import sys


def md2html(texto):
    # Cabeçalhos: "# texto", "## texto", "### texto"
    texto = re.sub(r'^# (.+)$', r'<h1>\1</h1>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^## (.+)$', r'<h2>\1</h2>', texto, flags=re.MULTILINE)
    texto = re.sub(r'^### (.+)$', r'<h3>\1</h3>', texto, flags=re.MULTILINE)

    # Bold: **texto**  (antes do itálico!)
    texto = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', texto)

    # Itálico: *texto*
    texto = re.sub(r'\*(.+?)\*', r'<i>\1</i>', texto)

    # Imagem: ![texto alternativo](path)  (antes do link!)
    texto = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', texto)

    # Link: [texto](url)
    texto = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', texto)

    # Lista numerada: linhas seguidas do tipo "1. texto"
    resultado = []
    dentro_da_lista = False

    for linha in texto.splitlines():
        item = re.match(r'\d+\. (.+)', linha)

        if item:
            if not dentro_da_lista:
                resultado.append('<ol>')
                dentro_da_lista = True
            resultado.append('<li>' + item.group(1) + '</li>')
        else:
            if dentro_da_lista:
                resultado.append('</ol>')
                dentro_da_lista = False
            resultado.append(linha)

    if dentro_da_lista:
        resultado.append('</ol>')

    return '\n'.join(resultado)


# Programa principal: lê o ficheiro indicado e escreve o HTML no ecrã
ficheiro = open(sys.argv[1], encoding='utf-8')
texto = ficheiro.read()
ficheiro.close()

print(md2html(texto))
