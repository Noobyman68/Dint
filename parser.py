from __future__ import annotations
from scanner.py import token


open_brackets = 0
open_paren = 0


class node:
    def __init__(self, name: str, children: list[node] = [], token: token = None):
        self.name = name
        self.children = children
        self.token = token

def parse_program(self):
        nodes = []
        while self.peek():
            nodes.append(self.parse_statement())
        return node("head", nodes)

    def parse_statement(self):
        token = self.peek()
        match token.T_type:
            case "T_VAR":
                return self.parse_var_decl()
            case "T_ID":
                return self.parse_assignment()
            case "T_RETURN":
                return self.parse_return()
            case _:
                raise SyntaxError(f"Unexpected token {token.T_type} at position {self.pos}")

    def parse_var_decl(self):
        self.expect("T_VAR")
        id_token = self.expect("T_ID")
        self.expect("T_SEMICOLON")
        return node("VarDecl", [node("Identifier", token=id_token)])

    def parse_assignment(self):
        id_token = self.expect("T_ID")
        self.expect("T_ASSIGN")
        expr = self.parse_expression()
        self.expect("T_SEMICOLON")
        return node("Assignment", [node("Identifier", token=id_token), expr])

    def parse_return(self):
        self.expect("T_RETURN")
        expr = self.parse_expression()
        self.expect("T_SEMICOLON")
        return node("Return", [expr])

    def parse_expression(self):
        token = self.peek()
        if token.T_type == "T_INTCONSTANT":
            return node("IntLiteral", token=self.match("T_INTCONSTANT"))
        elif token.T_type == "T_STRINGCONSTANT":
            return node("StringLiteral", token=self.match("T_STRINGCONSTANT"))
        elif token.T_type == "T_ID":
            return node("Identifier", token=self.match("T_ID"))
        else:
            raise SyntaxError(f"Invalid expression at position {self.pos}")

def parse_if(self):
    self.expect("T_IF")
    self.expect("T_LPAREN")
    condition = self.parse_expression()
    self.expect("T_RPAREN")
    self.expect("T_LCB")
    then_block = self.parse_block()
    self.expect("T_RCB")

    else_block = None
    if self.peek() and self.peek().T_type == "T_ELSE":
        self.match("T_ELSE")
        self.expect("T_LCB")
        else_block = self.parse_block()
        self.expect("T_RCB")

    return node("IfStatement", [condition, node("ThenBlock", then_block), node("ElseBlock", else_block if else_block else [])])

def parse_while(self):
    self.expect("T_WHILE")
    self.expect("T_LPAREN")
    condition = self.parse_expression()
    self.expect("T_RPAREN")
    self.expect("T_LCB")
    body = self.parse_block()
    self.expect("T_RCB")
    return node("WhileLoop", [condition, node("Body", body)])


def parse_function(self):
    self.expect("T_FUNC")
    name = self.expect("T_ID")
    self.expect("T_LPAREN")
    self.expect("T_RPAREN")  # No parameters yet
    self.expect("T_LCB")
    body = self.parse_block()
    self.expect("T_RCB")
    return node("FunctionDef", [node("Identifier", token=name), node("Body", body)])

def parse_block(self):
    statements = []
    while self.peek() and self.peek().T_type != "T_RCB":
        statements.append(self.parse_statement())
    return statements

def parse_statement(self):
    token = self.peek()
    if token.T_type == "T_VAR":
        return self.parse_var_decl()
    elif token.T_type == "T_ID":
        return self.parse_assignment()
    elif token.T_type == "T_RETURN":
        return self.parse_return()
    elif token.T_type == "T_IF":
        return self.parse_if()
    elif token.T_type == "T_WHILE":
        return self.parse_while()
    elif token.T_type == "T_FUNC":
        return self.parse_function()
    else:
        raise SyntaxError(f"Unexpected token {token.T_type} at position {self.pos}")

with open("output.txt","r") as file:
    lines = file.readlines()

