import re
import codecs
import os
import sys
import ply.lex as lex

tokens_final = []

reservadas = ['START','END','IF','THEN','WHILE','DO','CALL','CONST',
		'VARS','PROCS','OUT','IN','ELSE', 'ROBOT_R', "SOUTH", "O", "NORTH", "WEST", "EAST"
		]

tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT','COMMA','SEMMICOLOM',
		'DOT','UPDATE', 'COLON','RBRACKET','LBRACKET'
		]

# reservadas = {
# 	'ROBOT_R':'BEGIN',
# 	'end':'END',
# 	'if':'IF',
# 	'then':'THEN',
# 	'while':'WHILE',
# 	'do':'DO',
# 	'call':'CALL',
# 	'const':'CONST',
# 	'int':'VAR',
# 	'procedure':'PROCEDURE',
# 	'out':'OUT',
# 	'in':'IN',
# 	'else':'ELSE'
# }

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
t_START = r'ROBOT_R'

t_RBRACKET = r'\['
t_LBRACKET = r'\]'

t_COMMA = r','
t_SEMMICOLOM = r';'
t_COLON = r':'
t_DOT = r'\.'
t_UPDATE = r':='

def t_O(t):
	r'\|[Ss][Oo][Uu][Tt][Hh]|[nN][Oo][Rr][Tt][Hh]|[Ww][Ee][Ss][Tt]|[Ee][Aa][Ss][Tt]|[Ss][Oo][Uu][Tt][Hh]'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = "O"
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value


	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	#print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1
	files = []

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

directorio = '/Users/sebas/Documents/Compiladores/pl0/analizador version 1/test/'
archivo = buscarFicheros(directorio)

fp = codecs.open("read.txt","r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

i = 0

while True:
	tok = analizador.token()
	if not tok : break
	tokens_final.append(tok)
	print(tok)



print("\n\n")




