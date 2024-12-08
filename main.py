import sys
from antlr4 import *
from ppl4450Lexer import ppl4450Lexer
from ppl4450Parser import ppl4450Parser
from antlr4.tree.Tree import TerminalNode
from graphviz import Digraph


# Function to traverse the parse tree and add nodes to the graph
def add_nodes(graph, node, parentID=None):
    nodeID = str(id(node))

    if isinstance(node, TerminalNode):
        graph.node(nodeID, label=f"'{node.getText()}'", shape="box", style="filled", color="lightgrey")
    else:
        graph.node(nodeID, label=node.getText() or type(node).__name__)

    if parentID:
        graph.edge(parentID, nodeID)

    for i in range(node.getChildCount()):
        add_nodes(graph, node.getChild(i), nodeID)


# Main script
def main(argv):
    if len(sys.argv) > 1:
    	inp = FileStream(sys.argv[1])
    else:
    	inp = InputStream(sys.stdin.readline())

    lexer = ppl4450Lexer(inp)
    token_stream = CommonTokenStream(lexer)
    parser = ppl4450Parser(token_stream)
    tree = parser.program()  # Replace `startRule` with your actual grammar's start rule

    graph = Digraph(format='png')
    add_nodes(graph, tree)

    graph.render("parse_tree", cleanup=True)  # Outputs "parse_tree.png"
    print("Parse tree generated, 'parse_tree.png'")


if __name__ == "__main__":
    main(sys.argv)

