from antlr4 import *
from gen.RegexLexer import RegexLexer
from gen.RegexParser import RegexParser
from gen.RegexVisitor import RegexVisitor


class Parser:

    def run(self, regex):
        input_stream = InputStream(regex)

        lexer = RegexLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = RegexParser(stream)
        tree = parser.regex()

        visitor = RegexVisitor()
        return visitor.visitRegex(tree)
