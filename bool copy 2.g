start: program;

program  : functiondef* expression;

functiondef:  DEF ID LPAR (ID (',' ID)*)*  RPAR LCBR expression RCBR;


@expression:
	  parexpression
    | logicalexpression
    | boolexpression
	| conditional
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
	| TRUE
	| FALSE
	;

boolexpression:
    parexpression
	| expression ADD expression
	| expression MUL expression
	;

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
	);

// Ignore white space, tab and new lines.
WS: '[ \t\r\n]+' (%ignore);		