grammar Regex;

group: GROUP_OP_L expr GROUP_OP_R;
star : LITERAL STAR |
       group STAR;
expr:
      expr expr |
      expr OR_OP expr |
      group |
      star |
      LITERAL
      ;

regex : '/' expr '/';

PLUS:   '+';
STAR:   '*';
QUESTION_MARK : '?';
OR_OP : '|';
GROUP_OP_L: '(';
GROUP_OP_R: ')';
LITERAL: . ;
