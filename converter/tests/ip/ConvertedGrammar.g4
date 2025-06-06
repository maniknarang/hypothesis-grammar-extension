grammar ConvertedGrammar;

// Start rule
prog : ip EOF ;

// Parser rules
ip 
    : ipv4 
    | ipv6 
    ;

ipv4 
    : octet '.' octet '.' octet '.' octet 
    ;

octet 
    : '0' 
    | digitnozero 
    | digitnozero digit1 
    | '1' digit1 digit1 
    | '2' digit2 digit1 
    | '2' '5' digit3 
    ;

digit1 
    : '0' 
    | '1' 
    | '2' 
    | '3' 
    | '4' 
    | '5' 
    | '6' 
    | '7' 
    | '8' 
    | '9' 
    ;

digit2 
    : '0' 
    | '1' 
    | '2' 
    | '3' 
    | '4' 
    ;

digit3 
    : '0' 
    | '1' 
    | '2' 
    | '3' 
    | '4' 
    | '5' 
    ;

digitnozero 
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

ipv6 
    : hextet ':' hextet ':' hextet ':' hextet ':' hextet ':' hextet ':' hextet ':' hextet 
    ;

hextet 
    : h1 
    | h2 
    | h3 
    | h4 
    ;

h1 
    : hex 
    ;

h2 
    : hex hex 
    ;

h3 
    : hex hex hex 
    ;

h4 
    : hex hex hex hex 
    ;

hex 
    : digit1 
    | letter 
    ;

letter 
    : 'a' 
    | 'b' 
    | 'c' 
    | 'd' 
    | 'e' 
    | 'f' 
    ;

// Lexer rules
WS : [ \t\r\n]+ -> skip ;