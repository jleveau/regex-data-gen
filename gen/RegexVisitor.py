# Generated from C:/Users/jleveau/PycharmProjects/regex-data-gen/regex_parser\Regex.g4 by ANTLR 4.7
from antlr4 import *

from nodes.concat import Concat
from nodes.group import Group
from nodes.literal import Literal
from nodes.star import Star
from nodes.union import Union

if __name__ is not None and "." in __name__:
    from .RegexParser import RegexParser
else:
    from gen.RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    def visitGroup(self, ctx: RegexParser.GroupContext):
        return Group(self.visitExpr(ctx.expr()))

    def visitStar(self, ctx:RegexParser.StarContext):
        if ctx.LITERAL():
            return Star(Literal(ctx.LITERAL().getText()))
        else :
            return Star(self.visitGroup(ctx.group()))

    # Visit a parse tree produced by RegexParser#expr.
    def visitExpr(self, ctx:RegexParser.ExprContext):
        if ctx.star():
            return self.visitStar(ctx.star())

        if ctx.OR_OP():
            return Union(self.visitExpr(ctx.expr()[0]), self.visitExpr(ctx.expr()[1]))

        if ctx.group():
            return self.visitGroup(ctx.group())

        if ctx.LITERAL():
            return Literal(ctx.getText())

        elif ctx.expr().__len__() == 2:
            return Concat(self.visitExpr(ctx.expr()[0]), self.visitExpr(ctx.expr()[1]))

    # Visit a parse tree produced by RegexParser#regex.
    def visitRegex(self, ctx:RegexParser.RegexContext):
        return self.visitExpr(ctx.expr())

del RegexParser