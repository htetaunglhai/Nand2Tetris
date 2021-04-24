import sys, os

class CompilationEngine():
  def __init__(self, tokens, FilePath):
    self.tokenList = tokens
    self.tokenLength = len(self.tokenList)
    self.tokenIndex = 0
    self.currentToken = self._getCurrentToken()
    self.currentTokenValue = self._getTokenValue(self.currentToken)
    self.indent = 0
    self.outputFileName = os.path.splitext(os.path.basename(FilePath))[0] + '.xml'
    self.outputFile = open(self.outputFileName, 'a')


  def compile(self):
    self._compileClass()


  def _increaseTokenIndex(self):
    self.tokenIndex += 1

  def _updateCurrentToken(self):
    self._increaseTokenIndex()
    self.currentToken = self._getCurrentToken()
    self.currentTokenValue = self._getTokenValue(self.currentToken)

  def _getCurrentToken(self):
    return self.tokenList[self.tokenIndex]

##    def _getToken(tokenIndex):
##        return self.tokenList[tokenIndex]

##    def _parse(self, type='class'):
##        pass

##outputFile = open(outputFileName + '.asm', 'a')
##
##outputFile.write(codes + '\n')
## :Done replace outFile.write() with _writeCurrentTokenToOutput
## :Done replace increaseTokenindex() with updateCurrentToken()
## :Done setup _handleOneOrMoreToken()
## :Done replace with self.currentTokenValue

  def _getTokenType(self, token):
    tokenType = ''
    for alphabet in token[1:]:
      if alphabet ==  '>':
        break

      tokenType += word
    return tokenType


  def _getTokenValue(self, token):
    tokenValue = ''

    firstLetterFound = False
    for i in len(token):
      if token[i] == '>':
        firstLetterFound = True
        continue
      if firstLetterFound and token[i] != '<':
        tokenValue += token[i]
      if firstLetterFound and token[i] == '<':
        break

    return tokenValue.strip()

  def _isIdnetifier(self):
    return self._getTokenType(self.currentToken) == 'identifier'


  def _startNonTerminal(nonTerminalType):
    outputFile.write(' ' * self.indent + '<' + nonTerminalType + '>')
    self.indent +=1

  def _endNonTerminal(nonTerminalType):
    outputFile.write(' ' * self.indent + '</' + nonTerminalType + '>')
    self.indent -=1

  def _writeCurrentTokenToOutput(self):
    outputFile.write(' ' * self.indent + self.currentToken + '\n')

  def _throwError(self):
    outputFile.write("=======================")
    outputFile.write("An error occured!" + '\n')
    outputFile.write("=======================")
    sys.exit()

  def _handleValue(self, tokenValue):

    #currentTokenValue = self._getTokenValue(tokenList[tokenIndex])
    if self.currentTokenValue in tokenValue:
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()

    else:
      self._throwError()

  def _handleIdentifier(self):
    if self._isIdentifier():
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()

    else:
      self._throwError()

  def _handleType(self):

    if (self.currentTokenValue in 'int char boolean'.split()) or (self._isIdnetifier()):
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()

    else:
      self._throwError()


  def _handleOneOrMoreToken(self, copmileType):
    # oneOrMore = True
    # #Check if the current token value is valid before entering oneOrMore loop
    # if not ((compileType == "classVarDec" and self.currentTokenValue in 'static field'.split()) or 
    # (compileType == "subroutineDec" and self.currentTokenValue in 'static field'.split())
    # (compileType == "commaVarName")
    # ):

    #   oneOrMore = False 
    #   self._throwError() 

    if copmileType == "classVarDec":
      while True:
        self._compileClassVarDec()
        if self.currentTokenValue not in 'static field'.split():
          break
    elif compileType == "subroutineDec":
      while True:
        self._compileSubroutineDec()
        if self.currentTokenValue not in 'constructure function method'.split():
          break
    elif compileType == "commaVarName":
      while True:
        self._handleValue(',')
        self._handleIdentifier()
        if self.currentTokenValue not in ',':
          break
    elif compileType == "parameterList":
      while True:
        self._handleType()
        self._handleIdentifier()
        self._handleValue(',')
        self._handleType()
        self._handleIdentifier()
        if (self._getTokenType(self.currentToken) not in 'int char boolean'.split()) or not self._isIdnetifier():
          break
    elif compileType == "varDec":
      while True:
        self._compileVarDec()
        if self.currentTokenValue not in 'var':
          break




  def _compileClass(self):
    self._startNonTerminal('class')
    self._handleValue('class')
    self._handleIdentifier()
    self._handleValue('{')
    self._handleOneOrMoreToken('classVarDec')
    self._handleOneOrMoreToken('subroutineDec')

    # oneOrMore = True
    # while oneOrMore:
    #   self._compileClassVarDec()
    #   if self._getTokenValue(self.currentToken) not in 'static field'.split():
    #     oneOrMore = False

    # oneOrMore = True
    # while oneOrMore:
    #   self._compileSubroutineDec()
    #   if self._getTokenValue(self.currentToken) not in 'constructure function method'.split():
    #     oneOrMore = False

    self._handleValue('}')
    self._endNonTerminal('class')


  def _compileClassVarDec(self):
    self._startNonTerminal('classVarDec')
    self._handleValue('static field'.split())
    self._handleType()
    self._compileVarName()
    # oneOrMore = True
    
    # while oneOrMore:
    #   if self.tokenList[tokenIndex] == ',':
    #     self._handleValue(',')
    #     self._handleIdentifier()
    #   else:
    #     oneOrMore = False
    self._handleOneOrMoreToken('commaVarName')
    self._handleValue(';')
    self._endNonTerminal('classVarDec') 

  def _compileSubroutineDec(self):
    self._startNonTerminal('subroutineDec')
    self._handleValue('constructure function method'.split())

    if self.currentTokenValue == 'void':
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()
    else:
      self._handleType()

    self._handleIdentifier() #Compile subroutineName
    self._handleValue('(')
    self._compileParameterList()
    self._handleValue(')')
    self._compileSubroutineBody()
    self._endNonTerminal('subroutineDec')

  def _compileParameterList(self):
    self._startNonTerminal('parameterList')

    if self._isIdnetifier():
      self._handleOneOrMoreToken('parameterList')

    self._endNonTerminal('parameterList')

  def _compileSubroutineBody(self):
    self._startNonTerminal('subroutineBody')
    self._handleValue('{')
    self._handleOneOrMoreToken('varDec')
    self._compileStatements()
    self._handleValue('}')
    self._endNonTerminal('subroutineBody')

  def _compileVarDec(self):
    self._startNonTerminal('varDec')
    self._handleValue('var')
    self._handleType()
    self._handleIdentifier()
    self._handleOneOrMoreToken('commaVarName')
    self._handleValue(';')
    self._endNonTerminal('varDec')


  def _compileStatements(self):
    pass

  def _compileStatement(self):
    pass

  def _compileLetStatement(self):
    pass

  def _compileIfStatement(self):
    pass

  def _compileWhileStatement(self):
    pass

  def _compileDoStatement(self):
    pass

  def _compileReturnStatement(self):
    pass

  def _compileExpression(self):
    pass

  def _compileTerm(self):
    pass
  def _compileSubRoutineCall(self):
    pass

  def _compileExpressionList(self):
    pass
