# Generated from C:/Users/jleveau/PycharmProjects/regex-data-gen/regex_parser\Regex.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\5\4\32\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\2\3\6\6\2\4\6\b\2\2\2*\2\n\3\2\2\2\4\23\3\2")
        buf.write("\2\2\6\31\3\2\2\2\b%\3\2\2\2\n\13\7\b\2\2\13\f\5\6\4\2")
        buf.write("\f\r\7\t\2\2\r\3\3\2\2\2\16\17\7\n\2\2\17\24\7\5\2\2\20")
        buf.write("\21\5\2\2\2\21\22\7\5\2\2\22\24\3\2\2\2\23\16\3\2\2\2")
        buf.write("\23\20\3\2\2\2\24\5\3\2\2\2\25\26\b\4\1\2\26\32\5\2\2")
        buf.write("\2\27\32\5\4\3\2\30\32\7\n\2\2\31\25\3\2\2\2\31\27\3\2")
        buf.write("\2\2\31\30\3\2\2\2\32\"\3\2\2\2\33\34\f\7\2\2\34!\5\6")
        buf.write("\4\b\35\36\f\6\2\2\36\37\7\7\2\2\37!\5\6\4\7 \33\3\2\2")
        buf.write("\2 \35\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3\2")
        buf.write("\2\2$\"\3\2\2\2%&\7\3\2\2&\'\5\6\4\2\'(\7\3\2\2(\t\3\2")
        buf.write("\2\2\6\23\31 \"")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'+'", "'*'", "'?'", "'|'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PLUS", "STAR", "QUESTION_MARK", 
                      "OR_OP", "GROUP_OP_L", "GROUP_OP_R", "LITERAL" ]

    RULE_group = 0
    RULE_star = 1
    RULE_expr = 2
    RULE_regex = 3

    ruleNames =  [ "group", "star", "expr", "regex" ]

    EOF = Token.EOF
    T__0=1
    PLUS=2
    STAR=3
    QUESTION_MARK=4
    OR_OP=5
    GROUP_OP_L=6
    GROUP_OP_R=7
    LITERAL=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



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
        self.enterRule(localctx, 0, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(RegexParser.GROUP_OP_L)
            self.state = 9
            self.expr(0)
            self.state = 10
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

        def LITERAL(self):
            return self.getToken(RegexParser.LITERAL, 0)

        def STAR(self):
            return self.getToken(RegexParser.STAR, 0)

        def group(self):
            return self.getTypedRuleContext(RegexParser.GroupContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_star




    def star(self):

        localctx = RegexParser.StarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_star)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(RegexParser.LITERAL)
                self.state = 13
                self.match(RegexParser.STAR)
                pass
            elif token in [RegexParser.GROUP_OP_L]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.group()
                self.state = 15
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


        def LITERAL(self):
            return self.getToken(RegexParser.LITERAL, 0)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 20
                self.group()
                pass

            elif la_ == 2:
                self.state = 21
                self.star()
                pass

            elif la_ == 3:
                self.state = 22
                self.match(RegexParser.LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = RegexParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 26
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = RegexParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 28
                        self.match(RegexParser.OR_OP)
                        self.state = 29
                        self.expr(5)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(RegexParser.T__0)
            self.state = 36
            self.expr(0)
            self.state = 37
            self.match(RegexParser.T__0)
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
        self._predicates[2] = self.expr_sempred
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
         




