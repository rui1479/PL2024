# TPC2: Markdown to HTML Converter

Autor: Rui Pedro Ferndandes Ribeiro (a100816)

## Executação
Para a execução do programa, utilize o seguinte comando no terminal:

```bash
    $ python3 tp2.py (nome do ficheiro MD para converter) (nome do ficheiro que vai ser convertido)
```

## Funcionalidades

## Conversão de Cabeçalhos

- O programa converte cabeçalhos do Markdown para HTML. Os cabeçalhos de nível 1, 2 e 3 (#, ##, ###) são transformados em <h1>, <h2> e <h3> respectivamente.

## Conversão de Texto em Negrito

- O programa converte texto em negrito delimitado por ** no Markdown para a tag <b> no HTML.

## Conversão de Texto em Itálico

- O programa converte texto em itálico delimitado por * no Markdown para a tag <i> no HTML.

## Conversão de Links

- O programa converte links do Markdown, que usam a sintaxe [texto](url), para a tag <a href="url">texto</a> no HTML.

## Conversão de Imagens

- O programa converte imagens do Markdown, que usam a sintaxe ![alt](url), para a tag <img src="url" alt="alt"/> no HTML.

## Conversão de Listas Numeradas

- O programa converte listas numeradas do Markdown para listas ordenadas (<ol>) no HTML, com cada item da lista encapsulado em <li>.


## Resultados

Entrada (Markdown):
```
    # Exemplo

    Este é um **exemplo** de conversão de MarkDown para HTML.

    1. Primeiro item
    2. Segundo item
    3. Terceiro item

    Como pode ser consultado em [página da UC](http://www.uc.pt)

    ![imagem dum coelho](http://www.coellho.com)
```

Saída (HTML):
```
    <h1>Exemplo</h1>

    <p>Este é um <b>exemplo</b> de conversão de MarkDown para HTML.</p>

    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>

    <p>Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a></p>

    <img src="http://www.coellho.com" alt="imagem dum coelho"/>
```