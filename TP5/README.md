# TPC5: Máquina De Vending

Autor: Rui Pedro Ferndandes Ribeiro (a100816)

## Executação
Para executar o programa:

```bash
    $ python3 vending.py stock.json
```

## Funcionalidades

- LISTAR: Lista todos os produtos disponíveis no estoque.
- DEPOSITAR: Permite ao usuário depositar moedas.
- SELECIONAR: Seleciona um produto para compra.
- SAIR: Encerra a interação com a máquina de vendas.

## Observações

    -O saldo é atualizado com cada depósito e a compra só é realizada se o saldo for suficiente.
    -A aplicação calcula e devolve o troco após uma compra.
    -Caracteres ilegais são tratados e ignorados pelo analisador léxico.