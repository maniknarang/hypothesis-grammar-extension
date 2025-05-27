// Generated from converter/tests/Json/ConvertedGrammar.g4 by ANTLR 4.13.2
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
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#json}.
	 * @param ctx the parse tree
	 */
	void enterJson(ConvertedGrammarParser.JsonContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#json}.
	 * @param ctx the parse tree
	 */
	void exitJson(ConvertedGrammarParser.JsonContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#members}.
	 * @param ctx the parse tree
	 */
	void enterMembers(ConvertedGrammarParser.MembersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#members}.
	 * @param ctx the parse tree
	 */
	void exitMembers(ConvertedGrammarParser.MembersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#keyvalue}.
	 * @param ctx the parse tree
	 */
	void enterKeyvalue(ConvertedGrammarParser.KeyvalueContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#keyvalue}.
	 * @param ctx the parse tree
	 */
	void exitKeyvalue(ConvertedGrammarParser.KeyvalueContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#key}.
	 * @param ctx the parse tree
	 */
	void enterKey(ConvertedGrammarParser.KeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#key}.
	 * @param ctx the parse tree
	 */
	void exitKey(ConvertedGrammarParser.KeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(ConvertedGrammarParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(ConvertedGrammarParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(ConvertedGrammarParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(ConvertedGrammarParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#stringlist}.
	 * @param ctx the parse tree
	 */
	void enterStringlist(ConvertedGrammarParser.StringlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#stringlist}.
	 * @param ctx the parse tree
	 */
	void exitStringlist(ConvertedGrammarParser.StringlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#numberlist}.
	 * @param ctx the parse tree
	 */
	void enterNumberlist(ConvertedGrammarParser.NumberlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#numberlist}.
	 * @param ctx the parse tree
	 */
	void exitNumberlist(ConvertedGrammarParser.NumberlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(ConvertedGrammarParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(ConvertedGrammarParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#letters}.
	 * @param ctx the parse tree
	 */
	void enterLetters(ConvertedGrammarParser.LettersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#letters}.
	 * @param ctx the parse tree
	 */
	void exitLetters(ConvertedGrammarParser.LettersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(ConvertedGrammarParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(ConvertedGrammarParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#boolean}.
	 * @param ctx the parse tree
	 */
	void enterBoolean(ConvertedGrammarParser.BooleanContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#boolean}.
	 * @param ctx the parse tree
	 */
	void exitBoolean(ConvertedGrammarParser.BooleanContext ctx);
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
}