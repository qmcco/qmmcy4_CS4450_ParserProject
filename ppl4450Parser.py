# Generated from ppl4450.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,295,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        3,1,43,8,1,1,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,1,2,3,2,55,8,2,
        1,2,1,2,1,2,1,2,3,2,61,8,2,1,2,1,2,1,2,1,2,3,2,67,8,2,1,2,1,2,1,
        2,1,2,3,2,73,8,2,3,2,75,8,2,1,3,1,3,1,3,3,3,80,8,3,1,3,1,3,1,3,5,
        3,85,8,3,10,3,12,3,88,9,3,1,4,1,4,1,4,5,4,93,8,4,10,4,12,4,96,9,
        4,1,5,1,5,1,5,5,5,101,8,5,10,5,12,5,104,9,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,117,8,6,1,7,1,7,1,7,1,7,5,7,123,8,7,
        10,7,12,7,126,9,7,3,7,128,8,7,1,7,1,7,1,8,1,8,1,8,5,8,135,8,8,10,
        8,12,8,138,9,8,1,9,3,9,141,8,9,1,9,3,9,144,8,9,1,9,1,9,1,9,5,9,149,
        8,9,10,9,12,9,152,9,9,1,9,3,9,155,8,9,1,10,1,10,1,10,1,10,1,10,1,
        10,4,10,163,8,10,11,10,12,10,164,1,10,1,10,1,10,4,10,170,8,10,11,
        10,12,10,171,4,10,174,8,10,11,10,12,10,175,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,4,10,185,8,10,11,10,12,10,186,1,10,1,10,1,10,4,10,192,
        8,10,11,10,12,10,193,4,10,196,8,10,11,10,12,10,197,1,10,1,10,5,10,
        202,8,10,10,10,12,10,205,9,10,1,10,1,10,1,10,1,10,1,10,4,10,212,
        8,10,11,10,12,10,213,1,10,1,10,1,10,4,10,219,8,10,11,10,12,10,220,
        4,10,223,8,10,11,10,12,10,224,1,10,1,10,3,10,229,8,10,1,11,1,11,
        1,11,1,11,1,11,1,11,4,11,237,8,11,11,11,12,11,238,1,11,1,11,1,11,
        4,11,244,8,11,11,11,12,11,245,4,11,248,8,11,11,11,12,11,249,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,3,12,259,8,12,1,12,1,12,1,12,1,12,
        4,12,265,8,12,11,12,12,12,266,1,12,1,12,1,12,4,12,272,8,12,11,12,
        12,12,273,4,12,276,8,12,11,12,12,12,277,1,12,1,12,1,13,1,13,1,13,
        1,13,1,13,3,13,287,8,13,1,13,1,13,3,13,291,8,13,1,13,1,13,1,13,0,
        1,6,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,5,1,0,23,24,1,0,1,
        2,1,0,3,5,1,0,17,22,2,0,33,33,35,35,342,0,32,1,0,0,0,2,42,1,0,0,
        0,4,74,1,0,0,0,6,79,1,0,0,0,8,89,1,0,0,0,10,97,1,0,0,0,12,116,1,
        0,0,0,14,118,1,0,0,0,16,131,1,0,0,0,18,140,1,0,0,0,20,156,1,0,0,
        0,22,230,1,0,0,0,24,253,1,0,0,0,26,281,1,0,0,0,28,31,5,40,0,0,29,
        31,3,2,1,0,30,28,1,0,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,
        0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,5,0,0,1,36,1,1,
        0,0,0,37,43,3,4,2,0,38,43,3,6,3,0,39,43,3,20,10,0,40,43,3,22,11,
        0,41,43,3,24,12,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,
        1,0,0,0,42,41,1,0,0,0,43,3,1,0,0,0,44,45,5,33,0,0,45,48,5,12,0,0,
        46,49,5,33,0,0,47,49,3,6,3,0,48,46,1,0,0,0,48,47,1,0,0,0,49,75,1,
        0,0,0,50,51,5,33,0,0,51,54,5,13,0,0,52,55,5,33,0,0,53,55,3,6,3,0,
        54,52,1,0,0,0,54,53,1,0,0,0,55,75,1,0,0,0,56,57,5,33,0,0,57,60,5,
        14,0,0,58,61,5,33,0,0,59,61,3,6,3,0,60,58,1,0,0,0,60,59,1,0,0,0,
        61,75,1,0,0,0,62,63,5,33,0,0,63,66,5,15,0,0,64,67,5,33,0,0,65,67,
        3,6,3,0,66,64,1,0,0,0,66,65,1,0,0,0,67,75,1,0,0,0,68,69,5,33,0,0,
        69,72,5,16,0,0,70,73,5,33,0,0,71,73,3,6,3,0,72,70,1,0,0,0,72,71,
        1,0,0,0,73,75,1,0,0,0,74,44,1,0,0,0,74,50,1,0,0,0,74,56,1,0,0,0,
        74,62,1,0,0,0,74,68,1,0,0,0,75,5,1,0,0,0,76,77,6,3,-1,0,77,80,3,
        8,4,0,78,80,3,18,9,0,79,76,1,0,0,0,79,78,1,0,0,0,80,86,1,0,0,0,81,
        82,10,1,0,0,82,83,7,0,0,0,83,85,3,6,3,2,84,81,1,0,0,0,85,88,1,0,
        0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,7,1,0,0,0,88,86,1,0,0,0,89,94,
        3,10,5,0,90,91,7,1,0,0,91,93,3,10,5,0,92,90,1,0,0,0,93,96,1,0,0,
        0,94,92,1,0,0,0,94,95,1,0,0,0,95,9,1,0,0,0,96,94,1,0,0,0,97,102,
        3,12,6,0,98,99,7,2,0,0,99,101,3,12,6,0,100,98,1,0,0,0,101,104,1,
        0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,11,1,0,0,0,104,102,1,0,
        0,0,105,117,5,33,0,0,106,107,5,33,0,0,107,108,5,27,0,0,108,109,3,
        6,3,0,109,110,5,28,0,0,110,117,1,0,0,0,111,117,3,14,7,0,112,117,
        5,35,0,0,113,117,5,36,0,0,114,117,5,34,0,0,115,117,5,37,0,0,116,
        105,1,0,0,0,116,106,1,0,0,0,116,111,1,0,0,0,116,112,1,0,0,0,116,
        113,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,13,1,0,0,0,118,127,
        5,27,0,0,119,124,3,6,3,0,120,121,5,31,0,0,121,123,3,6,3,0,122,120,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,128,
        1,0,0,0,126,124,1,0,0,0,127,119,1,0,0,0,127,128,1,0,0,0,128,129,
        1,0,0,0,129,130,5,28,0,0,130,15,1,0,0,0,131,136,3,18,9,0,132,133,
        7,0,0,0,133,135,3,18,9,0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,17,1,0,0,0,138,136,1,0,0,0,139,141,5,
        29,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,144,5,
        25,0,0,143,142,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,150,3,
        8,4,0,146,147,7,3,0,0,147,149,3,8,4,0,148,146,1,0,0,0,149,152,1,
        0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,154,1,0,0,0,152,150,1,
        0,0,0,153,155,5,30,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,19,1,
        0,0,0,156,157,5,6,0,0,157,158,3,6,3,0,158,159,5,32,0,0,159,173,5,
        44,0,0,160,163,3,4,2,0,161,163,3,6,3,0,162,160,1,0,0,0,162,161,1,
        0,0,0,163,164,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,166,1,
        0,0,0,166,167,5,40,0,0,167,174,1,0,0,0,168,170,3,2,1,0,169,168,1,
        0,0,0,170,171,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,174,1,
        0,0,0,173,162,1,0,0,0,173,169,1,0,0,0,174,175,1,0,0,0,175,173,1,
        0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,203,5,45,0,0,178,179,5,
        7,0,0,179,180,3,6,3,0,180,181,5,32,0,0,181,195,5,44,0,0,182,185,
        3,4,2,0,183,185,3,6,3,0,184,182,1,0,0,0,184,183,1,0,0,0,185,186,
        1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,189,
        5,40,0,0,189,196,1,0,0,0,190,192,3,2,1,0,191,190,1,0,0,0,192,193,
        1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,196,1,0,0,0,195,184,
        1,0,0,0,195,191,1,0,0,0,196,197,1,0,0,0,197,195,1,0,0,0,197,198,
        1,0,0,0,198,199,1,0,0,0,199,200,5,45,0,0,200,202,1,0,0,0,201,178,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,228,
        1,0,0,0,205,203,1,0,0,0,206,207,5,8,0,0,207,208,5,32,0,0,208,222,
        5,44,0,0,209,212,3,4,2,0,210,212,3,6,3,0,211,209,1,0,0,0,211,210,
        1,0,0,0,212,213,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,215,
        1,0,0,0,215,216,5,40,0,0,216,223,1,0,0,0,217,219,3,2,1,0,218,217,
        1,0,0,0,219,220,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,223,
        1,0,0,0,222,211,1,0,0,0,222,218,1,0,0,0,223,224,1,0,0,0,224,222,
        1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,227,5,45,0,0,227,229,
        1,0,0,0,228,206,1,0,0,0,228,229,1,0,0,0,229,21,1,0,0,0,230,231,5,
        9,0,0,231,232,3,6,3,0,232,233,5,32,0,0,233,247,5,44,0,0,234,237,
        3,4,2,0,235,237,3,6,3,0,236,234,1,0,0,0,236,235,1,0,0,0,237,238,
        1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,
        5,40,0,0,241,248,1,0,0,0,242,244,3,2,1,0,243,242,1,0,0,0,244,245,
        1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,248,1,0,0,0,247,236,
        1,0,0,0,247,243,1,0,0,0,248,249,1,0,0,0,249,247,1,0,0,0,249,250,
        1,0,0,0,250,251,1,0,0,0,251,252,5,45,0,0,252,23,1,0,0,0,253,254,
        5,10,0,0,254,255,5,33,0,0,255,258,5,11,0,0,256,259,5,33,0,0,257,
        259,3,26,13,0,258,256,1,0,0,0,258,257,1,0,0,0,259,260,1,0,0,0,260,
        261,5,32,0,0,261,275,5,44,0,0,262,265,3,4,2,0,263,265,3,6,3,0,264,
        262,1,0,0,0,264,263,1,0,0,0,265,266,1,0,0,0,266,264,1,0,0,0,266,
        267,1,0,0,0,267,268,1,0,0,0,268,269,5,40,0,0,269,276,1,0,0,0,270,
        272,3,2,1,0,271,270,1,0,0,0,272,273,1,0,0,0,273,271,1,0,0,0,273,
        274,1,0,0,0,274,276,1,0,0,0,275,264,1,0,0,0,275,271,1,0,0,0,276,
        277,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,
        280,5,45,0,0,280,25,1,0,0,0,281,282,5,26,0,0,282,283,5,29,0,0,283,
        286,7,4,0,0,284,285,5,31,0,0,285,287,7,4,0,0,286,284,1,0,0,0,286,
        287,1,0,0,0,287,290,1,0,0,0,288,289,5,31,0,0,289,291,7,4,0,0,290,
        288,1,0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,293,5,30,0,0,293,
        27,1,0,0,0,51,30,32,42,48,54,60,66,72,74,79,86,94,102,116,124,127,
        136,140,143,150,154,162,164,171,173,175,184,186,193,195,197,203,
        211,213,220,222,224,228,236,238,245,247,249,258,264,266,273,275,
        277,286,290
    ]

class ppl4450Parser ( Parser ):

    grammarFileName = "ppl4450.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'if'", 
                     "'elif'", "'else'", "'while'", "'for'", "'in'", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "'and'", "'or'", "'not'", "'range'", 
                     "'['", "']'", "'('", "')'", "','", "':'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\t'", "'\\b'" ]

    symbolicNames = [ "<INVALID>", "PLU", "MIN", "MUL", "DIV", "MOD", "IF", 
                      "ELIF", "ELSE", "WH", "FOR", "IN", "EQU", "EQU_P", 
                      "EQU_MI", "EQU_MU", "EQU_D", "CLT", "CGT", "CLTE", 
                      "CGTE", "CEQU", "CNEQU", "AND", "OR", "NOT", "RAN", 
                      "BRA_O", "BRA_C", "PAR_O", "PAR_C", "COM", "COL", 
                      "ID", "STR", "INT", "FLO", "BOOL", "INDT", "OUTDT", 
                      "NL", "WS", "HCOM", "ACOM", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_operation = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_arithmetic = 4
    RULE_operator = 5
    RULE_elem = 6
    RULE_array = 7
    RULE_comparison = 8
    RULE_conditional = 9
    RULE_if_st = 10
    RULE_while_st = 11
    RULE_for_st = 12
    RULE_range = 13

    ruleNames =  [ "program", "operation", "assignment", "expression", "arithmetic", 
                   "operator", "elem", "array", "comparison", "conditional", 
                   "if_st", "while_st", "for_st", "range" ]

    EOF = Token.EOF
    PLU=1
    MIN=2
    MUL=3
    DIV=4
    MOD=5
    IF=6
    ELIF=7
    ELSE=8
    WH=9
    FOR=10
    IN=11
    EQU=12
    EQU_P=13
    EQU_MI=14
    EQU_MU=15
    EQU_D=16
    CLT=17
    CGT=18
    CLTE=19
    CGTE=20
    CEQU=21
    CNEQU=22
    AND=23
    OR=24
    NOT=25
    RAN=26
    BRA_O=27
    BRA_C=28
    PAR_O=29
    PAR_C=30
    COM=31
    COL=32
    ID=33
    STR=34
    INT=35
    FLO=36
    BOOL=37
    INDT=38
    OUTDT=39
    NL=40
    WS=41
    HCOM=42
    ACOM=43
    INDENT=44
    DEDENT=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ppl4450Parser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.NL)
            else:
                return self.getToken(ppl4450Parser.NL, i)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.OperationContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.OperationContext,i)


        def getRuleIndex(self):
            return ppl4450Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ppl4450Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1366504244800) != 0):
                self.state = 30
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 28
                    self.match(ppl4450Parser.NL)
                    pass
                elif token in [6, 9, 10, 25, 27, 29, 33, 34, 35, 36, 37]:
                    self.state = 29
                    self.operation()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(ppl4450Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ppl4450Parser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,0)


        def if_st(self):
            return self.getTypedRuleContext(ppl4450Parser.If_stContext,0)


        def while_st(self):
            return self.getTypedRuleContext(ppl4450Parser.While_stContext,0)


        def for_st(self):
            return self.getTypedRuleContext(ppl4450Parser.For_stContext,0)


        def getRuleIndex(self):
            return ppl4450Parser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = ppl4450Parser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 37
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 38
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 39
                self.if_st()
                pass

            elif la_ == 4:
                self.state = 40
                self.while_st()
                pass

            elif la_ == 5:
                self.state = 41
                self.for_st()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.ID)
            else:
                return self.getToken(ppl4450Parser.ID, i)

        def EQU(self):
            return self.getToken(ppl4450Parser.EQU, 0)

        def expression(self):
            return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,0)


        def EQU_P(self):
            return self.getToken(ppl4450Parser.EQU_P, 0)

        def EQU_MI(self):
            return self.getToken(ppl4450Parser.EQU_MI, 0)

        def EQU_MU(self):
            return self.getToken(ppl4450Parser.EQU_MU, 0)

        def EQU_D(self):
            return self.getToken(ppl4450Parser.EQU_D, 0)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ppl4450Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(ppl4450Parser.ID)
                self.state = 45
                self.match(ppl4450Parser.EQU)
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.match(ppl4450Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 47
                    self.expression(0)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(ppl4450Parser.ID)
                self.state = 51
                self.match(ppl4450Parser.EQU_P)
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.match(ppl4450Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 53
                    self.expression(0)
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(ppl4450Parser.ID)
                self.state = 57
                self.match(ppl4450Parser.EQU_MI)
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.match(ppl4450Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.expression(0)
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(ppl4450Parser.ID)
                self.state = 63
                self.match(ppl4450Parser.EQU_MU)
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 64
                    self.match(ppl4450Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 65
                    self.expression(0)
                    pass


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.match(ppl4450Parser.ID)
                self.state = 69
                self.match(ppl4450Parser.EQU_D)
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 70
                    self.match(ppl4450Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 71
                    self.expression(0)
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(ppl4450Parser.ArithmeticContext,0)


        def conditional(self):
            return self.getTypedRuleContext(ppl4450Parser.ConditionalContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,i)


        def AND(self):
            return self.getToken(ppl4450Parser.AND, 0)

        def OR(self):
            return self.getToken(ppl4450Parser.OR, 0)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ppl4450Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 77
                self.arithmetic()
                pass

            elif la_ == 2:
                self.state = 78
                self.conditional()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ppl4450Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 81
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 82
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 83
                    self.expression(2) 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.OperatorContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.OperatorContext,i)


        def PLU(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.PLU)
            else:
                return self.getToken(ppl4450Parser.PLU, i)

        def MIN(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.MIN)
            else:
                return self.getToken(ppl4450Parser.MIN, i)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)




    def arithmetic(self):

        localctx = ppl4450Parser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.operator()
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 90
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 91
                    self.operator() 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ElemContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ElemContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.MUL)
            else:
                return self.getToken(ppl4450Parser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.DIV)
            else:
                return self.getToken(ppl4450Parser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.MOD)
            else:
                return self.getToken(ppl4450Parser.MOD, i)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = ppl4450Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.elem()
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 99
                    self.elem() 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ppl4450Parser.ID, 0)

        def BRA_O(self):
            return self.getToken(ppl4450Parser.BRA_O, 0)

        def expression(self):
            return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,0)


        def BRA_C(self):
            return self.getToken(ppl4450Parser.BRA_C, 0)

        def array(self):
            return self.getTypedRuleContext(ppl4450Parser.ArrayContext,0)


        def INT(self):
            return self.getToken(ppl4450Parser.INT, 0)

        def FLO(self):
            return self.getToken(ppl4450Parser.FLO, 0)

        def STR(self):
            return self.getToken(ppl4450Parser.STR, 0)

        def BOOL(self):
            return self.getToken(ppl4450Parser.BOOL, 0)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElem" ):
                listener.enterElem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElem" ):
                listener.exitElem(self)




    def elem(self):

        localctx = ppl4450Parser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elem)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(ppl4450Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(ppl4450Parser.ID)
                self.state = 107
                self.match(ppl4450Parser.BRA_O)
                self.state = 108
                self.expression(0)
                self.state = 109
                self.match(ppl4450Parser.BRA_C)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.array()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.match(ppl4450Parser.INT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.match(ppl4450Parser.FLO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.match(ppl4450Parser.STR)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 115
                self.match(ppl4450Parser.BOOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRA_O(self):
            return self.getToken(ppl4450Parser.BRA_O, 0)

        def BRA_C(self):
            return self.getToken(ppl4450Parser.BRA_C, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.COM)
            else:
                return self.getToken(ppl4450Parser.COM, i)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = ppl4450Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ppl4450Parser.BRA_O)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 266992615424) != 0):
                self.state = 119
                self.expression(0)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 120
                    self.match(ppl4450Parser.COM)
                    self.state = 121
                    self.expression(0)
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 129
            self.match(ppl4450Parser.BRA_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ConditionalContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ConditionalContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.AND)
            else:
                return self.getToken(ppl4450Parser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.OR)
            else:
                return self.getToken(ppl4450Parser.OR, i)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = ppl4450Parser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.conditional()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.conditional()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ArithmeticContext,i)


        def CLT(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.CLT)
            else:
                return self.getToken(ppl4450Parser.CLT, i)

        def CGT(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.CGT)
            else:
                return self.getToken(ppl4450Parser.CGT, i)

        def CLTE(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.CLTE)
            else:
                return self.getToken(ppl4450Parser.CLTE, i)

        def CGTE(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.CGTE)
            else:
                return self.getToken(ppl4450Parser.CGTE, i)

        def CEQU(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.CEQU)
            else:
                return self.getToken(ppl4450Parser.CEQU, i)

        def CNEQU(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.CNEQU)
            else:
                return self.getToken(ppl4450Parser.CNEQU, i)

        def PAR_O(self):
            return self.getToken(ppl4450Parser.PAR_O, 0)

        def NOT(self):
            return self.getToken(ppl4450Parser.NOT, 0)

        def PAR_C(self):
            return self.getToken(ppl4450Parser.PAR_C, 0)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = ppl4450Parser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 139
                self.match(ppl4450Parser.PAR_O)



            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 142
                self.match(ppl4450Parser.NOT)


            self.state = 145
            self.arithmetic()
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 146
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 147
                    self.arithmetic() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 153
                self.match(ppl4450Parser.PAR_C)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ppl4450Parser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,i)


        def COL(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.COL)
            else:
                return self.getToken(ppl4450Parser.COL, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.INDENT)
            else:
                return self.getToken(ppl4450Parser.INDENT, i)

        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.DEDENT)
            else:
                return self.getToken(ppl4450Parser.DEDENT, i)

        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.ELIF)
            else:
                return self.getToken(ppl4450Parser.ELIF, i)

        def ELSE(self):
            return self.getToken(ppl4450Parser.ELSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.NL)
            else:
                return self.getToken(ppl4450Parser.NL, i)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.OperationContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.OperationContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.AssignmentContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.AssignmentContext,i)


        def getRuleIndex(self):
            return ppl4450Parser.RULE_if_st

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_st" ):
                listener.enterIf_st(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_st" ):
                listener.exitIf_st(self)




    def if_st(self):

        localctx = ppl4450Parser.If_stContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_st)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ppl4450Parser.IF)
            self.state = 157
            self.expression(0)
            self.state = 158
            self.match(ppl4450Parser.COL)
            self.state = 159
            self.match(ppl4450Parser.INDENT)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 162 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 162
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                        if la_ == 1:
                            self.state = 160
                            self.assignment()
                            pass

                        elif la_ == 2:
                            self.state = 161
                            self.expression(0)
                            pass


                        self.state = 164 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992615424) != 0)):
                            break

                    self.state = 166
                    self.match(ppl4450Parser.NL)
                    pass

                elif la_ == 2:
                    self.state = 169 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 168
                            self.operation()

                        else:
                            raise NoViableAltException(self)
                        self.state = 171 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                    pass


                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992617024) != 0)):
                    break

            self.state = 177
            self.match(ppl4450Parser.DEDENT)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 178
                self.match(ppl4450Parser.ELIF)
                self.state = 179
                self.expression(0)
                self.state = 180
                self.match(ppl4450Parser.COL)
                self.state = 181
                self.match(ppl4450Parser.INDENT)
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 184 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 184
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                            if la_ == 1:
                                self.state = 182
                                self.assignment()
                                pass

                            elif la_ == 2:
                                self.state = 183
                                self.expression(0)
                                pass


                            self.state = 186 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992615424) != 0)):
                                break

                        self.state = 188
                        self.match(ppl4450Parser.NL)
                        pass

                    elif la_ == 2:
                        self.state = 191 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 190
                                self.operation()

                            else:
                                raise NoViableAltException(self)
                            self.state = 193 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                        pass


                    self.state = 197 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992617024) != 0)):
                        break

                self.state = 199
                self.match(ppl4450Parser.DEDENT)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 206
                self.match(ppl4450Parser.ELSE)
                self.state = 207
                self.match(ppl4450Parser.COL)
                self.state = 208
                self.match(ppl4450Parser.INDENT)
                self.state = 222 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 211 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 211
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                            if la_ == 1:
                                self.state = 209
                                self.assignment()
                                pass

                            elif la_ == 2:
                                self.state = 210
                                self.expression(0)
                                pass


                            self.state = 213 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992615424) != 0)):
                                break

                        self.state = 215
                        self.match(ppl4450Parser.NL)
                        pass

                    elif la_ == 2:
                        self.state = 218 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 217
                                self.operation()

                            else:
                                raise NoViableAltException(self)
                            self.state = 220 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                        pass


                    self.state = 224 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992617024) != 0)):
                        break

                self.state = 226
                self.match(ppl4450Parser.DEDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WH(self):
            return self.getToken(ppl4450Parser.WH, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,i)


        def COL(self):
            return self.getToken(ppl4450Parser.COL, 0)

        def INDENT(self):
            return self.getToken(ppl4450Parser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(ppl4450Parser.DEDENT, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.NL)
            else:
                return self.getToken(ppl4450Parser.NL, i)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.OperationContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.OperationContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.AssignmentContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.AssignmentContext,i)


        def getRuleIndex(self):
            return ppl4450Parser.RULE_while_st

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_st" ):
                listener.enterWhile_st(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_st" ):
                listener.exitWhile_st(self)




    def while_st(self):

        localctx = ppl4450Parser.While_stContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_while_st)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ppl4450Parser.WH)
            self.state = 231
            self.expression(0)
            self.state = 232
            self.match(ppl4450Parser.COL)
            self.state = 233
            self.match(ppl4450Parser.INDENT)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 247
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 236 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 236
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                        if la_ == 1:
                            self.state = 234
                            self.assignment()
                            pass

                        elif la_ == 2:
                            self.state = 235
                            self.expression(0)
                            pass


                        self.state = 238 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992615424) != 0)):
                            break

                    self.state = 240
                    self.match(ppl4450Parser.NL)
                    pass

                elif la_ == 2:
                    self.state = 243 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 242
                            self.operation()

                        else:
                            raise NoViableAltException(self)
                        self.state = 245 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                    pass


                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992617024) != 0)):
                    break

            self.state = 251
            self.match(ppl4450Parser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ppl4450Parser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.ID)
            else:
                return self.getToken(ppl4450Parser.ID, i)

        def IN(self):
            return self.getToken(ppl4450Parser.IN, 0)

        def COL(self):
            return self.getToken(ppl4450Parser.COL, 0)

        def INDENT(self):
            return self.getToken(ppl4450Parser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(ppl4450Parser.DEDENT, 0)

        def range_(self):
            return self.getTypedRuleContext(ppl4450Parser.RangeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.NL)
            else:
                return self.getToken(ppl4450Parser.NL, i)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.OperationContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.OperationContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.AssignmentContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.AssignmentContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ppl4450Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ppl4450Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return ppl4450Parser.RULE_for_st

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_st" ):
                listener.enterFor_st(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_st" ):
                listener.exitFor_st(self)




    def for_st(self):

        localctx = ppl4450Parser.For_stContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_st)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ppl4450Parser.FOR)
            self.state = 254
            self.match(ppl4450Parser.ID)
            self.state = 255
            self.match(ppl4450Parser.IN)
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 256
                self.match(ppl4450Parser.ID)
                pass
            elif token in [26]:
                self.state = 257
                self.range_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 260
            self.match(ppl4450Parser.COL)
            self.state = 261
            self.match(ppl4450Parser.INDENT)
            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 275
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 264 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 264
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                        if la_ == 1:
                            self.state = 262
                            self.assignment()
                            pass

                        elif la_ == 2:
                            self.state = 263
                            self.expression(0)
                            pass


                        self.state = 266 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992615424) != 0)):
                            break

                    self.state = 268
                    self.match(ppl4450Parser.NL)
                    pass

                elif la_ == 2:
                    self.state = 271 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 270
                            self.operation()

                        else:
                            raise NoViableAltException(self)
                        self.state = 273 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

                    pass


                self.state = 277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 266992617024) != 0)):
                    break

            self.state = 279
            self.match(ppl4450Parser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAN(self):
            return self.getToken(ppl4450Parser.RAN, 0)

        def PAR_O(self):
            return self.getToken(ppl4450Parser.PAR_O, 0)

        def PAR_C(self):
            return self.getToken(ppl4450Parser.PAR_C, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.ID)
            else:
                return self.getToken(ppl4450Parser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.INT)
            else:
                return self.getToken(ppl4450Parser.INT, i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(ppl4450Parser.COM)
            else:
                return self.getToken(ppl4450Parser.COM, i)

        def getRuleIndex(self):
            return ppl4450Parser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)




    def range_(self):

        localctx = ppl4450Parser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ppl4450Parser.RAN)
            self.state = 282
            self.match(ppl4450Parser.PAR_O)

            self.state = 283
            _la = self._input.LA(1)
            if not(_la==33 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 284
                self.match(ppl4450Parser.COM)
                self.state = 285
                _la = self._input.LA(1)
                if not(_la==33 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 288
                self.match(ppl4450Parser.COM)
                self.state = 289
                _la = self._input.LA(1)
                if not(_la==33 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 292
            self.match(ppl4450Parser.PAR_C)
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
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




