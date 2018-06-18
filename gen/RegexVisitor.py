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
        if ctx.literal_expression():
            return Star(self.visitLiteralExpression(ctx.literal_expression()))
        else :
            return Star(self.visitGroup(ctx.group()))

    def visitClassname(self, ctx: RegexParser.Class_nameContext) -> Literal:
        return Literal(ctx.CLASSNAME().getText())

    def visitCharacterClass(self, ctx:RegexParser.Character_classContext) -> Literal:
        if ctx.LITERAL():
            if len(ctx.LITERAL()) > 1:
                return Literal.fromRange(ctx.LITERAL()[0].getText(), ctx.LITERAL()[1].getText())
            else:
                return Literal(ctx.LITERAL()[0].getText())
        if ctx.class_name():
            return self.visitClassname(ctx.class_name())

    def visitCharacterClassList(self, ctx:RegexParser.Character_class_listContext) -> Literal:
        if ctx.character_class():
            literal = self.visitCharacterClass(ctx.character_class())
            literal2 = self.visitCharacterClassList(ctx.character_class_list())
            if literal2:
                literal.alphabet += literal2.alphabet
            return literal

    def visitBracketExpression(self, ctx:RegexParser.Bracket_expressionContext) -> Literal:
        return self.visitCharacterClassList(ctx.character_class_list())

    def visitLiteralExpression(self, ctx:RegexParser.Literal_expressionContext) -> Literal:
        if ctx.LITERAL():
            return Literal(ctx.LITERAL().getText())
        elif ctx.bracket_expression():
            return self.visitBracketExpression(ctx.bracket_expression())

    # Visit a parse tree produced by RegexParser#expr.
    def visitExpr(self, ctx:RegexParser.ExprContext):
        if ctx.star():
            return self.visitStar(ctx.star())

        if ctx.OR_OP():
            return Union(self.visitExpr(ctx.expr()[0]), self.visitExpr(ctx.expr()[1]))

        if ctx.group():
            return self.visitGroup(ctx.group())

        if ctx.literal_expression():
            return self.visitLiteralExpression(ctx.literal_expression())

        elif ctx.expr().__len__() == 2:
            return Concat(self.visitExpr(ctx.expr()[0]), self.visitExpr(ctx.expr()[1]))

    # Visit a parse tree produced by RegexParser#regex.
    def visitRegex(self, ctx:RegexParser.RegexContext):
        return self.visitExpr(ctx.expr())

del RegexParser