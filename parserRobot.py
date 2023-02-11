import ply.yacc as yacc
import os
import codecs
import re
from lexerRobot import tokens
from sys import stdin
import sys

lista_procs = []
decl_variables = []

# ----------------------Inicio del programa ------------------------------

def p_program(p):
	'''program : block'''
	#print("program")

# ------------------------Estructura del programa---------------------------

def p_block(p):
	'''block : ROBOT_R varDecl procDecl instructions bloque'''
	#print ("block")

def p_block2(p):
	'''block : ROBOT_R procDecl instructions bloque'''
	#print ("block2")

def p_block3(p):
	'''block : ROBOT_R varDecl bloque'''
	#print ("block3")

def p_block4(p):
	'''block : ROBOT_R varDecl procDecl instructions'''
	#print ("block4")

def p_block5(p):
	'''block : ROBOT_R'''
	#print ("block5")

def p_block6(p):
	'''block : ROBOT_R bloque'''
	#print ("block6")

def p_block7(p):
	'''block : ROBOT_R procDecl instructions'''
	#print ("block7")

# ---------------------------------------------------

def p_instruction(p):
	'''instructions : RBRACKET insts LBRACKET'''
	#print ("instruction")

def p_instructionEmpty(p):
	'''instructions : empty'''
	#print ("instructionEmpty")

def p_instruction2(p):
	'''instructions : insts LBRACKET'''
	#print ("instruction2")

def p_instruction3(p):
	'''instructions : RBRACKET insts SEMMICOLOM'''
	#print ("instruction")

def p_varDecl(p):
    '''varDecl : VARS varSeparatelist SEMMICOLOM'''
    #print ("varDecl1")

def p_varDecl2(p):
    '''varDecl : VARS varSeparatelist'''
    #print ("varDecl1")

# ----------------------Lista de declaracion de variables--------------------------------

def p_varSeparateList(p):
	'''varSeparatelist :'''
	#print("varSeparateList")

def p_varSeparateList2(p):
	'''varSeparatelist : ID'''
	decl_variables.append(p[1].upper())
	#print("varSeparateList2")

def p_varSeparateList3(p):
	'''varSeparatelist : varSeparatelist COMMA ID'''
	decl_variables.append(p[3].upper())
	#print("varSeparateList3")

# --------------------------------------------------------------------------------------

def p_varDeclEmpty(p):
    '''varDecl : empty'''
    #print ("varDeclEmpty")

def p_nomSeparateList(p):
    '''nomSeparatelist :'''
    #print ("nomSeparateList")

def p_nomSeparateList2(p):
    '''nomSeparatelist : ID'''
    #print("nomSeparateList2")

def p_nomSeparateList3(p):
    '''nomSeparatelist : nomSeparatelist COMMA ID'''
    #print("nomSeparateList3")

def p_procDecl11 (p):
    '''procDecl : PROCS procDef LBRACKET new'''
    #print ("procDecl1")

def p_new2 (p):
    '''new : procDef LBRACKET'''
    #print ("new2")

def p_new3 (p):
    '''new : LBRACKET'''
    #print ("new3")

def p_procDecl33 (p):
    '''procDecl : procDef'''
    #print ("procDecl3")

def p_procDecl2 (p):
	'''again :'''
	#print("again2")

def p_procDecl5 (p):
	'''again : insts'''
	#print("again5")

def p_procDecl3 (p):
	'''again : again SEMMICOLOM insts'''
	#print("again3")

def p_procDeclEmpty (p):
    '''procDecl : empty'''
    #print ("procDeclEmpty")

def p_procDef2 (p):
	'''procDef : ID RBRACKET param again'''
	lista_procs.append(p[1].upper())																										
	#print ("procDef2", p[1])

def p_condition (p):
    '''condition : NUMBER COMMA location'''
    #print ("condition->location")

def p_condition2 (p):
    '''condition : NUMBER COMMA object'''
    #print ("condition->object")

def p_object (p):
    '''object : CHIPS'''
    #print ("object")

def p_object2 (p):
    '''object : BALLOONS'''
    #print ("ballons")

def p_condition4 (p):
	'''condition : location'''
	#print ("condition->location")

def p_location (p):
	'''location : WEST'''
	#print ("west")

def p_location2 (p):
	'''location : NORTH'''
	#print ("north")

def p_location3 (p):
	'''location : SOUTH'''
	#print ("south")

def p_location4 (p):
	'''location : EAST'''
	#print ("east")

def p_param (p):
	'''param : PIPE nomSeparatelist PIPE'''
	#print ("param")

def p_insts (p):
	'''insts : inst '''
	#print ("instsr")

def p_inst3 (p):
	'''inst : command'''
	#print ("insts3")

def p_commands (p):
	'''command : ASSIGNTO COLON NUMBER COMMA ID'''
	if p[5].upper() not in decl_variables:
		print("La Variable " + p[5] + " no ha sido declarada")
		sys.exit()
	#print("commandA")

# -------------------------goto--------------------------

def p_goto(p):
	'''command : GOTO COLON NUMBER COMMA NUMBER'''
	#print("command")

def p_goto2(p):
	'''command : GOTO COLON ID COMMA NUMBER'''
	if p[3].upper() not in decl_variables:
		print("La Variable " + p[3] + " no ha sido declarada")
		sys.exit()
	#print("command")

def p_goto3(p):
	'''command : GOTO COLON ID COMMA ID'''
	if p[3].upper() not in decl_variables:
		print("La Variable " + p[3] + " no ha sido declarada")
		sys.exit()
	elif p[5].upper() not in decl_variables:
		print("La Variable " + p[5] + " no ha sido declarada")
		sys.exit()
	#print("command")

def p_goto4(p):
	'''command : GOTO COLON NUMBER COMMA ID'''
	if p[5].upper() not in decl_variables:
		print("La Variable " + p[5] + " no ha sido declarada")
		sys.exit()
	#print("command")

# ------------------------------------------------------

def p_move (p):
	'''command : MOVE COLON NUMBER'''
	#print("command")

def p_move2 (p):
	'''command : MOVE COLON ID'''
	#print("command")

def p_direction (p):
	'''direction : LEFT'''
	#print("direction")

def p_direction2 (p):
	'''direction : RIGHT'''
	#print("direction2")

def p_direction3 (p):
	'''direction : AROUND'''
	#print("direction3")

def p_commands4 (p):
	'''command : TURN COLON direction'''
	#print("command")

def p_commands5 (p):
	'''command : FACE COLON location'''
	#print("command")

def p_commands6 (p):
	'''command : PUT COLON object COMMA NUMBER '''	
	#print("command")

def p_commands13 (p):
	'''command : PUT COLON ID COMMA object'''
	#print("command")

def p_commands7 (p):
	'''command : PICK COLON object COMMA NUMBER '''
	#print("command")

def p_commands8 (p):
	'''command : MOVETOTHE COLON NUMBER COMMA direction2'''
	#print("command")

def p_directions (p):
	'''direction2 : FRONT'''
	#print("directions")

def p_directions2 (p):
	'''direction2 : BACK'''
	#print("directions2")

def p_directions3 (p):
	'''direction2 : LEFT'''
	#print("directions3")

def p_directions4 (p):
	'''direction2 : RIGHT'''
	#print("directions4")

def p_commands9 (p):
	'''command : MOVEINDIR COLON condition'''
	#print("commands")

def p_commands10 (p):
	'''command : JUMPTOTHE COLON NUMBER COMMA direction2'''
	#print("commands")

def p_commands11 (p):
	'''command : JUMPINDIR COLON condition'''
	#print("commands")

def p_commands12 (p):
	'''command : NOP COLON'''
	#print("commands")

def p_inst4 (p):
	'''inst : estcon'''
	#print("inst4")

def p_inst5 (p):
	'''inst : ID'''
	lista_procs.append(p[1].upper())
	#print("inst5")

def p_inst6 (p):
	'''inst : ID RBRACKET param estcon'''
	lista_procs.append(p[1].upper())
	#print("inst6")

# ----------------------Bloque de procedimientos--------------------------------

def p_bloqueProcs (p):
	'''bloque : RBRACKET binst LBRACKET'''
	#print("bloqueProcs")

def p_blockInst2 (p):
	'''binst : insts SEMMICOLOM binst'''
	#print("blockInsts2")

def p_blockInst3 (p):
	'''binst : insts'''
	#print("blockInsts3")

def p_blockInst4 (p):
	'''binst : callProc SEMMICOLOM binst'''	
	#print("blockInsts4")

def p_blockInst5 (p):
	'''binst : callProc'''
	#print("blockInsts5")

def p_callProc (p):
	'''callProc : ID COLON NUMBER COMMA NUMBER'''
	if p[1].upper() not in lista_procs:
		print(f"Error: El procedimiento {p[1]} no existe")
		sys.exit()

	#print("callProc")

def p_callProc2 (p):
	'''callProc : ID COLON ID COMMA NUMBER'''
	if p[1].upper() not in lista_procs:
		print(f"Error: El procedimiento {p[1]} no existe")
		sys.exit()

	if p[3].upper() not in decl_variables:
		print("La Variable " + p[3] + " no ha sido declarada")
		sys.exit()

	#print("callProc2")

def p_callProc3 (p):
	'''callProc : ID COLON ID COMMA ID'''
	if p[1] not in lista_procs:
		print(f"Error: El procedimiento {p[1]} no existe")
		sys.exit()

	if p[3].upper() not in decl_variables:
		print("La Variable " + p[3] + " no ha sido declarada")
		sys.exit()
	elif p[5].upper() not in decl_variables:
		print("La Variable " + p[5] + " no ha sido declarada")
		sys.exit()

	#print("callProc3")

def p_callProc4 (p):
	'''callProc : ID COLON NUMBER COMMA ID'''
	if p[1] not in lista_procs:
		print(f"Error: El procedimiento {p[1]} no existe")
		sys.exit()
	
	if p[5].upper() not in decl_variables:
		print("La Variable " + p[5] + " no ha sido declarada")
		sys.exit()

	#print("callProc4")

# ------------------------------------------------------

def p_estcon (p):
	'''estcon : IF COLON conditions THEN COLON RBRACKET command LBRACKET ELSE COLON command'''
	#print("estcon")

def p_estcon2 (p):
	'''estcon : WHILE COLON conditions DO COLON RBRACKET command LBRACKET'''
	#print("estcon2")

def p_conditions (p):
	'''conditions : FACING COLON location'''
	#print("conditions")

def p_conditions2 (p):
	'''conditions : CANPUT COLON condition'''
	#print("conditions")

def p_conditions3 (p):
	'''conditions : CANPICK COLON condition'''
	#print("conditions")

def p_conditions4 (p):
	'''conditions : CANMOVEINDIR COLON condition'''
	#print("conditions")

def p_conditions5 (p):
	'''conditions : CANJUMPINDIR COLON condition'''
	#print("conditions")

def p_conditions6 (p):
	'''conditions : CANMOVETOTHE COLON NUMBER COMMA direction2'''
	#print("conditions")

def p_conditions7 (p):
	'''conditions : CANJUMPTOTHE COLON NUMBER COMMA direction2'''
	#print("conditions")

def p_conditions7 (p):
	'''conditions : NOT COLON conditions'''
	#print("conditions")

def p_repeat (p):
	'''estcon : REPEATTIMES COLON NUMBER'''
	#print("repeat")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print ("\nError de sintaxis en '", p.value, "'")
	print ("Error en la linea "+str(p.lineno)+"\n")
	sys.exit()

fp = codecs.open("read2.txt","r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print("\nAnalisis sintactico finalizado con exito: 0 errores encontrados\n")