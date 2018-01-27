
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
    yacc_parse_error = yacc_parse_error + 1

'''
expr                    : expr simple_keyword_expr 
                        | expr enum_keyword_expr
                        | expr message_keyword_expr
                        | empty

simple_keyword_expr     : KW_SYNTAX EQUAL STRING
                        | KW_OPTION ID EQUAL values
                        | KW_PACKAGE ID
                        | KW_IMPORT STRING

values                  : BOOL
                        | NUMBER
                        | ID

enum_keyword_expr       : KW_ENUM ID L_BRACE enum_content R_BRACE

enum_content            : enum_content enum_field
                        | empty

message_keyword_expr    : KW_MESSAGE ID L_BRACE message_content R_BRACE
                        | empty

message_content         : message_content ID ID EQUAL NUMBER SEMICOLON 
                        | message_content KW_REPEATED ID ID EQUAL NUMBER SEMICOLON 
                        | message_content message_keyword_expr
                        | message_content enum_keyword_expr
                        | empty
'''

#define yacc rule
def p_begin(p):
    'begin : expr'
    p[0] = p[1]

def p_expr_empty(p):
    'expr :'

# rule for expr
def p_expr_simple_keyword(p):
    'expr : expr simple_keyword_expr'
    ret = p[1] or []
    p[0] = ret

def p_expr_enum_keyword(p):
    'expr : expr enum_keyword_expr'
    ret = p[1] or []
    p[2] and ret.append(p[2])
    p[0] = ret

def p_expr_message_keyword(p):
    'expr : expr message_keyword_expr'
    ret = p[1] or []
    p[2] and ret.append(p[2])
    p[0] = ret

# rule for simple_keyword
def p_simple_keyword_expr_syntax(p):
    'simple_keyword_expr : KW_SYNTAX EQUAL STRING SEMICOLON'
    yacc_ret.syntax = p[3]

def p_simple_keyword_expr_option(p):
    'simple_keyword_expr : KW_OPTION ID EQUAL values SEMICOLON'
    yacc_ret.options[p[2]] = p[4]

def p_simple_keyword_expr_package(p):
    'simple_keyword_expr : KW_PACKAGE ID SEMICOLON'
    yacc_ret.package = p[2]

def p_simple_keyword_expr_import(p):
    'simple_keyword_expr : KW_IMPORT STRING SEMICOLON'
    yacc_ret.imports.add(p[2])

# rule for values
def p_values_bool(p):
    'values : BOOL'
    p[0] = p[1]

def p_values_number(p):
    'values : NUMBER'
    p[0] = p[1]

def p_values_string(p):
    'values : STRING'
    p[0] = p[1]

# rule for enum_keyword_expr
def p_enum_keyword_expr(p):
    'enum_keyword_expr : KW_ENUM ID L_BRACE enum_content R_BRACE'
    ret = PbEnum()
    ret.name = p[2]
    ret.fields = p[4] or []
    p[0] = ret

def p_enum_content_normal(p):
    'enum_content : enum_content ID EQUAL NUMBER SEMICOLON'
    ret = p[1] or []
    enum_field = PbEnumField()
    enum_field.name = p[2]
    enum_field.value = p[4]
    ret.append(enum_field)
    p[0] = ret

def p_enum_content_empty(p):
    'enum_content :'

#rule for message_keyword_expr
def p_message_keyword_expr(p):
    'message_keyword_expr : KW_MESSAGE ID L_BRACE message_content R_BRACE'
    ret = PbClass()
    ret.name = p[2]
    msg_content = p[4]
    if msg_content:
        for item in msg_content:
            if not item: continue
            if (isinstance(item, PbNode)):
                ret.children[item.name] = item
                item.parent = ret
            else:
                ret.fields.append(item)
    p[0] = ret


def p_message_content_normal(p):
    'message_content : message_content ID ID EQUAL NUMBER SEMICOLON'
    ret = p[1] or []
    msg_field = PbClassField()
    msg_field.is_array = False
    msg_field.type = p[2]
    msg_field.name = p[3]
    msg_field.filed_id = p[5]
    ret.append(msg_field)
    p[0] = ret

def p_message_content_repeated(p):
    'message_content : message_content KW_REPEATED ID ID EQUAL NUMBER SEMICOLON'
    ret = p[1] or []
    msg_field = PbClassField()
    msg_field.is_array = True
    msg_field.type = p[2]
    msg_field.name = p[3]
    msg_field.filed_id = p[5]
    ret.append(msg_field)
    p[0] = ret

def p_message_content_empty(p):
    'message_content :'

def p_message_content_nested_message(p):
    'message_content : message_content message_keyword_expr'
    ret = p[1] or []
    p[2] and ret.append(p[2])
    p[0] = ret

def p_message_content_nested_enum(p):
    'message_content : message_content enum_keyword_expr'
    ret = p[1] or []
    p[2] and ret.append(p[2])
    p[0] = ret

# error rule for syntax errors
def p_error(p):
    print("Syntax error in input")
    yacc_parse_error = yacc_parse_error + 1

STR_EMPTY = ''

class PbNode(object):
    def __init__(self):
        self.path = STR_EMPTY
        self.name = STR_EMPTY
        self.parent = None
        self.children = {}


class PbClass(PbNode):
    def __init__(self):
        PbNode.__init__(self)
        self.search_packages = []
        self.fields = []

class PbClassField(object):
    def __init__(self):
        self.is_array = False
        self.type = STR_EMPTY
        self.name = STR_EMPTY
        self.filed_id = -1

class PbEnum(PbNode):
    def __init__(self):
        PbNode.__init__(self)
        self.fields = []


class PbEnumField(PbNode):
    def __init__(self):
        PbNode.__init__(self)
        self.name = STR_EMPTY
        self.value = -1


class YaccResult(object):
    def __init__(self):
        self.syntax = STR_EMPTY
        self.package = STR_EMPTY
        self.imports = set()
        self.options = {}
        self.ns = PbNode()

def FindPbNode(pb_node, node_path, is_create):
    if not pb_node:
        return None
    node_names = []
    if node_path:
        node_names = node_path.split('.')
    ret_node = pb_node
    for node_name in node_names:
        if not ret_node: break
        finded_node = ret_node.children.get(node_name, None)
        if is_create and not finded_node:
            finded_node = PbNode()
            finded_node.name = node_name
            finded_node.parent = ret_node
            ret_node.children[finded_node.name] = finded_node
        ret_node = finded_node
    return ret_node

pb_root = None
yacc_ret = None
yacc_parse_error = 0

if __name__ == "__main__":
    pb_root = PbNode()
    lexer = lex.lex(debug=1)
    parser = yacc.yacc(debug=True)
    files = [
        "F:/git-dir/Utopia/Tools/GenProtobuf/Proto/try.proto",
        #"F:/git-dir/Utopia/Tools/GenProtobuf/Proto/test.proto",
        #"F:/git-dir/Utopia/Tools/GenProtobuf/Proto/BattleEnum.proto",
        #"F:/git-dir/Utopia/Tools/GenProtobuf/Proto/Battle.proto",
    ]
    for file_path in files:
        print("+++++++++++{0}".format(file_path))
        with codecs.open(file_path, 'r', 'utf-8') as f:
            yacc_parse_error = 0
            yacc_ret = YaccResult()
            file_content = f.read()
            pb_nodes = parser.parse(file_content, debug=True)
            if yacc_parse_error > 0:
                print("parse file {0} fail ".format(file_path))
                break
            package_node = FindPbNode(pb_root, yacc_ret.package, True)
            for pb_node in pb_nodes:
                package_node.children[pb_node.name] = pb_node
                pb_node.parent = package_node        
        print("---------------------------------------------")
    # at last  we process pb_root tree
    pb_root = None
    yacc_ret = None
    yacc_parse_error = 0
