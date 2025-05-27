grammar ConvertedGrammar;

// Start rule
prog : json EOF ;

// Parser rules
json 
    : '{' members '}' 
    ;

members 
    : keyvalue 
    | keyvalue ',' members 
    ;

keyvalue 
    : key ':' value 
    ;

key 
    : string 
    ;

value 
    : array 
    | string 
    | number 
    | boolean 
    | json 
    ;

array 
    : '[' stringlist ']' 
    | '[' numberlist ']' 
    ;

stringlist 
    : string ',' stringlist 
    | string 
    ;

numberlist 
    : number ',' numberlist 
    | number 
    ;

string 
    : '"' letters '"' 
    ;

letters 
    : letter letters 
    | letter letters 
    | letter letters 
    | letter 
    ;

number 
    : digit number
    | digit number 
    | digit number 
    | digit 
    ;

boolean 
    : 'true' 
    | 'false' 
    ;

digit 
    : '1' 
    | '2' 
    | '3' 
    | '4' 
    | '5' 
    | '6' 
    | '7' 
    | '8' 
    | '9' 
    ;

letter 
    : 'a' 
    | 'b' 
    | 'c' 
    | 'd' 
    | 'e' 
    | 'f' 
    | 'g' 
    | 'h' 
    | 'i' 
    | 'j' 
    | 'k' 
    | 'l' 
    | 'm' 
    | 'n' 
    | 'o' 
    | 'p' 
    | 'q' 
    | 'r' 
    | 's' 
    | 't' 
    | 'u' 
    | 'v' 
    | 'w' 
    | 'x' 
    | 'y' 
    | 'z' 
    ;

// Lexer rules
WS : [ \t\r\n]+ -> skip ;