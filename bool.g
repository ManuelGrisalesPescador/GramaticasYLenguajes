// Manuel Alejandro Grisales Pescador
start: program;

program  : expression;

@expression:
	  parexpression
    | logicalexpression
    | boolexpression
	| conditional
    | switchexpression
	| listexpression
	| functiondef
	| number 
	| variable
	;

parexpression:
  LPAR expression RPAR;

conditional:
	IF expression THEN expression ELSE expression;

variable:
	ID;

logicalexpression:
	expression (LT | GT | LEQ | GEQ | EQ | NEQ) expression
	| expression (OR | AND | NAND | NOR | XOR | XNOR) expression
	| NOT expression
	| TRUE
	| FALSE
	;

boolexpression:
    parexpression
	| expression ADD expression
	| expression MUL expression
	;

switchexpression:
    SWITCH expression (CASE expression THEN expression)+ DEFAULT expression
	;


listexpression:
	LPAR LIST (expression (',' expression)*)* RPAR;

functiondef:  DEF ID LPAR (expression (',' expression)*)* RPAR LCBR expression RCBR;

/**
 * Lexer rules
 *
 * Here we define the tokens identified by the lexer.
 */

// Comments
OPEN_COMMENT :  '/\*';
CLOSE_COMMENT :  '\*/';
COMMENT : OPEN_COMMENT '.*?' CLOSE_COMMENT (%ignore);

// Arithmetic operations
ADD  :  '\+';
SUB  :  '-';
MUL  :  '\*';
DIV  :  '/';
MOD  :  '%';

// Boolean operations
LT  :  '<';
GT  :  '>';
LEQ :  '<=';
GEQ :  '>=';
EQ  :  '==';
NEQ  : '!=';



LPAR : '\(';
RPAR : '\)';
LCBR : '{';
RCBR : '}';

// Integers and identifiers
number: '[0-9]+';
ID: '[a-z]+'
	(%unless
		DEF: 'def';
		IF    : 'if';
        THEN: 'then';
		ELSE  : 'else';
		TRUE  : 'true';
		FALSE : 'false';	
        SWITCH : 'switch';	
        CASE : 'case';	
		DEFAULT : 'default';	
		LIST : 'list';	
		OR  : 'or';
		AND  : 'and';
		NAND  : 'nand';
		NOR  : 'nor';
		XOR  : 'xor';
		XNOR  : 'xnor';
		NOT  : 'not';	
	);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		