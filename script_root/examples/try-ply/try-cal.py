
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

# regular expresions rule to match Token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# t_ignore means that ignore blank character (pre define?)
t_ignore = ' \t'
# t_newline means that match \n+ (pre define?)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #no return, so that we can discard token \n+

# error handling rule (pre define?)
def t_error(t):
    print("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1) # we just skip one character

lexer = lex.lex(debug=1)

'''
expression : expression + term
           | expression - term
           | term

term       : term * factor
           | term / factor
           | factor

factor     : NUMBER
           | ( expression )
           | - factor
'''

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_uminus(p):
    'factor :  MINUS factor'
    p[0] = -p[2]

# error rule for syntax errors
def p_error(p):
    print("Syntax error in input")

parser = yacc.yacc(debug=1)

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)