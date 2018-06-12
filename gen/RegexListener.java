// Generated from /home/jleveau/PycharmProjects/generateData/parser/Regex.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link RegexParser}.
 */
public interface RegexListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link RegexParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(RegexParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RegexParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(RegexParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RegexParser#regex}.
	 * @param ctx the parse tree
	 */
	void enterRegex(RegexParser.RegexContext ctx);
	/**
	 * Exit a parse tree produced by {@link RegexParser#regex}.
	 * @param ctx the parse tree
	 */
	void exitRegex(RegexParser.RegexContext ctx);
}