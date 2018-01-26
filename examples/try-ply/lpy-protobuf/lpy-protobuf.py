
import ply.lex as lex
import ply.yacc as yacc
import codecs
import sys
import logging as log

log.basicConfig(level=log.DEBUG)

# tokens
keywords = {
    'message': 'KW_MESSAGE', 
    'syntax': 'KW_SYNTAX', 
    'option': 'KW_OPTION', 
    'package': 'KW_PACKAGE', 
    'repeated': 'KW_REPEATED',
    'enum': 'KW_ENUM',
    'import': 'KW_IMPORT',
    }

tokens = [
    'L_BRACE',
    'R_BRACE',
    'EQUAL',
    'SEMICOLON',
    'QUOTATION',
    'D_QUATION',
    'NUMBER',
    'BOOL',
    'STRING',
    'ID',
    'COMMENT'
    ] + list(keywords.values())

# regular express rules for tokens

t_L_BRACE = r'{'
t_R_BRACE = r'}'
t_EQUAL = r'='
t_SEMICOLON = r';'
t_QUOTATION = r'\''
t_D_QUATION = r'\"'

def t_STRING(t):
    r'([\"][^\"]*[\"])|[\'][^\']*[\']'
    return t

def t_BOOL(t):
    r'(true)|(false)'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    ret_type = keywords.get(t.value, t.type)
    t.type = ret_type
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t|\r'
t_ignore_COMMENT = r"//.*"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

'''
expr                    : simple_keyword_expr
                        | enum_keyword_expr
                        | message_keyword_expr


simple_keyword_expr     : KW_SYNTAX EQUAL STRING
                        | KW_OPTION ID EQUAL values
                        | KW_PACKAGE ID
                        | KW_IMPORT STRING

values                  : BOOL
                        | NUMBER
                        | ID

enum_keyword_expr       : KW_ENUM L_BRACE enum_content R_BRACE

enum_content            : ID EQUAL NUMBER SEMICOLON enum_content

'''

if __name__ == "__main__":
    lexer = lex.lex(debug=1)
    files = [
        "F:/git-dir/Utopia/Tools/GenProtobuf/Proto/test.proto",
        #"F:/git-dir/Utopia/Tools/GenProtobuf/Proto/BattleEnum.proto",
        #"F:/git-dir/Utopia/Tools/GenProtobuf/Proto/Battle.proto",
    ]
    for file_path in files:
        print("+++++++++++{0}".format(file_path))
        with codecs.open(file_path, 'r', 'utf-8') as f:
            file_content = f.read()
            lexer.input(file_content)
            while True:
                tok = lexer.token()
                if not tok : break
                print(tok)
        print("---------------------------------------------")
