######## Constants 

DIGITS = '0123456789'

#### ERROR

class Error:
    def __init__(self,error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self,details):
        super().__init__('Illegal Character', details)


#TOKEN

TT_INT      =   'INT'
TT_FLOAT    =   'FLOAT'
TT_PLUS     =   'PLUS'
TT_MINUS    =   'MINUS'
TT_MUL      =   'MUL'
TT_DIV      =   'DIV'
TT_LPAREN   =   'LPAREN'
TT_RPAREN   =   'RPAREN'
WHITESPACE  =   ' '

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    
########## LEXER

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        token = []

        while self.current_char != None:
            if self.current_char in '\t' :
                self.advance()
            elif self.current_char in DIGITS:
                token.append(self.make_number())
            elif self.current_char == '+':
                token.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                token.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                token.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                token.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                token.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                token.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == ' ':
                # token.append(Token(WHITESPACE))
                self.advance()
            
            else:
                # return some error
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return token, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))      

######## RUN 
        
def run(text):
    lexer   = Lexer(text)
    tokens, error = lexer.make_tokens()  

    return tokens, error 


    