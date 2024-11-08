grammar ppl4450;
program: (assignment | expression)+;
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

PLU	: '+';
MIN	: '-';
MUL	: '*';
DIV	: '/';
MOD : '%';
EQU	: '=';
EQU_P	: '+=';
EQU_MI	: '-=';
EQU_MU	: '*=';
EQU_D	: '/=';
BRA_O	: '[';
BRA_C	: ']';
COM	: ',';
ID 	: [a-zA-Z_][a-zA-Z_0-9]*;
STR 	: '\'' ( ~['] )* '\'' | '"' ( ~["] )* '"';
INT 	: [0-9]+;
FLO	: [+-]? [0-9]+ '.' [0-9]+ | [+-]? '.' [0-9]+;
BOOL	: 'True' | 'False';
WS  	: [ \t\r\n]+ -> skip;

