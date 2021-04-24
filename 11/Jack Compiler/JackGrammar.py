
class JackGrammar():
    def __init__(self):
        self.keyword = [
        'class', 'constructor', 'function', 'method', 'field', 'static', 'var',
        'int', 'char', 'boolean', 'void', 'true', 'false',
        'null', 'this', 'let', 'do', 'if','else', 'while', 'return'
        ]

        self.symbol = [
        '{', '}', '(', ')', '[', ']', '.', ',', ';',
        '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'
        ]

        self.operators = ['+', '-', '*', '/', '&', '|', '~', '<', '>', '=', '&lt;', '&gt;', '&amp;']
        self.arithGroup = ['(', ')']
        self.arrayIndex = ['[', ']']
        self.unitGroup = ['{', '}']
        self.varListSeparator = [',']
        self.terminator = [';']
        self.classMembership = ['.']

        self.integerConstant = '0 1 2 3 4 5 6 7 8 9'.split()
        self.stringConstant = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 1 0'.split() + 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
        self.identifier = []
        self.symbol = self.operators + self.arithGroup + self.arrayIndex + self.unitGroup + self.varListSeparator + self.terminator + self.classMembership
        self.lex = self.keyword + self.symbol + self.integerConstant + self.stringConstant + self.identifier










