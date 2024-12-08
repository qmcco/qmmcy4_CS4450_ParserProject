grammar ppl4450;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from ppl4450Parser import ppl4450Parser
}
@lexer::members{
class antlrDenter(DenterHelper):
	def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
		super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
		self.lexer: ppl4450Lexer = lexer
		
	def pull_token(self):
		return super(ppl4450Lexer, self.lexer).nextToken()
		
denter = None

def nextToken(self):
	if not self.denter:
		self.denter = self.antlrDenter(self, self.NL, ppl4450Parser.INDENT, ppl4450Parser.DEDENT, False)
	return self.denter.next_token()
}

program
	: ( NL | operation )* EOF
	;

operation: (assignment | expression | if_st | while_st | for_st);
assignment
    : ID EQU (ID|expression)
    | ID EQU_P (ID|expression)
    | ID EQU_MI (ID|expression)
    | ID EQU_MU (ID|expression)
    | ID EQU_D (ID|expression)
    ;
expression
    :arithmetic
    |conditional
    |expression (AND|OR) expression
    ;
arithmetic: operator ((PLU|MIN)operator)*;
operator: elem ((MUL|DIV|MOD)elem)*;
elem
    : ID
    | ID BRA_O expression BRA_C
    | array
    | INT
    | FLO
    | STR
    | BOOL
    ; 
array: BRA_O (expression(COM expression)*)? BRA_C;
comparison: conditional ((AND|OR)conditional)*;
conditional: (PAR_O?)(NOT?)arithmetic ((CLT|CGT|CLTE|CGTE|CEQU|CNEQU)arithmetic)*(PAR_C?);

if_st
    	: IF expression COL INDENT (((assignment | expression)+ NL) | operation+ )+ DEDENT
      	( ELIF expression COL INDENT (((assignment | expression)+ NL) | operation+ )+ DEDENT )*
      	( ELSE COL INDENT (((assignment | expression)+ NL) | operation+ )+ DEDENT )?
    	;
    
while_st
	: WH expression COL INDENT (((assignment | expression)+ NL) | operation+ )+ DEDENT
	;

for_st
	: FOR ID IN (ID | range) COL INDENT (((assignment | expression)+ NL) | operation+ )+ DEDENT
	;
	
range: RAN PAR_O ((ID | INT)(COM (ID | INT))?(COM (ID | INT))?) PAR_C;
	



PLU	: '+';
MIN	: '-';
MUL	: '*';
DIV	: '/';
MOD 	: '%';
IF	: 'if';
ELIF	: 'elif';
ELSE	: 'else';
WH	: 'while';
FOR	: 'for';
IN	: 'in';
EQU	: '=';
EQU_P	: '+=';
EQU_MI	: '-=';
EQU_MU	: '*=';
EQU_D	: '/=';
CLT	: '<';
CGT	: '>';
CLTE	: '<=';
CGTE	: '>=';
CEQU	: '==';
CNEQU	: '!=';
AND	: 'and';
OR	: 'or';
NOT	: 'not';
RAN	: 'range';
BRA_O	: '[';
BRA_C	: ']';
PAR_O   : '(';
PAR_C   : ')';
COM	: ',';
COL	: ':';
ID 	: [a-zA-Z_][a-zA-Z_0-9]*;
STR 	: '\'' ( ~['] )* '\'' | '"' ( ~["] )* '"';
INT 	: [+-]? [0-9]+;
FLO	: [+-]? [0-9]+ '.' [0-9]+ | [+-]? '.' [0-9]+;
BOOL	: 'True' | 'False';
INDT    : '\t';
OUTDT   : '\b';
NL      : ('\r'? '\n' '\t'*);
WS  	: [ \t]+ -> skip;
HCOM	: '#' ~[\r\n]* -> skip;
ACOM	: ('\'\'\'' .*? '\'\'\'' ) -> skip;
