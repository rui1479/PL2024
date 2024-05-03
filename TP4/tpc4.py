import ply.lex as lex

# Definir os tipos de tokens
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'ID',
    'GREATER_EQUAL',
    'NUMBER',
    'COMMA',
)

# Expressões regulares para os tokens
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_GREATER_EQUAL = r'>='
t_COMMA = r','

# Regra para identificar números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Tratar caracteres não reconhecidos
def t_error(t):
    print(f"Caractere não reconhecido: {t.value[0]}")
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()

# Consulta SQL de exemplo
sql_query = "SELECT id, nome, salario FROM empregados WHERE salario >= 820"

# Configurar o analisador léxico para a consulta SQL
lexer.input(sql_query)

# Exibir tokens
while True:
    token = lexer.token()
    if not token:
        break
    print(token)
