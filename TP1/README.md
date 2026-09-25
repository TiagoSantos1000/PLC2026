# TP1

## Exercício
Expressão regular para apanhar strings binárias que não contenham a substring "011".

## Resolução
    1*(0|01)*

## Explicação
Antes do primeiro 0 pode haver qualquer número de 1s (`1*`), porque sem
nenhum 0 anterior não há como formar "011". A partir do primeiro 0, cada 0
só pode ser seguido de no máximo um 1, o que corresponde a `(0|01)*`.

## Testar
    printf '%s\n' 0 001 1101 011 0110 1011 | grep -E '^1*(0|01)*$'
