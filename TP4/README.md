# TPC4: Analisador Léxico

Autor: Rui Pedro Ferndandes Ribeiro (a100816)

## Executação
Para executar o programa:

```bash
    $ python3 tpc4.py
```

## Funcionalidades

## Tokens Reconhecidos

    -SELECT: A palavra-chave SELECT.
    -FROM: A palavra-chave FROM.
    -WHERE: A palavra-chave WHERE.
    -ID: Identificadores que começam com uma letra ou sublinhado, seguidos por letras, números ou sublinhados.
    -GREATER_EQUAL: O operador >=.
    -NUMBER: Números inteiros.
    -COMMA: A vírgula ,.

## Regras de Tokenização

    -t_SELECT, t_FROM, t_WHERE, t_ID, t_GREATER_EQUAL, t_COMMA: Expressões regulares que definem os padrões para os tokens.
    -t_NUMBER: Função que converte o valor de string do token para um inteiro.
    -t_ignore: Especifica caracteres a serem ignorados (espaços em branco e tabulações).
    -t_error: Função que trata caracteres não reconhecidos e os ignora