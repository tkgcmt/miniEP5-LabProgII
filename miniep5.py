'''
/******************************************************************************/
/* Nome: Christian M. T. Takagi             No. USP: 7136971                  */
/* Disciplina: MAC0242                      Prof.  Alfredo Goldman            */
/* Mini-EP 5                                Arquivo: miniep5.py               */
/******************************************************************************/
'''

import ply.lex as lex
import ply.yacc as yacc

tokens = ('NOME', 'NUM', 'SOM', 'SUB', 'PRO', 'FRA', 'IGU',)

# Tokens
t_SOM    = r'\+'
t_SUB   = r'-'
t_PRO   = r'\*'
t_FRA  = r'/'
t_IGU  = r'='
t_NOME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUM(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor do inteiro (%d) grande demais", t.value)
        t.value = 0
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_QuebraDeLinha(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("O caractere '%s' é invalido" % t.value[0])
    t.lexer.skip(1)

# Constroi o lexer
lex.lex()


# Regras do parser
precedence = (
    ('right','SOM','SUB'),
    ('right','PRO','FRA'),
    ('left','USUB'),
    )

# Dicionario de nomes
nomes = { }

def p_definicao(t):
    'definicao : NOME expressao IGU '
    nomes[t[1]] = t[2]

def p_definicao_expressao(t):
    'definicao : expressao'
    print(t[1])

def p_expressao_operacao_binaria(t):
    '''expressao : expressao expressao SOM 
                  | expressao expressao SUB 
                  | expressao expressao PRO 
                  | expressao expressao FRA ''' 
    if t[3] == '+'  : t[0] = t[1] + t[2]
    elif t[3] == '-': t[0] = t[1] - t[2]
    elif t[3] == '*': t[0] = t[1] * t[2]
    elif t[3] == '/': t[0] = t[1] / t[2]

def p_expressao_usub(t):
    'expressao : SUB expressao %prec USUB'
    t[0] = -t[2]

def p_expressao_num(t):
    'expressao : NUM'
    t[0] = t[1]

def p_nome_da_expressao(t):
    'expressao : NOME'
    try:
        t[0] = nomes[t[1]]
    except LookupError:
        print("Nome '%s' nao definido." % t[1])
        t[0] = 0

def p_error(t):
    print("Erro de sintaxe em  '%s'" % t.value)

yacc.yacc()

while 1:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    yacc.parse(s)
