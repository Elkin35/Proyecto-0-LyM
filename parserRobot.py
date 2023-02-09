import ply.yacc as yacc
import os
import codecs
import re
from lexerRobot import tokens
from sys import stdin


def p_program(p):
	'''program : block'''
	print("program")

def p_block(p):
	'''block : ROBOT_R varDecl procDecl instruction'''
	print ("block")

def p_instruction(p):
	'''instruction : RBRACKET inst LBRACKET'''
	print ("instruction")

def p_instructionEmpty(p):
	'''instruction : empty'''
	print ("instructionEmpty")

def p_instruction2(p):
	'''instruction : inst LBRACKET'''
	print ("instruction")

def p_instruction3(p):
	'''instruction : RBRACKET inst SEMMICOLOM'''
	print ("instruction")

def p_varDecl(p):
    '''varDecl : VARS nomSeparatelist SEMMICOLOM'''
    print ("varDecl")

def p_varDeclEmpty(p):
    '''varDecl : empty'''
    print ("varDeclEmpty")

def p_nomSeparateList(p):
    '''nomSeparatelist :'''
    print ("nomSeparateList")

def p_nomSeparateList2(p):
    '''nomSeparatelist : ID'''
    print ("nomSeparateList2")

def p_nomSeparateList3(p):
    '''nomSeparatelist : nomSeparatelist COMMA ID'''
    print ("nomSeparateList3")

def p_procDecl (p):
    '''procDecl : PROCS again inst'''
    print ("procDecl")

def p_procDecl2 (p):
	'''again :'''
	print("again2")

def p_procDecl5 (p):
	'''again : procDef'''
	print("again5")

def p_procDecl3 (p):
	'''again : again SEMMICOLOM'''
	print("again3")

def p_procDecl4 (p):
	'''again : SEMMICOLOM again LBRACKET'''
	print("again4")

def p_procDeclEmpty (p):
    '''procDecl : empty'''
    print ("procDeclEmpty")

def p_procDef2 (p):
    '''procDef : ID RBRACKET param insts'''																														
    print ("procDef2")

def p_condition (p):
    '''condition : NUMBER COMMA location'''
    print ("condition->location")

def p_condition2 (p):
    '''condition : NUMBER COMMA object'''
    print ("condition->object")

def p_object (p):
    '''object : CHIPS'''
    print ("object")

def p_object2 (p):
    '''object : BALLOONS'''
    print ("ballons")

def p_condition4 (p):
	'''condition : location'''
	print ("condition->location")

def p_location (p):
	'''location : WEST'''
	print ("west")

def p_location2 (p):
	'''location : NORTH'''
	print ("north")

def p_location3 (p):
	'''location : SOUTH'''
	print ("south")

def p_location4 (p):
	'''location : EAST'''
	print ("east")

def p_param (p):
	'''param : PIPE nomSeparatelist PIPE'''
	print ("param")

def p_insts (p):
	'''insts : inst '''
	print ("instsr")

def p_inst3 (p):
	'''inst : command'''
	print ("insts3")

def p_commands (p):
	'''command : ASSIGNTO COLON NUMBER COMMA ID'''
	print("commandA")

def p_commands2 (p):
	'''command : GOTO COLON NUMBER COMMA NUMBER'''
	print("command")

def p_commands3 (p):
	'''command : MOVE COLON NUMBER'''
	print("command")

def p_direction (p):
	'''direction : LEFT'''
	print("direction")

def p_direction2 (p):
	'''direction : RIGHT'''
	print("direction2")

def p_direction3 (p):
	'''direction : AROUND'''
	print("direction3")

def p_commands4 (p):
	'''command : TURN COLON direction'''
	print("command")

def p_commands5 (p):
	'''command : FACE COLON location'''
	print("command")

def p_commands6 (p):
	'''command : PUT COLON object COMMA NUMBER '''	
	print("command")

def p_commands7 (p):
	'''command : PICK COLON object COMMA NUMBER '''
	print("command")

def p_commands8 (p):
	'''command : MOVETOTHE COLON NUMBER COMMA direction2'''
	print("command")

def p_directions (p):
	'''direction2 : FRONT'''
	print("directions")

def p_directions2 (p):
	'''direction2 : BACK'''
	print("directions2")

def p_directions3 (p):
	'''direction2 : LEFT'''
	print("directions3")

def p_directions4 (p):
	'''direction2 : RIGHT'''
	print("directions4")

def p_commands9 (p):
	'''command : MOVEINDIR COLON condition'''
	print("commands")

def p_commands10 (p):
	'''command : JUMPTOTHE COLON NUMBER COMMA direction2'''
	print("commands")

def p_commands11 (p):
	'''command : JUMPINDIR COLON condition'''
	print("commands")

def p_commands12 (p):
	'''command : NOP COLON'''
	print("commands")

def p_inst4 (p):
	'''inst : estcon'''
	print("inst4")

def p_inst5 (p):
	'''inst : ID'''
	print("inst5")

def p_estcon (p):
	'''estcon : IF COLON conditions THEN COLON RBRACKET command LBRACKET ELSE COLON command'''
	print("estcon")

def p_estcon2 (p):
	'''estcon : WHILE COLON conditions DO COLON RBRACKET command LBRACKET'''
	print("estcon2")

def p_conditions (p):
	'''conditions : FACING COLON location'''
	print("conditions")

def p_conditions2 (p):
	'''conditions : CANPUT COLON condition'''
	print("conditions")

def p_conditions3 (p):
	'''conditions : CANPICK COLON condition'''
	print("conditions")

def p_conditions4 (p):
	'''conditions : CANMOVEINDIR COLON condition'''
	print("conditions")

def p_conditions5 (p):
	'''conditions : CANJUMPINDIR COLON condition'''
	print("conditions")

def p_conditions6 (p):
	'''conditions : CANMOVETOTHE COLON NUMBER COMMA direction2'''
	print("conditions")

def p_conditions7 (p):
	'''conditions : CANJUMPTOTHE COLON NUMBER COMMA direction2'''
	print("conditions")

def p_conditions7 (p):
	'''conditions : NOT COLON conditions'''
	print("conditions")

def p_repeat (p):
	'''estcon : REPEATTIMES COLON NUMBER'''
	print("repeat")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print ("Error de sintaxis "), p
	print ("Error en la linea "+str(p.lineno))

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	# while respuesta == False:
	# 	numArchivo = input('\nNumero del test: ')
	# 	for file in files:
	# 		if file == files[int(numArchivo)-1]:
	# 			respuesta = True
	# 			break

	# print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	# return files[int(numArchivo)-1]

# directorio = '/Users/sebas/Documents/Compiladores/pl0/analizador version 2/test/'
# archivo = buscarFicheros(directorio)
# test = directorio+archivo
fp = codecs.open("read.txt","r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print(result)