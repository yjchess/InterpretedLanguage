"""
File used to test lexer's functionality
"""

from Lexer import Lexer

testFile = open("Test")

source = testFile.read()

lexer = Lexer(source)

for token in lexer.scan():
    print(token)