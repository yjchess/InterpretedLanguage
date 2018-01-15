"""
Token class
Tokens each have a type, a lexeme and line.
The type tells us what type this token is. This is a TokenType object.
The lexeme is the set of characters that make up this token. This will typically be a string or character.
The line corresponds to the line number that we scanned this token on. This is useful for error handling.
"""

class Token:
    # Constructor taking in token type, lexeme and line number
    def __init__(self, lexeme, tokType, line):
        self.__lexeme = lexeme
        self.__type = tokType
        self.__line = line

    # Getters for each private field
    def getLexeme(self):
        return self.__lexeme

    def getType(self):
        return self.__type

    def getLine(self):
        return self.__line

    # Overriding __str__ to allow nicer printing of tokens for debugging
    # __str__ is called whenever you print this object : print(Token)
    def __str__(self):
        return "<'{}', {}>".format(self.__lexeme, self.__type)