# qmmcy4_CS4450_ParserProject
A repository for my Computer Science 4450 Python Parser project submission. My implementation has been made using Antlr4, with Python being used as the language for implementation. 
## General Information
This project implements a parser to recognized and validate basic Python code. The parser is capable of recognizing basic expressions, including arithmetic, conditional, and boolean expressions, as well as variable assignments. The parser properly identifies if statements, including elif and else blocks, as well as basic while and for loops. The parser can also properly identify nested structures, such as nested loops and if statements. The parser properly handles indentations by implementing INDENT and DEDENT tokens, which are provided by the antlr-denter Python plugin, found here: https://github.com/yshavit/antlr-denter . The plugin tokenizes tabs as INDENT tokens, then tracks the number of INDENTs, and uses that number to dicate the number of expected DEDENT tokens to satify the conditions of the statement, whether that be an if, while, or for statement. These tokens are what facilitate the implementation of nested structures. The parser properly accommodates comments by identifying comment markers (# or ''') and ignoring any content after them. The details of the parser rules are written using context-free grammar, these rules are written in a .g4 file, then Antlr4 uses that .g4 file to generate the lexer and parser. @lexer::header{ and @lexer::member{ methods are used within the .g4 file to facilitate the use of the perviously mentioned antlr-denter plugin, so the lexer and parser files generated from the .g4 must be Python files, and the enviornment used to test the parser must also be written in Python (e.g., the provided main.py). main.py will properly run the parser, and will generate a visual representation of the parse tree, which is saves as a .png. This is done by making use of the graphviz Python plugin, found here: https://pypi.org/project/graphviz/ . The main.py file is a modified version of the one provided in the ANTLR_Tutorial.pdf found on the class canvas page. 
## Required Plugins
* Antlr4 version 4.13.2 https://github.com/antlr/antlr4
* antlr-denter version 1.3.1 https://github.com/yshavit/antlr-denter
* graphviz version 0.20.3 https://pypi.org/project/graphviz
## Installation/Run Tutorial
For Windows:
* Install Python3 (project was written with Python 3.13)
  * Can be installed here: https://www.python.org/downloads/
* To ensure that python packages can be installed, run ***py -m ensurepip --upgrade*** in the Command Prompt
* Install Antlr4 Python3 runtime
  * In the Command Prompt, run the command ***pip install antlr4-python3-runtime***
* Install antlr-denter
  * Run the command ***pip install antlr-denter***
* Install anaconda3 to facilitate use of graphviz plugin
  * Install here: https://www.anaconda.com/download 
* Install graphviz
  * Open an Anaconda Prompt
  * Run the command ***conda install graphviz*** note: installing via pip without anaconda may work, however it cause me issues so this is the method I would recommend
* Clone the GitHub repository
  * Run the command ***git clone https://github.com/qmcco/qmmcy4_CS4450_ParserProject.git***
* Navigate to the project folder in an Anaconda Prompt
  * Run the command ***cd qmmcy4_CS4450_ParserProject***
* In the Anaconda Prompt run the following command to test the provided project_deliverable_3.py file: ***python3 main.py project_deliverable_3.py*** this will also create a .png of the parse tree

For Ubuntu:
* Install python virtual environment library
  * Run ***sudo apt install python3-venv***
* Initialize the virtual environment: ***python3 -m venv vvv*** (vvv is the directory name)
* Activate the virtual environment: ***source vvv/bin/activate***
* Install antlr4 runtime: ***pip install antlr4-python3-runtime***
* Install antlr-denter ***pip install antlr-denter***
* Install graphviz ***pip install graphviz***
* To test the parser and produce a .png visual representation of the parse tree, run the following command: ***python3 main.py project_deliverable_3.py***

## Group Members
* Quinn McCollister

## Demo Video
The demo video is attached, the attached version is a compressed version, the original will be attached to the project submission


https://github.com/user-attachments/assets/485bc05d-6dba-44ef-a7d7-57d3efd8ed5b

