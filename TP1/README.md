
# TPC1: Análise de um dataset

Autor: Rui Pedro Fernandes Ribeiro (a100816)


## Executação
Para a execução do programa, utilize o seguinte comando no terminal:

```bash
    $ cat emd.csv | python3 tpc1.py
```


## Parse CSV
- O programa realiza o parse dos dados de um arquivo CSV, armazenando as informações relevantes em um dicionário. Utiliza-se o redirecionamento do conteúdo do CSV para o stdin.

## Lista ordenada alfabeticamente das modalidades desportivas
- As modalidades desportivas são extraídas e apresentadas em ordem alfabética.

## Percentagens de atletas aptos e inaptos para a prática desportiva
- São calculadas as percentagens de atletas aptos e inaptos com base no campo 'resultado'.

## Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos)
- É criada uma distribuição de atletas por intervalos de 5 anos.
