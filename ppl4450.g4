grammar ppl4450;
program: (operation (NL?))+;
operation: (assignment | expression | if);
assignment
    : ID EQU (ID|expression)
    | ID EQU_P (ID|expression)
    | ID EQU_MI (ID|expression)
    | ID EQU_MU (ID|expression)
    | ID EQU_D (ID|expression)
    ;
expression
    :STR
    |BOOL
    |INT
    |FLO
    |ID
    |array
    |arithmetic
    |comparison
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

if: IF ((expression) | (PAR_O expression PAR_C)) COL NL (operation NL?)+ (ELIF ((expression) | (PAR_O expression PAR_C)) COL NL (operation NL?)+)* (ELSE COL NL (operation NL?)+)?;




PLU	: '+';
MIN	: '-';
MUL	: '*';
DIV	: '/';
MOD 	: '%';
IF	: 'if';
ELIF	: 'elif';
ELSE	: 'else';
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
BRA_O	: '[';
BRA_C	: ']';
PAR_O   : '(';
PAR_C   : ')';
COM	: ',';
COL	: ':';
ID 	: [a-zA-Z_][a-zA-Z_0-9]*;
STR 	: '\'' ( ~['] )* '\'' | '"' ( ~["] )* '"';
INT 	: [0-9]+;
FLO	: [+-]? [0-9]+ '.' [0-9]+ | [+-]? '.' [0-9]+;
BOOL	: 'True' | 'False';
INDT    : '\t';
OUTDT   : '\b';
NL      : [\r\n]+;
WS  	: [ \t]+ -> skip;
