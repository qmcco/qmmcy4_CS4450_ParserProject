import sys
import antlr4
from io import StringIO
from antlr4 import *
from ppl4450Parser import ppl4450Parser
from ppl4450Lexer import ppl4450Lexer
from antlr4.tree.Trees import Trees

def main(argv):
	if len(sys.argv) > 1:
		s = FileStream(sys.argv[1])
	else:
		s = InputStream(sys.stdin.readline())
	
	lexer = ppl4450Lexer(s)
	tokens = CommonTokenStream(lexer)
	parser = ppl4450Parser(tokens)
	tree = parser.program()
	print(tree.toStringTree(recog=parser))
	
if __name__ == '__main__':
	main(sys.argv)
