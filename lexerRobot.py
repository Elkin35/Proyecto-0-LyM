import re
import codecs
import os
import sys
import ply.lex as lex

tokens_final = []

# Lista de tokens, en esta lista se deben agragar todos los Tookens que se vayan a utilizar en las funciones
reservadas = ['ROBOT_R','END','IF','THEN','WHILE','DO', 'CALL','CONST',
		'VARS','PROCS','OUT','IN','ELSE', 
		
		"SOUTH", "O", "NORTH", "WEST", "EAST",
		"REPEAT", "COMMAND", "CONDITION", "PIPE", "DIRECTION", "OBJECT", 
		
		"LEFT", "RIGHT","FRONT", "BACK", 
		
		"ASSIGNTO", "GOTO", "MOVE", "TURN", "FACE", "PUT", "PICK",
		"MOVETOTHE", "MOVEINDIR", "JUMPTOTHE", "JUMPINDIR", "NOP",

		"FACING", "CANPUT", "CANPICK", "CANMOVEINDIR", "CANJUMPINDIR",
		"CANMOVETOTHE", "CANJUMPTOTHE", "NOT"

		"CHIPS", "BALLOONS",

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
#t_START = r'ROBOT_R'

t_RBRACKET = r'\['
t_LBRACKET = r'\]'
t_PIPE = r'\|'

t_COMMA = r','
t_SEMMICOLOM = r';'
t_COLON = r':'
t_DOT = r'\.'
t_UPDATE = r':='



# # Detecta el inicio del programa (es decir la palabra reservada "ROBOT_R")
# def t_START(t):
# 	r'[Rr][Oo][Bb][Oo][Tt]_[Rr]'
# 	if t.value.upper() in reservadas:
# 		t.value = t.value.upper()
# 		#reservadas.get(t.value,'ID')
# 		t.type = "START"
# 	return t



# # Detecta los puntos cardinales
# def t_O(t):
# 	r'\|[Ss][Oo][Uu][Tt][Hh]|[nN][Oo][Rr][Tt][Hh]|[Ww][Ee][Ss][Tt]|[Ee][Aa][Ss][Tt]|[Ss][Oo][Uu][Tt][Hh]'
# 	if t.value.upper() in reservadas:
# 		t.value = t.value.upper()
# 		#reservadas.get(t.value,'ID')
# 		t.type = "O"
# 	return t

# # Detecta las direcciones
# def t_DIRECTION(t):
# 	r'\|[Ll][Ee][Ff][Tt]|[Rr][Ii][Gg][Hh][Tt]|[Ff][Rr][Oo][Nn][Tt]|[Bb][Aa][Cc][Kk]|[Ll][Ee][Ff][Tt]'
# 	if t.value.upper() in reservadas:
# 		t.value = t.value.upper()
# 		#reservadas.get(t.value,'ID')
# 		t.type = "DIRECTION"
# 	return t

# # Detecta los comandos
# def t_COMMAND(t):
# 	r'\|[Aa][Ss][Ss][Ii][Gg][Nn][Tt][Oo]:|[Gg][Oo][Tt][Oo]:|[Mm][Oo][Vv][Ee]:|[Tt][Uu][Rr][Nn]:|[Ff][Aa][Cc][Ee]:|[Pp][Uu][Tt]:|[Pp][Ii][Cc][Kk]:|[Mm][Oo][Vv][Ee][Tt][Oo][Tt][Hh][Ee]:|[Mm][Oo][Vv][Ee][Ii][Nn][Dd][Ii][Rr]:|[Jj][Uu][Mm][Pp][Tt][Oo][Tt][Hh][Ee]:|[Jj][Uu][Mm][Pp][Ii][Nn][Dd][Ii][Rr]:|[Nn][Oo][Pp]:|[Aa][Ss][Ss][Ii][Gg][Nn][Tt][Oo]:'
# 	if t.value.upper() in reservadas:
# 		t.value = t.value.upper()
# 		#reservadas.get(t.value,'ID')
# 		t.type = "COMMAND"
# 	return t

# # Detecta las condiciones
# def t_CONDITION(t):
# 	r'\|[Ff][Aa][Cc][Ii][Nn][Gg]:|[Cc][Aa][Nn][Pp][Uu][Tt]:|[Cc][Aa][Nn][Pp][Ii][Cc][Kk]:|[Cc][Aa][Nn][Mm][Oo][Vv][Ee][Ii][Nn][Dd][Ii][Rr]:|[Cc][Aa][Nn][Jj][Uu][Mm][Pp][Ii][Nn][Dd][Ii][Rr]:|[Cc][Aa][Nn][Mm][Oo][Vv][Ee][Tt][Oo][Tt][Hh][Ee]:|[Cc][Aa][Nn][Jj][Uu][Mm][Pp][Tt][Oo][Tt][Hh][Ee]:|[Nn][Oo][Tt]:|[Ff][Aa][Cc][Ii][Nn][Gg]:'
# 	if t.value.upper() in reservadas:
# 		t.value = t.value.upper()
# 		#reservadas.get(t.value,'ID')
# 		t.type = "CONDITION"
# 	return t

# # Detecta los objetos (Chips y Balloons)
# def t_OBJECT(t):
# 	r'\|[Cc][Hh][Ii][Pp][Ss]|[Bb][Aa][Ll][Ll][Oo][Oo][Nn][Ss]|[Cc][Hh][Ii][Pp][Ss]'
# 	if t.value.upper() in reservadas:
# 		t.value = t.value.upper()
# 		#reservadas.get(t.value,'ID')
# 		t.type = "OBJECT"
# 	return t



# Detecta los ID's de las variables (en este se guarda todo lo que no se guarda en la  otras funciones)
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value
	return t

# Detecta los saltos de linea
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Detecta los comentarios (El lenguaje de robot no tiene comentarios... para la entrega final se puede borrar)
def t_COMMENT(t):
	r'\#.*'
	pass

# Detecta los numeros
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Detecta los errores
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

while True:
	tok = analizador.token()
	if not tok : break
	#tokens_final.append(tok)
	print(tok)





