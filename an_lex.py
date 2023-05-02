#!/usr/bin/env python3


import ply.lex as lex
import re
import sys

# Define the tokens
tokens = [
   'LPAREN',
   'RPAREN',
   'LBRACK',
   'RBRACK',
   'TIPO',
   'IDENTIFICADOR',
   'ASIG',
   'FIN_DE_LINEA',
   'OPERACION',
   'VALENCIA',
   'ELEMENTO_QUIMICO',
   'ENLACE',
   'INICIO',
   'FIN',
   'DEFINA',
   'COMO'
]

def t_ASIG(t):
    r':='
    return t

def t_TIPO(t):
    r'modelo'
    return t

# Regular expression rules for simple tokens
# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'

#t_PALABRA_RESERVADA = r'inicio | fin | defina | como'
# t_INICIO = r'inicio'
# t_FIN = r'fin'
# t_DEFINA = r'defina'
# t_COMO = r'como'

t_FIN_DE_LINEA = r';'
t_VALENCIA = r'[0-9]'
t_ELEMENTO_QUIMICO = r'Hs|He|Li|Be|B|Cl|Ne|Na|Mg|Al|Si|Ar|Ca|Sc|Ti|V|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|Rb|Sr|Zr|Nb|Mo|Tc|Ru|Rh|Pd|Ag|Cd|In|Sn|Sb|Te|Xe|Cs|Ba|La|Ce|Pr|Nd|Pm|Sm|Eu|Gd|Tb|Dy|Ho|Er|Tm|Yb|Lu|Hf|Ta|Re|Os|Ir|Pt|Au|Hg|Tl|Pb|Bi|Th|Pa|Np|Pu|Am|Cm|Bk|Cf|Es|Fm|Md|No|Lr|Rf|Db|Sg|Bh|Mt|Ds|Rg|Cn|Nh|Fl|Mc|Lv|Ts|Og|W|H|K|N|O|F|P|S|C|U|I|Y'
t_IDENTIFICADOR = r'[a-zA-Z][a-zA-Z0-9_]*'
t_OPERACION = r'graficar2d | graficar3d | pesomolecular'
t_ENLACE = r'(-|=|:{1,2})'

def t_INICIO(t):
    r'inicio'
    return t

def t_FIN(t):
    r'fin'
    return t

def t_DEFINA(t):
    r'defina'
    return t

def t_COMO(t):
    r'como'
    return t

# def t_IDENTIFICADOR(t):
#     r'[a-zA-Z][a-zA-Z0-9_]*'
#     if re.match(r'inicio|fin|defina|como', t.value):
#         if t.value == 'inicio':
#             t.type = "INICIO"
#         elif t.value == 'fin':
#             t.type = "FIN"
#         elif t.value == 'defina':
#             t.type = "DEFINA"
#         elif t.value == 'como':
#             t.type = "COMO"
#     return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#Read from .txt file
myFile = open(sys.argv[1])

lexer = lex.lex()

for line in myFile:
    try:
        lexer.input(line)

        for token in lexer:
            print(f'Token: {token.type} | Value: {token.value} | Position: {token.lexpos} | Line: {token.lineno}')

    except EOFError:
        break
