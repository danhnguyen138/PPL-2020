//Nguyen Quang Cong Danh
// 1610392

grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}



//Parser
program: declare+ EOF ;
declare: vardecls|constants|funcdecls;
vardecls: LET vardecl (CM vardecl)* SM;

vardecl:IDV (COLON types)? (ASSIGN expr)?|arraydecl (COLON types)? (ASSIGN expr)?;

// vardecl1:ID (COLON type)? (ASSIGN literals )?;
// vardecl2: arraydecl (COLON type)? (ASSIGN ARRAYLIT)?;




constants: CONSTANT consdecl(CM consdecl)* SM ;
consdecl: IDC (COLON types)? (ASSIGN expr)|arraydecl (COLON types)? (ASSIGN expr);
arraydecl: IDV LSB (expr3 (CM expr3)*) RSB;
types: NUMBER|STRING|JSON|BOOLEAN;

funcdecls: FUNCTION IDV LP paralist? RP LCB body* RCB ;
paralist: parameter (CM parameter)*;
parameter: IDV | index_oper;
index_oper: IDV LSB RSB|IDV LSB expr3 (CM expr3)* RSB;
body: statement|vardecls|constants;
statement: assign_stmt|if_stmt|for_stmt|while_stmt|break_stmt|continue_stmt|call_stmt|return_stmt;
assign_stmt:lhs ASSIGN expr SM;
lhs: expr|IDV;
if_stmt: ifs elifs* elses?;
ifs: IF LP expr1 RP LCB body* RCB;
elifs:ELIF LP expr1 RP LCB body* RCB;
elses: ELSE LCB body* RCB;
for_stmt: infor| offor;
infor: FOR IDV IN expr LCB body* RCB;
offor: FOR IDV OF expr LCB body* RCB;
while_stmt: WHILE LP expr1 RP LCB body* RCB;
break_stmt: BREAK SM;
continue_stmt: CONTINUE SM;
call_stmt: CALL LP IDV CM LSB list_call? RSB RP SM;
list_call: expr (CM expr)*;
return_stmt: RETURN expr SM;

jsonlit: LCB jsonlist? RCB;
jsonlist: jsonmember (CM jsonmember)*;
jsonmember: IDV COLON expr;
/*literals2: NUMBERLIT|BOOLEANLIT|STRINGLIT|arraylit|jsonlist;*/



arraylit: simple_array|multi_array;
simple_array: LSB literals3 ( CM literals3)* RSB;
multi_array: LSB simple_array(CM simple_array)* RSB| LSB multi_array(CM multi_array) RSB;
literals3: NUMBERLIT | BOOLEANLIT | STRINGLIT|jsonlit ;

expr: expr1 (ADDDOT|EQUALDOT)expr1|expr1;
expr1: expr2 (EQUAL|NOT_EQUAL|LT|GT|LE|GE) expr2|expr2;
expr2: expr2 (ANDAND|OR) expr3|expr3;
expr3: expr3 (ADD|SUB) expr4|expr4;
expr4: expr4( MUL|DIV|MOD) expr5|expr5;
expr5: NOT expr5|expr6;
expr6: SUB expr6| expr7;
expr7: expr7 key_operators |expr7 LSB index_operators RSB | expr8;
key_operators: LCB expr RCB | key_operators LCB expr RCB ;
index_operators: expr3 | expr3 CM index_operators;
expr8: IDV|NUMBERLIT|BOOLEANLIT|STRINGLIT|LP expr RP|call_expr|IDC|arraylit|jsonlit;
call_expr: CALL LP IDV CM LSB list_call? RSB RP;






//Lexer
//Keyword
BOOLEANLIT: TRUE|FALSE;
BREAK:'Break';
WHILE:'While';
LET:'Let';
NUMBER:'Number';
CONSTANT:'Constant';
CONTINUE:'Continue';
FOR:'For';
TRUE:'True';
BOOLEAN:'Boolean';
IF:'If';
OF:'Of';
FALSE:'False';
STRING:'String';
ELIF:'Elif';
IN:'In';
CALL:'Call';
JSON:'JSON';
ELSE:'Else';
FUNCTION:'Function';
RETURN:'Return';
ARRAY:'Array';
//Operators
ADDDOT:'+.';
EQUALDOT:'==.';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
OR: '||';
ANDAND: '&&';
NOT_EQUAL: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
ASSIGN: '=';
//Seperatos
LP: '(' ;
RP: ')' ;
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
SM: ';' ;
CM: ',';
COLON:':';
DOT:'.';
//CMT
BLOCK_CMT: '##' .*? '##' ->skip;

//identifiers
NUMBERLIT: Interger Decimal? Exponent?; //
fragment Interger: [0-9]+;
fragment Decimal: DOT [0-9]*;
fragment Exponent: [eE][-+]?[0-9]+;

IDV:[a-z][0-9a-zA-Z_]*;
IDC:[$][0-9a-zA-Z_]*;
//literals



STRINGLIT: DoubleQuote ( StringChar*) DoubleQuote {
        result = str(self.text)
        self.text = result[1:-1]}
    ;
fragment DoubleQuote: '"';
fragment IllegalString
    : '\\' ~[bfrnt"\\]
    ;
fragment StringChar
    : ~[\b\t\f\r\n"\\]
    | EscapeSequence
    ;
fragment EscapeSequence: '\\' [bfrnt"\\]|'\'' DoubleQuote;
 WS : [ \t\r\n\f\b\\]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: DoubleQuote StringChar* ([\b\t\f\n\r"\\] | EOF){
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    };

ILLEGAL_ESCAPE: DoubleQuote StringChar* IllegalString
    {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    };

ERROR_CHAR: .
    {
        raise ErrorToken(self.text)
    };
UNTERMINATED_COMMENT: '##' .*? WS? ;
// STRINGLIT: '"' (~'\\'|ESC_LIT|~'"')* '"' {self.text=self.text[1:-1]};
// fragment ESC_LIT: '\\' [bfrnt'\\] | '\'''"';



// fragment IllegalString: '\\' ~[bfrnt"\\] ;




// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: . { raise ErrorToken(self.text)};
// UNCLOSE_STRING: '"' (~'\\'|ESC_LIT|~'"')* 
// {
//     unclose_str = str(self.text)
//     raise UncloseString(unclose_str[1:])
// } ;

// ILLEGAL_ESCAPE: '"' (~'\\'|ESC_LIT|~'"')* '\\' ~[bfrnt"\\] '"'
// {
    
//     raise IllegalEscape(self.text[1:])
    
// };

// 