
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
expr                    : simple_keyword_expr  expr
                        | enum_keyword_expr expr
                        | message_keyword_expr expr
                        | empty

simple_keyword_expr     : KW_SYNTAX EQUAL STRING
                        | KW_OPTION ID EQUAL values
                        | KW_PACKAGE ID
                        | KW_IMPORT STRING

values                  : BOOL
                        | NUMBER
                        | ID

enum_keyword_expr       : KW_ENUM L_BRACE enum_content R_BRACE

enum_content            : ID EQUAL NUMBER SEMICOLON enum_content
                        | empty

message_keyword_expr    : KW_MESSAGE ID L_BRACE message_content R_BRACE
                        | empty

message_content         : ID ID EQUAL NUMBER SEMICOLON message_content
                        | KW_REPEATED ID ID EQUAL NUMBER SEMICOLON message_content
                        | message_keyword_expr
                        | empty


'''

simple_keyword_map = {}
KW_STR_SYNTAX = 'syntax'
KW_STR_OPTION = 'option'

#define yacc rule

def p_expr_empty(p):
    'expr :'

# rule for expr
def p_expr_simple_keyword(p):
    'expr : expr simple_keyword_expr'
    p[0] = p[1]

def p_expr_enum_keyword(p):
    'expr : expr enum_keyword_expr'

def p_expr_message_keyword(p):
    'expr : expr message_keyword_expr'

# rule for simple_keyword
def p_simple_keyword_expr_syntax(p):
    'simple_keyword_expr : KW_SYNTAX EQUAL STRING SEMICOLON'
    simple_keyword_map[KW_STR_SYNTAX] = p[3]

def p_simple_keyword_expr_option(p):
    'simple_keyword_expr : KW_OPTION ID EQUAL values SEMICOLON'
    simple_keyword_map[KW_STR_OPTION] = p[4]

def p_simple_keyword_expr_package(p):
    'simple_keyword_expr : KW_PACKAGE ID SEMICOLON'

def p_simple_keyword_expr_import(p):
    'simple_keyword_expr : KW_IMPORT STRING SEMICOLON'

# rule for values
def p_values_bool(p):
    'values : BOOL'

def p_values_number(p):
    'values : NUMBER'

def p_values_string(p):
    'values : STRING'

# rule for enum_keyword_expr
def p_enum_keyword_expr(p):
    'enum_keyword_expr : KW_ENUM ID L_BRACE enum_content R_BRACE'

def p_enum_content_normal(p):
    'enum_content : enum_content ID EQUAL NUMBER SEMICOLON'

def p_enum_content_empty(p):
    'enum_content :'

#rule for message_keyword_expr
def p_message_keyword_expr(p):
    'message_keyword_expr : KW_MESSAGE ID L_BRACE message_content R_BRACE'

def p_message_content_normal(p):
    'message_content : message_content ID ID EQUAL NUMBER SEMICOLON'

def p_message_content_repeated(p):
    'message_content : message_content KW_REPEATED ID ID EQUAL NUMBER SEMICOLON'

def p_message_content_empty(p):
    'message_content :'

def p_message_content_nested(p):
    'message_content : message_content message_keyword_expr'

if __name__ == "__main__":
    lexer = lex.lex(debug=1)
    parser = yacc.yacc(debug=True)
    files = [
        "F:/git-dir/Utopia/Tools/GenProtobuf/Proto/try.proto",
        "F:/git-dir/Utopia/Tools/GenProtobuf/Proto/test.proto",
        "F:/git-dir/Utopia/Tools/GenProtobuf/Proto/BattleEnum.proto",
        "F:/git-dir/Utopia/Tools/GenProtobuf/Proto/Battle.proto",
    ]
    for file_path in files:
        print("+++++++++++{0}".format(file_path))
        with codecs.open(file_path, 'r', 'utf-8') as f:
            file_content = f.read()
            ret = parser.parse(file_content, debug=False)
            print(ret)
            if False:
                lexer.input(file_content)
                while True:
                    tok = lexer.token()
                    if not tok : break
                    print(tok)
        print("---------------------------------------------")
