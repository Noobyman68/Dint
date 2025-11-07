import sys
import re

print(len(sys.argv))
print(sys.argv[0])
# print(sys.argv[1])
if len(sys.argv) < 2:
    print("Please provide file as command line argument")
    sys.exit()
if len(sys.argv) > 2:
    print("Please only provide one command line argument")
    sys.exit()




class lex:
    line: str = ""
    cur_pos: int = 0
    next_pos: int = 0
    ch: str= ''
    def reset(self, line: str):
        self.line = line
        self.cur_pos = 0
        self.next_pos = 0
        self.ch = peek_char(self)


class token:
    def __init__(self, T_type, T_literal, T_start, T_end):
        self.T_type = T_type
        self.T_literal = T_literal
        self.T_start = T_start
        self.T_end = T_end
        


def read_char(cur_data: lex) -> None:
    if cur_data.next_pos >= len(cur_data.line):
        cur_data.ch = '\0'
    else:
        cur_data.ch = cur_data.line[cur_data.next_pos]
    cur_data.cur_pos = cur_data.next_pos
    cur_data.next_pos += 1

def peek_char(cur_data: lex) -> str:
    if cur_data.next_pos >= len(cur_data.line):
        return '\0'
    else:
        return cur_data.line[cur_data.next_pos]

def get_word(cur_data: lex) -> str:
    delimiters = {"=", "/", ".", ">", "<", "-", "%", "\"", ",", "*", "!", "+", "{", "}", "(", ")", "[", "]", ";"}
    if cur_data.ch in delimiters:
        word = cur_data.ch
        read_char(cur_data)
        return word

    word = ""
    while cur_data.ch not in ["\0", "\t", " ", "\n"] and cur_data.ch not in delimiters:
        word += cur_data.ch
        read_char(cur_data)
    return word





def get_token(cur_data: lex) -> token:
    start = cur_data.cur_pos
    word = get_word(cur_data)
    end = cur_data.cur_pos

    match word:
        case "&&":
            tok = token("T_AND", word, start +1, end)
        case "=":
            tok = token("T_ASSIGN", word, start +1, end)
        case "bool":
            tok = token("T_BOOLTYPE", word, start +1, end)
        case "break":
            tok = token("T_BREAK", word, start +1, end)
        case "char_lit":
            tok = token("T_CHARCONSTANT", word, start +1, end)
        case ",":
            tok = token("T_COMMA", word, start +1, end)
        case "\"":
            word = f"\"{get_word(cur_data)}\""
            tok = token(f"T_STRINGCONSTANT (value= {word})", word, start +1, end)
        case "comment":
            tok = token("T_COMMENT", word, start +1, end)
        case "continue":
            tok = token("T_CONTINUE", word, start +1, end)
        case "/":
            tok = token("T_DIV", word, start +1, end)
        case ".":
            tok = token("T_DOT", word, start +1, end)
        case "else":
            tok = token("T_ELSE", word, start +1, end)
        case "==":
            tok = token("T_EQ", word, start +1, end)
        case "extern":
            tok = token("T_EXTERN", word, start +1, end)
        case "false":
            tok = token("T_FALSE", word, start +1, end)
        case "for":
            tok = token("T_FOR", word, start +1, end)
        case "func":
            tok = token("T_FUNC", word, start +1, end)
        case ">=":
            tok = token("T_GEQ", word, start +1, end)
        case ">":
            tok = token("T_GT", word, start +1, end)
        case "identifier":
            tok = token("T_ID", word, start +1, end)
        case "if":
            tok = token("T_IF", word, start +1, end)
        case "int_lit":
            tok = token("T_INTCONSTANT", word, start +1, end)
        case "int":
            tok = token("T_INTTYPE", word, start +1, end)
        case "{":
            tok = token("T_LCB", word, start +1, end)
        case "<<":
            tok = token("T_LEFTSHIFT", word, start +1, end)
        case "<=":
            tok = token("T_LEQ", word, start +1, end)
        case "(":
            tok = token("T_LPAREN", word, start +1, end)
        case "[":
            tok = token("T_LSB", word, start +1, end)
        case "<":
            tok = token("T_LT", word, start +1, end)
        case "-":
            tok = token("T_MINUS", word, start +1, end)
        case "%":
            tok = token("T_MOD", word, start +1, end)
        case "*":
            tok = token("T_MULT", word, start +1, end)
        case "!=":
            tok = token("T_NEQ", word, start +1, end)
        case "!":
            tok = token("T_NOT", word, start +1, end)
        case "null":
            tok = token("T_NULL", word, start +1, end)
        case "||":
            tok = token("T_OR", word, start +1, end)
        case "package":
            tok = token("T_PACKAGE", word, start +1, end)
        case "+":
            tok = token("T_PLUS", word, start +1, end)
        case "}":
            tok = token("T_RCB", word, start +1, end)
        case "return":
            tok = token("T_RETURN", word, start +1, end)
        case ">>":
            tok = token("T_RIGHTSHIFT", word, start +1, end)
        case ")":
            tok = token("T_RPAREN", word, start +1, end)
        case "]":
            tok = token("T_RSB", word, start +1, end)
        case ";":
            tok = token("T_SEMICOLON", word, start +1, end)
        case "string_lit":
            tok = token("T_STRINGCONSTANT", word, start +1, end)
        case "string":
            tok = token("T_STRINGTYPE", word, start +1, end)
        case "true":
            tok = token("T_TRUE", word, start +1, end)
        case "var":
            tok = token("T_VAR", word, start +1, end)
        case "void":
            tok = token("T_VOID", word, start +1, end)
        case "while":
            tok = token("T_WHILE", word, start +1, end)
        case "whitespace":
            tok = token("T_WHITESPACE", word, start +1, end)
        case "whitespace":
            tok = token("T_WHITESPACE", word, start +1, end)
        case _:
            # Check if word is a valid identifier
            if re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', word):
                tok = token("T_ID", word, start +1, end)
            else:
                tok = token("T_UNKNOWN", word, start +1, end)

    return tok

#tokens can be keywords, identifiers, operators, or literals

        
# token_dict = {
#     "T_AND": "&&",
#     "T_ASSIGN": "=",
#     "T_BOOLTYPE": "bool",
#     "T_BREAK": "break",
#     "T_CHARCONSTANT": "char_lit",
#     "T_COMMA": ",",
#     "T_COMMENT": "comment",
#     "T_CONTINUE": "continue",
#     "T_DIV": "/",
#     "T_DOT": ".",
#     "T_ELSE": "else",
#     "T_EQ": "==",
#     "T_EXTERN": "extern",
#     "T_FALSE": "false",
#     "T_FOR": "for",
#     "T_FUNC": "func",
#     "T_GEQ": ">=",
#     "T_GT": ">",
#     "T_ID": "identifier",
#     "T_IF": "if",
#     "T_INTCONSTANT": "int_lit",
#     "T_INTTYPE": "int",
#     "T_LCB": "{",
#     "T_LEFTSHIFT": "<<",
#     "T_LEQ": "<=",
#     "T_LPAREN": "(",
#     "T_LSB": "[",
#     "T_LT": "<",
#     "T_MINUS": "-",
#     "T_MOD": "%",
#     "T_MULT": "*",
#     "T_NEQ": "!=",
#     "T_NOT": "!",
#     "T_NULL": "null",
#     "T_OR": "||",
#     "T_PACKAGE": "package",
#     "T_PLUS": "+",
#     "T_RCB": "}",
#     "T_RETURN": "return",
#     "T_RIGHTSHIFT": ">>",
#     "T_RPAREN": ")",
#     "T_RSB": "]",
#     "T_SEMICOLON": ";",
#     "T_STRINGCONSTANT": "string_lit",
#     "T_STRINGTYPE": "string",
#     "T_TRUE": "true",
#     "T_VAR": "var",
#     "T_VOID": "void",
#     "T_WHILE": "while",
#     "T_WHITESPACE": "whitespace"
# }


T_list: list[token] = []

line_number = 0
token_start = 0
token_end = 0








lexer = lex()
with open(sys.argv[1], 'r',) as file:
    lines = file.readlines()

    for i, line in enumerate(lines):
        lexer.reset(line)
        read_char(lexer)
        T_list = []
        while(peek_char(lexer) != '\0'):
            if lexer.ch in [' ', '\t', '\n']:
                read_char(lexer)
            else:
                T_list.append(get_token(lexer))
        for tok in T_list:
            print(f"{tok.T_literal}\tline {i} Cols {tok.T_start} - {tok.T_end} is {tok.T_type}")
