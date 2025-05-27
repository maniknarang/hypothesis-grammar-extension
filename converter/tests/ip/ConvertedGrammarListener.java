// Generated from converter/tests/ip/ConvertedGrammar.g4 by ANTLR 4.13.2
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
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#ip}.
	 * @param ctx the parse tree
	 */
	void enterIp(ConvertedGrammarParser.IpContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#ip}.
	 * @param ctx the parse tree
	 */
	void exitIp(ConvertedGrammarParser.IpContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#ipv4}.
	 * @param ctx the parse tree
	 */
	void enterIpv4(ConvertedGrammarParser.Ipv4Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#ipv4}.
	 * @param ctx the parse tree
	 */
	void exitIpv4(ConvertedGrammarParser.Ipv4Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#octet}.
	 * @param ctx the parse tree
	 */
	void enterOctet(ConvertedGrammarParser.OctetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#octet}.
	 * @param ctx the parse tree
	 */
	void exitOctet(ConvertedGrammarParser.OctetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#digit1}.
	 * @param ctx the parse tree
	 */
	void enterDigit1(ConvertedGrammarParser.Digit1Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#digit1}.
	 * @param ctx the parse tree
	 */
	void exitDigit1(ConvertedGrammarParser.Digit1Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#digit2}.
	 * @param ctx the parse tree
	 */
	void enterDigit2(ConvertedGrammarParser.Digit2Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#digit2}.
	 * @param ctx the parse tree
	 */
	void exitDigit2(ConvertedGrammarParser.Digit2Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#digit3}.
	 * @param ctx the parse tree
	 */
	void enterDigit3(ConvertedGrammarParser.Digit3Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#digit3}.
	 * @param ctx the parse tree
	 */
	void exitDigit3(ConvertedGrammarParser.Digit3Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#digitnozero}.
	 * @param ctx the parse tree
	 */
	void enterDigitnozero(ConvertedGrammarParser.DigitnozeroContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#digitnozero}.
	 * @param ctx the parse tree
	 */
	void exitDigitnozero(ConvertedGrammarParser.DigitnozeroContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#ipv6}.
	 * @param ctx the parse tree
	 */
	void enterIpv6(ConvertedGrammarParser.Ipv6Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#ipv6}.
	 * @param ctx the parse tree
	 */
	void exitIpv6(ConvertedGrammarParser.Ipv6Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#hextet}.
	 * @param ctx the parse tree
	 */
	void enterHextet(ConvertedGrammarParser.HextetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#hextet}.
	 * @param ctx the parse tree
	 */
	void exitHextet(ConvertedGrammarParser.HextetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#h1}.
	 * @param ctx the parse tree
	 */
	void enterH1(ConvertedGrammarParser.H1Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#h1}.
	 * @param ctx the parse tree
	 */
	void exitH1(ConvertedGrammarParser.H1Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#h2}.
	 * @param ctx the parse tree
	 */
	void enterH2(ConvertedGrammarParser.H2Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#h2}.
	 * @param ctx the parse tree
	 */
	void exitH2(ConvertedGrammarParser.H2Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#h3}.
	 * @param ctx the parse tree
	 */
	void enterH3(ConvertedGrammarParser.H3Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#h3}.
	 * @param ctx the parse tree
	 */
	void exitH3(ConvertedGrammarParser.H3Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#h4}.
	 * @param ctx the parse tree
	 */
	void enterH4(ConvertedGrammarParser.H4Context ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#h4}.
	 * @param ctx the parse tree
	 */
	void exitH4(ConvertedGrammarParser.H4Context ctx);
	/**
	 * Enter a parse tree produced by {@link ConvertedGrammarParser#hex}.
	 * @param ctx the parse tree
	 */
	void enterHex(ConvertedGrammarParser.HexContext ctx);
	/**
	 * Exit a parse tree produced by {@link ConvertedGrammarParser#hex}.
	 * @param ctx the parse tree
	 */
	void exitHex(ConvertedGrammarParser.HexContext ctx);
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