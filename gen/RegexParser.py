# Generated from C:/Users/jleveau/PycharmProjects/regex-data-gen/regex_parser\Regex.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\34")
        buf.write("\n\3\3\4\3\4\3\4\3\4\5\4\"\n\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\5\6*\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\66\n\b\3\t\3\t\3\t\3\t\5\t<\n\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\tC\n\t\f\t\16\tF\13\t\3\n\3\n\3\n\3\n\3\n\2\3\20\13\2")
        buf.write("\4\6\b\n\f\16\20\22\2\2\2K\2\24\3\2\2\2\4\33\3\2\2\2\6")
        buf.write("!\3\2\2\2\b#\3\2\2\2\n)\3\2\2\2\f+\3\2\2\2\16\65\3\2\2")
        buf.write("\2\20;\3\2\2\2\22G\3\2\2\2\24\25\7\r\2\2\25\3\3\2\2\2")
        buf.write("\26\34\7\16\2\2\27\34\5\2\2\2\30\31\7\16\2\2\31\32\7\3")
        buf.write("\2\2\32\34\7\16\2\2\33\26\3\2\2\2\33\27\3\2\2\2\33\30")
        buf.write("\3\2\2\2\34\5\3\2\2\2\35\36\5\4\3\2\36\37\5\6\4\2\37\"")
        buf.write("\3\2\2\2 \"\3\2\2\2!\35\3\2\2\2! \3\2\2\2\"\7\3\2\2\2")
        buf.write("#$\7\4\2\2$%\5\6\4\2%&\7\5\2\2&\t\3\2\2\2\'*\5\b\5\2(")
        buf.write("*\7\16\2\2)\'\3\2\2\2)(\3\2\2\2*\13\3\2\2\2+,\7\13\2\2")
        buf.write(",-\5\20\t\2-.\7\f\2\2.\r\3\2\2\2/\60\5\n\6\2\60\61\7\b")
        buf.write("\2\2\61\66\3\2\2\2\62\63\5\f\7\2\63\64\7\b\2\2\64\66\3")
        buf.write("\2\2\2\65/\3\2\2\2\65\62\3\2\2\2\66\17\3\2\2\2\678\b\t")
        buf.write("\1\28<\5\f\7\29<\5\16\b\2:<\5\n\6\2;\67\3\2\2\2;9\3\2")
        buf.write("\2\2;:\3\2\2\2<D\3\2\2\2=>\f\7\2\2>C\5\20\t\b?@\f\6\2")
        buf.write("\2@A\7\n\2\2AC\5\20\t\7B=\3\2\2\2B?\3\2\2\2CF\3\2\2\2")
        buf.write("DB\3\2\2\2DE\3\2\2\2E\21\3\2\2\2FD\3\2\2\2GH\7\6\2\2H")
        buf.write("I\5\20\t\2IJ\7\6\2\2J\23\3\2\2\2\t\33!)\65;BD")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'['", "']'", "'/'", "'+'", "'*'", 
                     "'?'", "'|'", "'('", "')'", "'[:digit:]'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PLUS", "STAR", "QUESTION_MARK", "OR_OP", 
                      "GROUP_OP_L", "GROUP_OP_R", "CLASSNAME", "LITERAL" ]

    RULE_class_name = 0
    RULE_character_class = 1
    RULE_character_class_list = 2
    RULE_bracket_expression = 3
    RULE_literal_expression = 4
    RULE_group = 5
    RULE_star = 6
    RULE_expr = 7
    RULE_regex = 8

    ruleNames =  [ "class_name", "character_class", "character_class_list", 
                   "bracket_expression", "literal_expression", "group", 
                   "star", "expr", "regex" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PLUS=5
    STAR=6
    QUESTION_MARK=7
    OR_OP=8
    GROUP_OP_L=9
    GROUP_OP_R=10
    CLASSNAME=11
    LITERAL=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Class_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASSNAME(self):
            return self.getToken(RegexParser.CLASSNAME, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_class_name




    def class_name(self):

        localctx = RegexParser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_class_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(RegexParser.CLASSNAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(RegexParser.LITERAL)
            else:
                return self.getToken(RegexParser.LITERAL, i)

        def class_name(self):
            return self.getTypedRuleContext(RegexParser.Class_nameContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_character_class




    def character_class(self):

        localctx = RegexParser.Character_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_character_class)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(RegexParser.LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.class_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(RegexParser.LITERAL)
                self.state = 23
                self.match(RegexParser.T__0)
                self.state = 24
                self.match(RegexParser.LITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_class_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def character_class(self):
            return self.getTypedRuleContext(RegexParser.Character_classContext,0)


        def character_class_list(self):
            return self.getTypedRuleContext(RegexParser.Character_class_listContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_character_class_list




    def character_class_list(self):

        localctx = RegexParser.Character_class_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_character_class_list)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.CLASSNAME, RegexParser.LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.character_class()
                self.state = 28
                self.character_class_list()
                pass
            elif token in [RegexParser.T__2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bracket_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def character_class_list(self):
            return self.getTypedRuleContext(RegexParser.Character_class_listContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_bracket_expression




    def bracket_expression(self):

        localctx = RegexParser.Bracket_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bracket_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(RegexParser.T__1)
            self.state = 34
            self.character_class_list()
            self.state = 35
            self.match(RegexParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bracket_expression(self):
            return self.getTypedRuleContext(RegexParser.Bracket_expressionContext,0)


        def LITERAL(self):
            return self.getToken(RegexParser.LITERAL, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_literal_expression




    def literal_expression(self):

        localctx = RegexParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal_expression)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.bracket_expression()
                pass
            elif token in [RegexParser.LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(RegexParser.LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP_OP_L(self):
            return self.getToken(RegexParser.GROUP_OP_L, 0)

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def GROUP_OP_R(self):
            return self.getToken(RegexParser.GROUP_OP_R, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_group




    def group(self):

        localctx = RegexParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(RegexParser.GROUP_OP_L)
            self.state = 42
            self.expr(0)
            self.state = 43
            self.match(RegexParser.GROUP_OP_R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_expression(self):
            return self.getTypedRuleContext(RegexParser.Literal_expressionContext,0)


        def STAR(self):
            return self.getToken(RegexParser.STAR, 0)

        def group(self):
            return self.getTypedRuleContext(RegexParser.GroupContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_star




    def star(self):

        localctx = RegexParser.StarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_star)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.T__1, RegexParser.LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.literal_expression()
                self.state = 46
                self.match(RegexParser.STAR)
                pass
            elif token in [RegexParser.GROUP_OP_L]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.group()
                self.state = 49
                self.match(RegexParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(RegexParser.GroupContext,0)


        def star(self):
            return self.getTypedRuleContext(RegexParser.StarContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(RegexParser.Literal_expressionContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegexParser.ExprContext,i)


        def OR_OP(self):
            return self.getToken(RegexParser.OR_OP, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 54
                self.group()
                pass

            elif la_ == 2:
                self.state = 55
                self.star()
                pass

            elif la_ == 3:
                self.state = 56
                self.literal_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = RegexParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 60
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = RegexParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 62
                        self.match(RegexParser.OR_OP)
                        self.state = 63
                        self.expr(5)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RegexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_regex




    def regex(self):

        localctx = RegexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(RegexParser.T__3)
            self.state = 70
            self.expr(0)
            self.state = 71
            self.match(RegexParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




