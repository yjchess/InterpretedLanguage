"""
Lexer class
A lexer is used to scan through a source file and break it up into tokens. These tokens are what is passed as input to
the parser.
"""

from Token import *
from TokenType import *

class Lexer:
    # Source file is passed in and other useful variables are setup
    def __init__(self, source):
        self.__source = source

        self.__lookahead = ''
        self.__index = -1 # We use consume to increment this to 0

        self.__line = 1

        self.__keywords = ["if", "else", "while", "null"]
        self.__booleans = ["true", "false"]

        self.__tokens = []

    # 'Eats' the current character
    def consume(self):
        self.__index += 1 # Increment the current position in the source
        if self.__index >= len(self.__source): # Check if we are at the end of the file
            self.__lookahead = '\0' # Set the eof marker
            return
        self.__lookahead = self.__source[self.__index] # Set the lookahead to the character at the new index

    # Checks if we see this character and advances if so
    def match(self, char):
        if char == self.__lookahead: # Have we seen this character
            self.consume() # Eat it
            return True
        return False

    # Gets the previous character scanned
    def previous(self):
        return self.__source[self.__index-1]

    # Checks if the current character is a letter
    def isLetter(self):
        return (ord('a') <= ord(self.__lookahead) <= ord('z')) or (ord('A') >= ord(self.__lookahead) <= ord('Z'))

    # Checks if the current character is a digit
    def isDigit(self):
        return self.__lookahead in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Scans the source file returning the tokens produced at the end
    def scan(self):
        self.consume()
        while self.__lookahead != '\0': # While we are not at the end of file
        # Whitespace
            while self.__lookahead in [' ', '\n', '\t']: # We ignore any whitespace
                if self.__lookahead == '\n': # Increment our line if we see a newline character
                    self.__line += 1
                self.consume()

        # Double character tokens
            if self.match('/'):
                if self.match('/'): # Are we in an inline comment
                    while self.__lookahead != '\n': # Ignore all characters on the remainder of this line
                        self.consume()
                else:
                    self.__tokens.append(Token(self.previous(), TokenType.SLASH, self.__line))

            elif self.match('>'):
                if self.__lookahead == '=':
                    self.__tokens.append(Token(self.previous()+self.__lookahead, TokenType.GREATEREQUAL, self.__line))
                else:
                    self.__tokens.append(Token(self.previous(), TokenType.GREATER, self.__line))

            elif self.match('<'):
                if self.__lookahead == '=':
                    self.__tokens.append(Token(self.previous()+self.__lookahead, TokenType.LESSEQUAL, self.__line))
                else:
                    self.__tokens.append(Token(self.previous(), TokenType.LESS, self.__line))

            elif self.match('='):
                if self.__lookahead == '=':
                    self.__tokens.append(Token(self.previous()+self.__lookahead, TokenType.EQUALEQUAL, self.__line))
                else:
                    self.__tokens.append(Token(self.previous(), TokenType.EQUAL, self.__line))

            elif self.match('!'):
                if self.__lookahead == '=':
                    self.__tokens.append(Token(self.previous()+self.__lookahead, TokenType.BANGEQUAL, self.__line))
                else:
                    self.__tokens.append(Token(self.previous(), TokenType.BANG, self.__line))

        # Multi-character tokens
            elif self.match('"'): # String matching
                string = ""
                while not self.match('"'):
                    string += self.__lookahead # Concatenate each character in the string to our temp
                    self.consume()
                self.__tokens.append(Token(string, TokenType.STRING, self.__line))

            elif self.isLetter(): # Identifier/keyword matching
                identifier = ""
                while self.isLetter() or self.isDigit() or self.__lookahead == '_':
                    identifier += self.__lookahead
                    self.consume()

                if identifier in self.__keywords: # Check if this is a keyword
                    self.__tokens.append(Token(identifier, TokenType.KEYWORD, self.__line))
                elif identifier in self.__booleans: # Check if it is a boolean
                    self.__tokens.append(Token(identifier, TokenType.BOOLEAN, self.__line))
                else:
                    self.__tokens.append(Token(identifier, TokenType.IDENTIFIER, self.__line))

            elif self.isDigit(): # Matching integers and floats
                number = 0
                while self.isDigit() and self.__lookahead != '.':
                    number = number * 10 + int(self.__lookahead)
                    self.consume()

                if self.match('.'): # Is this a float
                    fraction = 0 # Stores the fractional part of the number
                    place = 1 # Used for calculating value of current digid
                    while self.isDigit():
                        number += int(self.__lookahead) / 10**place
                        place += 1
                        self.consume()
                    self.__tokens.append(Token(float(number+fraction), TokenType.FLOAT, self.__line))
                else:
                    self.__tokens.append(Token(int(number), TokenType.INTEGER, self.__line))

        # Single character tokens
            elif self.match('.'):
                self.__tokens.append(Token(self.previous(), TokenType.DOT, self.__line))
            elif self.match(','):
                self.__tokens.append(Token(self.previous(), TokenType.COMMA, self.__line))
            elif self.match(';'):
                self.__tokens.append(Token(self.previous(), TokenType.SEMICOLON, self.__line))
            elif self.match('*'):
                self.__tokens.append(Token(self.previous(), TokenType.STAR, self.__line))
            elif self.match('('):
                self.__tokens.append(Token(self.previous(), TokenType.LPAREN, self.__line))
            elif self.match(')'):
                self.__tokens.append(Token(self.previous(), TokenType.RPAREN, self.__line))
            elif self.match('['):
                self.__tokens.append(Token(self.previous(), TokenType.LSQRBRACKET, self.__line))
            elif self.match(']'):
                self.__tokens.append(Token(self.previous(), TokenType.RSQRBRACKET, self.__line))
            elif self.match('{'):
                self.__tokens.append(Token(self.previous(), TokenType.LBRACE, self.__line))
            elif self.match('}'):
                self.__tokens.append(Token(self.previous(), TokenType.RBRACE, self.__line))
            elif self.match('+'):
                self.__tokens.append(Token(self.previous(), TokenType.PLUS, self.__line))
            elif self.match('-'):
                self.__tokens.append(Token(self.previous(), TokenType.MINUS, self.__line))

        # Error
            else:
                raise Exception("Line {}: unidentified character {}".format(self.__line, self.__lookahead))

        # Add eof token to end and return tokens
        self.__tokens.append(Token('eof', TokenType.EOF, None))
        return self.__tokens