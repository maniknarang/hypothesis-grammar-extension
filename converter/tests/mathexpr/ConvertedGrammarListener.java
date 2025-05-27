// Generated from converter/tests/MathExpr/ConvertedGrammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ConvertedGrammarParser}.
 */
public interface ConvertedGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(ConvertedGrammarParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(ConvertedGrammarParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ConvertedGrammarParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ConvertedGrammarParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(ConvertedGrammarParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(ConvertedGrammarParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(ConvertedGrammarParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(ConvertedGrammarParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#letter}.
	 * @param ctx the parse tree
	 */
	void enterLetter(ConvertedGrammarParser.LetterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#letter}.
	 * @param ctx the parse tree
	 */
	void exitLetter(ConvertedGrammarParser.LetterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#digit}.
	 * @param ctx the parse tree
	 */
	void enterDigit(ConvertedGrammarParser.DigitContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#digit}.
	 * @param ctx the parse tree
	 */
	void exitDigit(ConvertedGrammarParser.DigitContext ctx);
}