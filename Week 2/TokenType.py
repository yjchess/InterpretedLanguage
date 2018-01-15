"""
TokenType class
This holds all possible types of tokens under a single object
"""

class TokenType:
    # End of file token
    EOF = 0

    # Single character token types
    DOT = 1
    COMMA = 2
    SEMICOLON = 3
    SLASH = 4
    GREATER = 5
    LESS = 6
    EQUAL = 7
    BANG = 8
    STAR = 9
    LPAREN = 10
    RPAREN = 11
    LSQRBRACKET = 12
    RSQRBRACKET = 13
    LBRACE = 14
    RBRACE = 15
    PLUS = 16
    MINUS = 17

    # Double character token types
    LESSEQUAL = 18
    GREATEREQUAL = 19
    EQUALEQUAL = 20
    BANGEQUAL = 21

    # Multi-character token types
    FLOAT = 22
    INTEGER = 23
    STRING = 24
    IDENTIFIER = 25
    KEYWORD = 26
    BOOLEAN = 27
    BUILTINTYPE = 28
