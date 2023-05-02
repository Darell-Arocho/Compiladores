#!/usr/bin/env python3


from ply import yacc
from an_lex import tokens

def formatOutput(p):
    # Loop through each element in the "slice" attribute of the input parameter "p" using a for loop.
    # for i, x in enumerate(p.slice):
        # Print the type of the current element using the "print" function, without printing a new line character.
        # print(x.type, end='')
        # If the current element is not the last element in the "slice" attribute, print the string ' | ' without a new line character.
        # if i < len(p.slice) - 1:
        #     print(' | ', end='')
    # Print a new line character after printing all the types of the elements in the "slice" attribute.
    # print(" | ".join([x.type for x in p.slice]))
    types = [x.type for x in p.slice]
    print(types[0] + " : " + " | ".join(types[1:]))


# Define el axioma / Es una variable interna que YACC ya tiene
start = 's'

def p_s(p):
    '''s : INICIO sentencias FIN'''
    formatOutput(p)

def p_sentencias(p):
    '''sentencias : sentencia FIN_DE_LINEA sentencias
    | sentencia FIN_DE_LINEA'''
    formatOutput(p)

# Token Tipo no es necesario ponerlo en minúscula

def p_sentencia(p):
    '''sentencia : DEFINA IDENTIFICADOR COMO TIPO
    | IDENTIFICADOR ASIG modelo_molecular
    | OPERACION LPAREN IDENTIFICADOR RPAREN'''
    formatOutput(p)

def p_modelo_molecular(p):
    '''modelo_molecular : ELEMENTO_QUIMICO
    | ELEMENTO_QUIMICO VALENCIA
    | elemento grupo_funcional
    | compuesto elemento
    | compuesto elemento grupo_funcional
    | compuesto compuesto compuestos'''
    formatOutput(p)

def p_compuesto(p):
    '''compuesto : ELEMENTO_QUIMICO
    | ELEMENTO_QUIMICO VALENCIA
    | elemento grupo_funcional
    | elemento grupo_funcional ENLACE
    | elemento ENLACE'''
    formatOutput(p)

def p_compuestos(p):
    '''compuestos : compuestos compuesto
    | compuesto'''
    formatOutput(p)

def p_elemento(p):
    '''elemento : ELEMENTO_QUIMICO
    | ELEMENTO_QUIMICO VALENCIA'''


def p_grupo_funcional(p):
    '''grupo_funcional : grupo_funcional_inferior grupo_funcional_superior
    | grupo_funcional_superior grupo_funcional_inferior
    | LPAREN modelo_grupo_funcional RPAREN
    | LBRACK modelo_grupo_funcional RBRACK'''
    formatOutput(p)

def p_grupo_funcional_inferior(p):
    '''grupo_funcional_inferior : LBRACK modelo_grupo_funcional RBRACK'''
    formatOutput(p)

def p_grupo_funcional_superior(p):
    '''grupo_funcional_superior : LPAREN modelo_grupo_funcional RPAREN'''
    formatOutput(p)

def p_modelo_grupo_funcional(p):
    '''modelo_grupo_funcional : ENLACE modelo_molecular
    | ELEMENTO_QUIMICO
    | ELEMENTO_QUIMICO VALENCIA
    | elemento grupo_funcional
    | compuesto elemento
    | compuesto elemento grupo_funcional
    | compuesto compuesto compuestos'''
    formatOutput(p)

def p_error(p):
    if p:
        print(f"Error de sintax en '{p.value}', línea: {p.lineno}, posición: {p.lexpos}, token: {p.type}")
        parser.errok() 
    else:
        print('')

parser = yacc.yacc(debug=True)
