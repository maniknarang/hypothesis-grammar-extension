// Generated from converter/tests/ip/ConvertedGrammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ConvertedGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, WS=19;
	public static final int
		RULE_prog = 0, RULE_ip = 1, RULE_ipv4 = 2, RULE_octet = 3, RULE_digit1 = 4, 
		RULE_digit2 = 5, RULE_digit3 = 6, RULE_digitnozero = 7, RULE_ipv6 = 8, 
		RULE_hextet = 9, RULE_h1 = 10, RULE_h2 = 11, RULE_h3 = 12, RULE_h4 = 13, 
		RULE_hex = 14, RULE_letter = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "ip", "ipv4", "octet", "digit1", "digit2", "digit3", "digitnozero", 
			"ipv6", "hextet", "h1", "h2", "h3", "h4", "hex", "letter"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'0'", "'1'", "'2'", "'5'", "'3'", "'4'", "'6'", "'7'", 
			"'8'", "'9'", "':'", "'a'", "'b'", "'c'", "'d'", "'e'", "'f'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ConvertedGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ConvertedGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public IpContext ip() {
			return getRuleContext(IpContext.class,0);
		}
		public TerminalNode EOF() { return getToken(ConvertedGrammarParser.EOF, 0); }
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			ip();
			setState(33);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IpContext extends ParserRuleContext {
		public Ipv4Context ipv4() {
			return getRuleContext(Ipv4Context.class,0);
		}
		public Ipv6Context ipv6() {
			return getRuleContext(Ipv6Context.class,0);
		}
		public IpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ip; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterIp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitIp(this);
		}
	}

	public final IpContext ip() throws RecognitionException {
		IpContext _localctx = new IpContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_ip);
		try {
			setState(37);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(35);
				ipv4();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(36);
				ipv6();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Ipv4Context extends ParserRuleContext {
		public List<OctetContext> octet() {
			return getRuleContexts(OctetContext.class);
		}
		public OctetContext octet(int i) {
			return getRuleContext(OctetContext.class,i);
		}
		public Ipv4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ipv4; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterIpv4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitIpv4(this);
		}
	}

	public final Ipv4Context ipv4() throws RecognitionException {
		Ipv4Context _localctx = new Ipv4Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_ipv4);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			octet();
			setState(40);
			match(T__0);
			setState(41);
			octet();
			setState(42);
			match(T__0);
			setState(43);
			octet();
			setState(44);
			match(T__0);
			setState(45);
			octet();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OctetContext extends ParserRuleContext {
		public DigitnozeroContext digitnozero() {
			return getRuleContext(DigitnozeroContext.class,0);
		}
		public List<Digit1Context> digit1() {
			return getRuleContexts(Digit1Context.class);
		}
		public Digit1Context digit1(int i) {
			return getRuleContext(Digit1Context.class,i);
		}
		public Digit2Context digit2() {
			return getRuleContext(Digit2Context.class,0);
		}
		public Digit3Context digit3() {
			return getRuleContext(Digit3Context.class,0);
		}
		public OctetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_octet; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterOctet(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitOctet(this);
		}
	}

	public final OctetContext octet() throws RecognitionException {
		OctetContext _localctx = new OctetContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_octet);
		try {
			setState(63);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(47);
				match(T__1);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				digitnozero();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(49);
				digitnozero();
				setState(50);
				digit1();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(52);
				match(T__2);
				setState(53);
				digit1();
				setState(54);
				digit1();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(56);
				match(T__3);
				setState(57);
				digit2();
				setState(58);
				digit1();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(60);
				match(T__3);
				setState(61);
				match(T__4);
				setState(62);
				digit3();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Digit1Context extends ParserRuleContext {
		public Digit1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_digit1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterDigit1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitDigit1(this);
		}
	}

	public final Digit1Context digit1() throws RecognitionException {
		Digit1Context _localctx = new Digit1Context(_ctx, getState());
		enterRule(_localctx, 8, RULE_digit1);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4092L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Digit2Context extends ParserRuleContext {
		public Digit2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_digit2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterDigit2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitDigit2(this);
		}
	}

	public final Digit2Context digit2() throws RecognitionException {
		Digit2Context _localctx = new Digit2Context(_ctx, getState());
		enterRule(_localctx, 10, RULE_digit2);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 220L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Digit3Context extends ParserRuleContext {
		public Digit3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_digit3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterDigit3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitDigit3(this);
		}
	}

	public final Digit3Context digit3() throws RecognitionException {
		Digit3Context _localctx = new Digit3Context(_ctx, getState());
		enterRule(_localctx, 12, RULE_digit3);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 252L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DigitnozeroContext extends ParserRuleContext {
		public DigitnozeroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_digitnozero; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterDigitnozero(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitDigitnozero(this);
		}
	}

	public final DigitnozeroContext digitnozero() throws RecognitionException {
		DigitnozeroContext _localctx = new DigitnozeroContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_digitnozero);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4088L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Ipv6Context extends ParserRuleContext {
		public List<HextetContext> hextet() {
			return getRuleContexts(HextetContext.class);
		}
		public HextetContext hextet(int i) {
			return getRuleContext(HextetContext.class,i);
		}
		public Ipv6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ipv6; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterIpv6(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitIpv6(this);
		}
	}

	public final Ipv6Context ipv6() throws RecognitionException {
		Ipv6Context _localctx = new Ipv6Context(_ctx, getState());
		enterRule(_localctx, 16, RULE_ipv6);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			hextet();
			setState(74);
			match(T__11);
			setState(75);
			hextet();
			setState(76);
			match(T__11);
			setState(77);
			hextet();
			setState(78);
			match(T__11);
			setState(79);
			hextet();
			setState(80);
			match(T__11);
			setState(81);
			hextet();
			setState(82);
			match(T__11);
			setState(83);
			hextet();
			setState(84);
			match(T__11);
			setState(85);
			hextet();
			setState(86);
			match(T__11);
			setState(87);
			hextet();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HextetContext extends ParserRuleContext {
		public H1Context h1() {
			return getRuleContext(H1Context.class,0);
		}
		public H2Context h2() {
			return getRuleContext(H2Context.class,0);
		}
		public H3Context h3() {
			return getRuleContext(H3Context.class,0);
		}
		public H4Context h4() {
			return getRuleContext(H4Context.class,0);
		}
		public HextetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hextet; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterHextet(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitHextet(this);
		}
	}

	public final HextetContext hextet() throws RecognitionException {
		HextetContext _localctx = new HextetContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_hextet);
		try {
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				h1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(90);
				h2();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(91);
				h3();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(92);
				h4();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class H1Context extends ParserRuleContext {
		public HexContext hex() {
			return getRuleContext(HexContext.class,0);
		}
		public H1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_h1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterH1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitH1(this);
		}
	}

	public final H1Context h1() throws RecognitionException {
		H1Context _localctx = new H1Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_h1);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			hex();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class H2Context extends ParserRuleContext {
		public List<HexContext> hex() {
			return getRuleContexts(HexContext.class);
		}
		public HexContext hex(int i) {
			return getRuleContext(HexContext.class,i);
		}
		public H2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_h2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterH2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitH2(this);
		}
	}

	public final H2Context h2() throws RecognitionException {
		H2Context _localctx = new H2Context(_ctx, getState());
		enterRule(_localctx, 22, RULE_h2);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			hex();
			setState(98);
			hex();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class H3Context extends ParserRuleContext {
		public List<HexContext> hex() {
			return getRuleContexts(HexContext.class);
		}
		public HexContext hex(int i) {
			return getRuleContext(HexContext.class,i);
		}
		public H3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_h3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterH3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitH3(this);
		}
	}

	public final H3Context h3() throws RecognitionException {
		H3Context _localctx = new H3Context(_ctx, getState());
		enterRule(_localctx, 24, RULE_h3);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			hex();
			setState(101);
			hex();
			setState(102);
			hex();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class H4Context extends ParserRuleContext {
		public List<HexContext> hex() {
			return getRuleContexts(HexContext.class);
		}
		public HexContext hex(int i) {
			return getRuleContext(HexContext.class,i);
		}
		public H4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_h4; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterH4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitH4(this);
		}
	}

	public final H4Context h4() throws RecognitionException {
		H4Context _localctx = new H4Context(_ctx, getState());
		enterRule(_localctx, 26, RULE_h4);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			hex();
			setState(105);
			hex();
			setState(106);
			hex();
			setState(107);
			hex();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HexContext extends ParserRuleContext {
		public Digit1Context digit1() {
			return getRuleContext(Digit1Context.class,0);
		}
		public LetterContext letter() {
			return getRuleContext(LetterContext.class,0);
		}
		public HexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hex; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterHex(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitHex(this);
		}
	}

	public final HexContext hex() throws RecognitionException {
		HexContext _localctx = new HexContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_hex);
		try {
			setState(111);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				digit1();
				}
				break;
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
			case T__17:
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				letter();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetterContext extends ParserRuleContext {
		public LetterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).enterLetter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ConvertedGrammarListener ) ((ConvertedGrammarListener)listener).exitLetter(this);
		}
	}

	public final LetterContext letter() throws RecognitionException {
		LetterContext _localctx = new LetterContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_letter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 516096L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0013t\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001"+
		"&\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u0003@\b\u0003\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0003\t^\b\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0003\u000ep\b\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0000\u0000\u0010\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u001e\u0000\u0005\u0001\u0000\u0002\u000b"+
		"\u0002\u0000\u0002\u0004\u0006\u0007\u0001\u0000\u0002\u0007\u0001\u0000"+
		"\u0003\u000b\u0001\u0000\r\u0012m\u0000 \u0001\u0000\u0000\u0000\u0002"+
		"%\u0001\u0000\u0000\u0000\u0004\'\u0001\u0000\u0000\u0000\u0006?\u0001"+
		"\u0000\u0000\u0000\bA\u0001\u0000\u0000\u0000\nC\u0001\u0000\u0000\u0000"+
		"\fE\u0001\u0000\u0000\u0000\u000eG\u0001\u0000\u0000\u0000\u0010I\u0001"+
		"\u0000\u0000\u0000\u0012]\u0001\u0000\u0000\u0000\u0014_\u0001\u0000\u0000"+
		"\u0000\u0016a\u0001\u0000\u0000\u0000\u0018d\u0001\u0000\u0000\u0000\u001a"+
		"h\u0001\u0000\u0000\u0000\u001co\u0001\u0000\u0000\u0000\u001eq\u0001"+
		"\u0000\u0000\u0000 !\u0003\u0002\u0001\u0000!\"\u0005\u0000\u0000\u0001"+
		"\"\u0001\u0001\u0000\u0000\u0000#&\u0003\u0004\u0002\u0000$&\u0003\u0010"+
		"\b\u0000%#\u0001\u0000\u0000\u0000%$\u0001\u0000\u0000\u0000&\u0003\u0001"+
		"\u0000\u0000\u0000\'(\u0003\u0006\u0003\u0000()\u0005\u0001\u0000\u0000"+
		")*\u0003\u0006\u0003\u0000*+\u0005\u0001\u0000\u0000+,\u0003\u0006\u0003"+
		"\u0000,-\u0005\u0001\u0000\u0000-.\u0003\u0006\u0003\u0000.\u0005\u0001"+
		"\u0000\u0000\u0000/@\u0005\u0002\u0000\u00000@\u0003\u000e\u0007\u0000"+
		"12\u0003\u000e\u0007\u000023\u0003\b\u0004\u00003@\u0001\u0000\u0000\u0000"+
		"45\u0005\u0003\u0000\u000056\u0003\b\u0004\u000067\u0003\b\u0004\u0000"+
		"7@\u0001\u0000\u0000\u000089\u0005\u0004\u0000\u00009:\u0003\n\u0005\u0000"+
		":;\u0003\b\u0004\u0000;@\u0001\u0000\u0000\u0000<=\u0005\u0004\u0000\u0000"+
		"=>\u0005\u0005\u0000\u0000>@\u0003\f\u0006\u0000?/\u0001\u0000\u0000\u0000"+
		"?0\u0001\u0000\u0000\u0000?1\u0001\u0000\u0000\u0000?4\u0001\u0000\u0000"+
		"\u0000?8\u0001\u0000\u0000\u0000?<\u0001\u0000\u0000\u0000@\u0007\u0001"+
		"\u0000\u0000\u0000AB\u0007\u0000\u0000\u0000B\t\u0001\u0000\u0000\u0000"+
		"CD\u0007\u0001\u0000\u0000D\u000b\u0001\u0000\u0000\u0000EF\u0007\u0002"+
		"\u0000\u0000F\r\u0001\u0000\u0000\u0000GH\u0007\u0003\u0000\u0000H\u000f"+
		"\u0001\u0000\u0000\u0000IJ\u0003\u0012\t\u0000JK\u0005\f\u0000\u0000K"+
		"L\u0003\u0012\t\u0000LM\u0005\f\u0000\u0000MN\u0003\u0012\t\u0000NO\u0005"+
		"\f\u0000\u0000OP\u0003\u0012\t\u0000PQ\u0005\f\u0000\u0000QR\u0003\u0012"+
		"\t\u0000RS\u0005\f\u0000\u0000ST\u0003\u0012\t\u0000TU\u0005\f\u0000\u0000"+
		"UV\u0003\u0012\t\u0000VW\u0005\f\u0000\u0000WX\u0003\u0012\t\u0000X\u0011"+
		"\u0001\u0000\u0000\u0000Y^\u0003\u0014\n\u0000Z^\u0003\u0016\u000b\u0000"+
		"[^\u0003\u0018\f\u0000\\^\u0003\u001a\r\u0000]Y\u0001\u0000\u0000\u0000"+
		"]Z\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000]\\\u0001\u0000\u0000"+
		"\u0000^\u0013\u0001\u0000\u0000\u0000_`\u0003\u001c\u000e\u0000`\u0015"+
		"\u0001\u0000\u0000\u0000ab\u0003\u001c\u000e\u0000bc\u0003\u001c\u000e"+
		"\u0000c\u0017\u0001\u0000\u0000\u0000de\u0003\u001c\u000e\u0000ef\u0003"+
		"\u001c\u000e\u0000fg\u0003\u001c\u000e\u0000g\u0019\u0001\u0000\u0000"+
		"\u0000hi\u0003\u001c\u000e\u0000ij\u0003\u001c\u000e\u0000jk\u0003\u001c"+
		"\u000e\u0000kl\u0003\u001c\u000e\u0000l\u001b\u0001\u0000\u0000\u0000"+
		"mp\u0003\b\u0004\u0000np\u0003\u001e\u000f\u0000om\u0001\u0000\u0000\u0000"+
		"on\u0001\u0000\u0000\u0000p\u001d\u0001\u0000\u0000\u0000qr\u0007\u0004"+
		"\u0000\u0000r\u001f\u0001\u0000\u0000\u0000\u0004%?]o";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}