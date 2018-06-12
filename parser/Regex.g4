grammar Regex;


expr: expr expr |
      expr OR_OP expr |
      expr STAR |
      expr QUESTION_MARK |
      expr PLUS |
      GROUP_OP_L expr GROUP_OP_R |
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
