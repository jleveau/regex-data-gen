grammar Regex;


class_name: CLASSNAME
;

character_class: LITERAL |
                 class_name |
                 LITERAL '-' LITERAL
                 ;

character_class_list: character_class character_class_list |
                        ;

bracket_expression : '[' character_class_list ']';

literal_expression: bracket_expression |
                    LITERAL |
                    ANY_CHAR |
                    SPECIAL_CHAR;

group : GROUP_OP_L expr GROUP_OP_R;
star  : literal_expression STAR |
        group STAR;

expr:
      expr expr |
      expr OR_OP expr |
      group |
      star |
      literal_expression
      ;

regex : SLASH expr SLASH;

PLUS:   '+';
ANY_CHAR: '.';
STAR:   '*';
QUESTION_MARK : '?';
OR_OP : '|';
GROUP_OP_L: '(';
GROUP_OP_R: ')';
BRACKET_L: '[';
BRACKET_R: ']';
SLASH: '/';
CLASSNAME: '[:digit:]' | '[:lower:]' | '[:upper:]' | '[:alpha:]' | '[:word:]' | '[:blank:]' | '[:space:]' | '[:punct:]';

SPECIAL_CHAR:  '\\' (BRACKET_L | SLASH |'-' | OR_OP | QUESTION_MARK | PLUS | STAR | GROUP_OP_L | GROUP_OP_R |'\'' | BRACKET_R | '\\' | '"' | ANY_CHAR);

LITERAL: '-' | . ;
