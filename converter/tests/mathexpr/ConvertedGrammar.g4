grammar ConvertedGrammar;

// Start rule
prog : expr EOF ;

// Parser rules
expr 
    : expr '/' term 
    | expr '*' term 
    | expr '+' term 
    | expr '-' term 
    | expr '/' term 
    | expr '*' term 
    | expr '+' term 
    | expr '-' term 
    | term 
    ;

term 
    : digit '*' variable 
    | digit 
    ;

variable 
    : letter '**' digit 
    | letter 
    ;

letter 
    : 'x' 
    | 'y' 
    | 'z' 
    ;

digit 
    : '1' 
    | '2' 
    | '3' 
    ;

// Lexer rules
WS : [ \t\r\n]+ -> skip ;