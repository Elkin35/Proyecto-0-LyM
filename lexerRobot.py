import re
import codecs
import os
import sys
import ply.lex as lex

tokens_final = []

# Lista de tokens, en esta lista se deben agragar todos los Tookens que se vayan a utilizar en las funciones
reservadas = ['ROBOT_R','END','IF','THEN','WHILE','DO', 'CALL','CONST',
		'VARS','PROCS','OUT','IN','ELSE', 'REPEATTIMES',
		
		"SOUTH", "O", "NORTH", "WEST", "EAST",
		"REPEAT", "COMMAND", "CONDITION", "PIPE", "DIRECTION", "OBJECT", 
		
		"LEFT", "RIGHT","FRONT", "BACK", "AROUND",
		
		"ASSIGNTO", "GOTO", "MOVE", "TURN", "FACE", "PUT", "PICK",
		"MOVETOTHE", "MOVEINDIR", "JUMPTOTHE", "JUMPINDIR", "NOP",

		"FACING", "CANPUT", "CANPICK", "CANMOVEINDIR", "CANJUMPINDIR",
		"CANMOVETOTHE", "CANJUMPTOTHE", "NOT",

		"CHIPS", "BALLOONS",

		"estcon2"

		]

tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT','COMMA','SEMMICOLOM',
		'DOT','UPDATE', 'COLON','RBRACKET','LBRACKET'
		]

t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'

t_RBRACKET = r'\['
t_LBRACKET = r'\]'
t_PIPE = r'\|'

t_COMMA = r','
t_SEMMICOLOM = r';'
t_COLON = r':'
t_DOT = r'\.'
t_UPDATE = r':='

# Detecta los ID's de las variables (en este se guarda todo lo que no se guarda en la  otras funciones)
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
	return t

# Detecta los saltos de linea
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Detecta los numeros
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Detecta los errores
def t_error(t):
	t.lexer.skip(1)

fp = codecs.open("read.txt","r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

# while True:
# 	tok = analizador.token()
# 	if not tok : break
# 	#tokens_final.append(tok)
# 	print(tok)
