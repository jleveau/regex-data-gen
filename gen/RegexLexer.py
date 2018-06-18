# Generated from C:/Users/jleveau/PycharmProjects/regex-data-gen/regex_parser\Regex.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write(";\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\3\2\2\2:\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2")
        buf.write("\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2\2\17\'\3")
        buf.write("\2\2\2\21)\3\2\2\2\23+\3\2\2\2\25-\3\2\2\2\27/\3\2\2\2")
        buf.write("\319\3\2\2\2\33\34\7/\2\2\34\4\3\2\2\2\35\36\7]\2\2\36")
        buf.write("\6\3\2\2\2\37 \7_\2\2 \b\3\2\2\2!\"\7\61\2\2\"\n\3\2\2")
        buf.write("\2#$\7-\2\2$\f\3\2\2\2%&\7,\2\2&\16\3\2\2\2\'(\7A\2\2")
        buf.write("(\20\3\2\2\2)*\7~\2\2*\22\3\2\2\2+,\7*\2\2,\24\3\2\2\2")
        buf.write("-.\7+\2\2.\26\3\2\2\2/\60\7]\2\2\60\61\7<\2\2\61\62\7")
        buf.write("f\2\2\62\63\7k\2\2\63\64\7i\2\2\64\65\7k\2\2\65\66\7v")
        buf.write("\2\2\66\67\7<\2\2\678\7_\2\28\30\3\2\2\29:\13\2\2\2:\32")
        buf.write("\3\2\2\2\3\2\2")
        return buf.getvalue()


class RegexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    PLUS = 5
    STAR = 6
    QUESTION_MARK = 7
    OR_OP = 8
    GROUP_OP_L = 9
    GROUP_OP_R = 10
    CLASSNAME = 11
    LITERAL = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'['", "']'", "'/'", "'+'", "'*'", "'?'", "'|'", "'('", 
            "')'", "'[:digit:]'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "STAR", "QUESTION_MARK", "OR_OP", "GROUP_OP_L", "GROUP_OP_R", 
            "CLASSNAME", "LITERAL" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "PLUS", "STAR", "QUESTION_MARK", 
                  "OR_OP", "GROUP_OP_L", "GROUP_OP_R", "CLASSNAME", "LITERAL" ]

    grammarFileName = "Regex.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


