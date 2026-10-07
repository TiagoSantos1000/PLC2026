# TPC2: Conversor de MarkDown para HTML

## Resumo

Pequeno conversor de MarkDown para HTML, escrito em Python com expressões regulares (módulo `re`), para os elementos da "Basic Syntax" da Cheat Sheet:

| Elemento | MarkDown | HTML |
|---|---|---|
| Cabeçalhos | `# texto`, `## texto`, `### texto` | `<h1>texto</h1>`, `<h2>…`, `<h3>…` |
| Bold | `**texto**` | `<b>texto</b>` |
| Itálico | `*texto*` | `<i>texto</i>` |
| Lista numerada | `1. item` | `<ol><li>item</li></ol>` |
| Link | `[texto](url)` | `<a href="url">texto</a>` |
| Imagem | `![alt](path)` | `<img src="path" alt="alt"/>` |

## Como funciona

A função `md2html` recebe o texto todo e faz a conversão em duas partes.

**1. Substituições com `re.sub`.** Cada elemento é uma expressão regular que procura o padrão em MarkDown e o troca pelo HTML, guardando o texto de dentro num grupo `( )` que é reutilizado com `\1` e `\2`. A ordem é importante:

- o **bold** é convertido antes do **itálico**, porque `**texto**` contém a sintaxe do itálico;
- a **imagem** é convertida antes do **link**, porque `![alt](path)` contém a sintaxe de um link.

**2. Lista numerada.** Como a lista ocupa várias linhas, o texto é percorrido linha a linha. A variável `dentro_da_lista` guarda se estamos dentro de uma lista: o `<ol>` é aberto no primeiro item e o `</ol>` é fechado na primeira linha que já não seja um item (ou no fim do texto).

## Utilização

```
python3 md2html.py exemplo.md             # escreve o HTML no ecrã
python3 md2html.py exemplo.md > out.html  # guarda o HTML num ficheiro
```

## Ficheiros

- [md2html.py](md2html.py): o conversor
- [exemplo.md](exemplo.md): ficheiro de teste com os exemplos do enunciado
