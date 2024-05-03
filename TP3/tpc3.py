import re

texto = ''' 
Este é apenas 1 texto demonstrativo.
Amanhã, 2023-03-07, tens de ir visitar o teu amigo.
Até agora totalizamos: =
ofF
Agora já não está a somar os números: 1, 2, ...
Ora vamos ver: =
On, ligou-se outra vez, cuidado com o 1, 2, 3 ...
Chegamos ao fim com =
'''

token_specification = [
        ('INT', r'(\+|-)?\d+'),             
        ('ON',  r'(?i:on)'),             
        ('OFF', r'(?i:off)'),
        ('EQ', r'='),
        ('SKIP', r'\s+'),
        ('UNKNOWN', r'.')
    ]

mypattern = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

on = True
total = 0
ptr = 0

while ptr < len(texto):
    m = re.match(mypattern, texto[ptr:])
    token = m.groupdict()
    ptr = ptr + m.end()
    if token['EQ']:
        print('Total = ', total)
    elif token['ON']:
        on = True
    elif token['OFF']:
        on = False
    elif token['INT']:
        if on:
            valor = int(m.group(1))
            total = total + valor
    elif token['SKIP']:
        pass
    elif token['UNKNOWN']:
        pass
        #print(f'ERRO: símbolo desconhecido \"{token['UNKNOWN']}\"')

