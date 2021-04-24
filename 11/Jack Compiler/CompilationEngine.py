import sys, os, JackGrammar, SymbolTable,  VMWriter

class CompilationEngine():
  def __init__(self, tokens, FilePath):
    self.tokenList = tokens
    self.tokenLength = len(self.tokenList)
    self.tokenIndex = 0
    self.currentToken = self._getCurrentToken()
    self.currentTokenValue = self._getTokenValue(self.currentToken)
    self.indent = 0 # for line indent in XML file.
    self.tempList = []
    self.currentClassName = ""
    self.currentSubName = ""
    self.currentSubType = "" # constructor, function or method
    self.currentSubDataType = "" # return data type
    self.labelCounter = 0
    self.outputXMLFileName = os.path.splitext(os.path.basename(FilePath))[0] + '.xml'
    self.outputXMLFile = open('.\\output\\'+ self.outputXMLFileName, 'w')
    self.JackGrammar = JackGrammar.JackGrammar()
    self.classSymbolTable = SymbolTable.SymbolTable()
    self.subSymbolTable = SymbolTable.SymbolTable()
    self.vm = VMWriter.VMWriter(FilePath)
    self.vmSegment  = [] 

  def compile(self):
    self._compileClass()


  def _getLabel(self, lableType):
    self.labelCounter += 1
    return self.currentClassName + "_" + self.currentSubName + "_" + lableType + "_" + str(self.labelCounter)

  def _translateVar(self, token):
    # First, check in current subroutine table.
    var = self.subSymbolTable.getVarScope(token)
    if var != None:
      if var[0] == 'var':
        var[0] = 'local'

      self.vmSegment = var
      return

    # Second, check in class table.
    var = self.classSymbolTable.getVarScope(token)
    if var != None:
      if var[0] == 'field':
        var[0] = 'this'
      self.vmSegment = var
      return

    print('Error: var not found!')
    self._throwError()

  def _increaseTokenIndex(self):
    self.tokenIndex += 1

  def _updateCurrentToken(self):
    self._increaseTokenIndex()
    if self.tokenIndex > self.tokenLength - 1:
      return
    self.currentToken = self._getCurrentToken()
    self.currentTokenValue = self._getTokenValue(self.currentToken)

  def _getCurrentToken(self):
    return self.tokenList[self.tokenIndex]


  def _getTokenType(self, token):
    tokenType = ''
    for alphabet in token[1:]:
      if alphabet ==  '>':
        break

      tokenType += alphabet
    return tokenType


  def _getTokenValue(self, token):
    tokenValue = ''

    firstLetterFound = False
    for i in range(len(token)):
      if token[i] == '>':
        firstLetterFound = True
        continue
      if firstLetterFound and token[i] != '<':
        tokenValue += token[i]
      if firstLetterFound and token[i] == '<':
        break

    return tokenValue.strip()

  def _isIdentifier(self):
    return self._getTokenType(self.currentToken) == 'identifier'

  def _isExpression(self):
  	return ((self._getTokenType(self.currentToken) in 'integerConstant stringConstant'.split())
      or (self.currentTokenValue in '( - ~ true false null this'.split()) #For unaryOp and KeywordConstant
      or (self._isIdentifier())) #for subroutineCall, varName

  def _startNonTerminal(self, nonTerminalType):
    self.outputXMLFile.write(' ' * self.indent + '<' + nonTerminalType + '>' + '\n')
    self.indent +=2

  def _endNonTerminal(self, nonTerminalType):
    self.indent -=2
    self.outputXMLFile.write(' ' * self.indent + '</' + nonTerminalType + '>' + '\n')

  def _writeCurrentTokenToOutput(self):
    self.outputXMLFile.write(' ' * self.indent + self.currentToken + '\n')

  def _throwError(self):
    self.outputXMLFile.write("=======================" + '\n')
    self.outputXMLFile.write("Compilation error occured!" + '\n')
    self.outputXMLFile.write(self._getCurrentToken() + '\n')
    self.outputXMLFile.write(self.currentTokenValue + '\n')
    self.outputXMLFile.write("=======================")
    sys.exit()

  def _handleValue(self, tokenValues, opt=None):

    #currentTokenValue = self._getTokenValue(tokenList[tokenIndex])
    if self.currentTokenValue in tokenValues:
      if opt == "saveToTemp":
        if self.currentTokenValue == 'var':
          self.tempList.append('local')
        
        else:
          self.tempList.append(self.currentTokenValue)
      
      elif opt == "saveSubType":
        self.currentSubType = self.currentTokenValue

      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()

    else:
      self._throwError()

  def _handleIdentifier(self, opt=None):
    if self._isIdentifier():
      if opt == "saveclassName":
        self.currentClassName = self.currentTokenValue 

      elif opt == "addToClassSymTbl":
        self.classSymbolTable.define(self.tempList + [self.currentTokenValue])
      
      elif opt == "addToSubSymTbl":
        self.subSymbolTable.define(self.tempList + [self.currentTokenValue])
      
      elif opt == 'saveSubName':
        self.currentSubName = self.currentTokenValue

        
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()

    else:
      self._throwError()

  def _handleType(self, opt=None):

    if (self.currentTokenValue in 'int char boolean'.split()) or (self._isIdentifier()):
      if opt == "saveToTemp": 
        #for symbol table
        self.tempList.append(self.currentTokenValue) 

      elif opt == "saveSubDataType":
        self.currentSubDataType = self.currentTokenValue 
      
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()

    else:
      self._throwError()


  def  _handleZeroOrMoreToken(self, compileType, opt=None):
    
    if compileType == "classVarDec":
      while True:
        if self.currentTokenValue not in 'static field'.split():
          break        
        self._compileClassVarDec()

    elif compileType == "subroutineDec":
      while True:
        if self.currentTokenValue not in 'constructor function method'.split():
          break        
        self._compileSubroutineDec()

    elif compileType == "commaVarName":
      while True:
        if self.currentTokenValue not in ',':
          break
        self._handleValue(',')
        if opt == 'saveForSub':
          self._handleIdentifier("addToSubSymTbl")
        else:
          self._handleIdentifier("addToClassSymTbl")

    elif compileType == "parameterList":
      while True:
        if self.currentTokenValue not in ',':
          break 

        self._handleValue(',')
        self.tempList.pop() # Need to remove last item before adding next type.
        self._handleType("saveToTemp")
        self._handleIdentifier("addToSubSymTbl")

    elif compileType == "varDec":
      while True:
        if self.currentTokenValue not in 'var':
          break        
        self._compileVarDec()
      
    elif compileType == "opTerm":      
      while True:
        if self.currentTokenValue not in self.JackGrammar.operators:
          break
          
        op = self.currentTokenValue 
        self._handleValue(self.JackGrammar.operators)
        self._compileTerm()
        if op == "*":
          self.vm.writeCall('Math.multiply', 2)

        elif op == "/":
          self.vm.writeCall('Math.divide', 2) 

        else:
          if op == "&lt;":
            op = '<'
          elif op == "&gt;":
            op = '>'
          elif op == "&amp;":
            op = '&'
            
          self.vm.writeArithmetic(op)   
        
    elif compileType == "commaExpression":
      expListCounter = opt
      while True:
        if self.currentTokenValue not in ',':
          return expListCounter

        self._handleValue(',')
        expListCounter += 1
        self._compileExpression()

    elif compileType == "statements":
      while True:
        if self.currentTokenValue not in 'let if while do return'.split():
          break
        self._compileStatement()

  def _compileClass(self):
    self._startNonTerminal('class')
    self._handleValue('class')
    self._handleIdentifier("saveclassName")
    self._handleValue('{')
    self.classSymbolTable.reset()
    self._handleZeroOrMoreToken('classVarDec')
    self._handleZeroOrMoreToken('subroutineDec')
    self._handleValue('}')
    self._endNonTerminal('class')


  def _compileClassVarDec(self):
    self._startNonTerminal('classVarDec')
    self._handleValue('static field'.split(), "saveToTemp") 
    self._handleType("saveToTemp")
    self._handleIdentifier("addToClassSymTbl") #add a new entry to class symbol table 
    self._handleZeroOrMoreToken('commaVarName')
    self.tempList = [] #clear tempList to be ready for next uses 
    self._handleValue(';')
    self._endNonTerminal('classVarDec') 

  def _compileSubroutineDec(self):
    self.subSymbolTable.reset()

    self._startNonTerminal('subroutineDec')
    self._handleValue('constructor function method'.split(), "saveSubType")
    if self.currentTokenValue == 'void':
      self.currentSubDataType = 'void'
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()
    else:
      self._handleType('saveSubDataType')

    self._handleIdentifier('saveSubName') #Compile subroutineName
    self._handleValue('(')

    if self.currentSubType == 'method': # if this is method, set this as arg 0.
      self.subSymbolTable.define(['argument', self.currentClassName, 'this'])

    self._compileParameterList()
    self._handleValue(')')      
    self._compileSubroutineBody()
    self._endNonTerminal('subroutineDec')

  def _compileParameterList(self):
    self._startNonTerminal('parameterList')
    self.tempList.append('argument') #because parameters are arguments.

    if (self.currentTokenValue in 'int char boolean'.split()) or (self._isIdentifier()): # Check if current token is type 
      self._handleType("saveToTemp")
      self._handleIdentifier("addToSubSymTbl")
      
      if self.currentTokenValue == ',':
        self._handleZeroOrMoreToken('parameterList')

    self.tempList = [] #clear tempList for next uses 
    self._endNonTerminal('parameterList')

  def _compileSubroutineBody(self):
    self._startNonTerminal('subroutineBody')
    self._handleValue('{')
    self._handleZeroOrMoreToken('varDec')
    self.vm.writeFunction(self.currentSubName, self.subSymbolTable.countVar('local'))

    # if constructor, call os to create fields.
    if self.currentSubType == 'constructor':
      self.vm.writePush('constant', self.classSymbolTable.countVar('field'))
      self.vm.writeCall('Memory.alloc', 1)
      self.vm.writePop('pointer', 0)
    
    # if method, set current obj addr to pointer 0.
    elif self.currentSubType == 'method':
      self.vm.writePush('argument', 0)
      self.vm.writePop('pointer', 0)

    self._compileStatements()
    self._handleValue('}')
    self._endNonTerminal('subroutineBody')

  def _compileVarDec(self):
    self._startNonTerminal('varDec')
    self._handleValue('var', 'saveToTemp') #save variable scope 
    self._handleType('saveToTemp') # save variable type
    self._handleIdentifier('addToSubSymTbl') # take variable name and add to symbol table
    self._handleZeroOrMoreToken('commaVarName', 'saveForSub')
    self.tempList = [] 
    self._handleValue(';')
    self._endNonTerminal('varDec')


  def _compileStatements(self):
    self._startNonTerminal('statements')
    self._handleZeroOrMoreToken('statements')
    self._endNonTerminal('statements')

  def _compileStatement(self):
    if self.currentTokenValue == 'let':
    	self._compileLetStatement()
    elif self.currentTokenValue == 'if':
    	self._compileIfStatement()
    
    elif self.currentTokenValue == 'while':
    	self._compileWhileStatement()
    
    elif self.currentTokenValue == 'do':
    	self._compileDoStatement()
    
    elif self.currentTokenValue == 'return':
    	self._compileReturnStatement()
    	
    else:	self._throwError()


  def _compileLetStatement(self):
    self._startNonTerminal('letStatement')
    lhsIsArray = False 
    self._handleValue('let')
    # save var for later pop 
    tempVar = self.currentTokenValue
    self._handleIdentifier()
    
    if self.currentTokenValue == '[':
      lhsIsArray = True
      # push var saved above
      self._translateVar(tempVar)
      self.vm.writePush(self.vmSegment[0], self.vmSegment[1])

      self._handleValue('[')
      self._compileExpression()
      self._handleValue(']')
      self.vm.writeArithmetic('+') 

    self._handleValue('=')
    self._compileExpression()
    
    if lhsIsArray:
      self.vm.writePop('temp', '0')
      self.vm.writePop('pointer', '1')
      self.vm.writePush('temp', '0');
      self.vm.writePop('that', '0')

    else:
      self._translateVar(tempVar)
      self.vm.writePop(self.vmSegment[0], self.vmSegment[1])
      
    self._handleValue(';')
    self._endNonTerminal('letStatement')

  def _compileIfStatement(self):
    ifLabel = self._getLabel('if')
    elseLabel = ifLabel + "_false"
    endLabel = ifLabel + "_end"

    self._startNonTerminal('ifStatement')
    self._handleValue('if')
    self._handleValue('(')
    self._compileExpression()
    self.vm.writeArithmetic('not') # Called 'not' to know that the condidition is false.
    self.vm.writeIf(elseLabel) # jump to else-block 
    self._handleValue(')')
    self._handleValue('{')
    self._compileStatements()
    self._handleValue('}')
    # When the true-block end, go to the end label
    self.vm.writeGoto(endLabel)
    #Create else label
    self.vm.writeLable(elseLabel)

    if self.currentTokenValue == 'else':
      self._handleValue('else')
      self._handleValue('{')
      self._compileStatements()
      self._handleValue('}')

    # Create end label
    self.vm.writeLable(endLabel)


    self._endNonTerminal('ifStatement')

  def _compileWhileStatement(self):
    whileLabel = self._getLabel('while')
    whileEndLable = whileLabel + '_end'

    self._startNonTerminal('whileStatement')

    self._handleValue('while')
    self._handleValue('(')
    self.vm.writeLable(whileLabel)
    self._compileExpression()
    self._handleValue(')')
    self.vm.writeArithmetic('not')
    self.vm.writeIf(whileEndLable)
    self._handleValue('{')
    self._compileStatements()
    self._handleValue('}')
    
    self.vm.writeGoto(whileLabel)
    self.vm.writeLable(whileEndLable)

    self._endNonTerminal('whileStatement')

  def _compileDoStatement(self):
    self._startNonTerminal('doStatement')
    self._handleValue('do')
    self._compileSubRoutineCall()

    self.vm.writePop('temp', '0')
    self._handleValue(';')
    self._endNonTerminal('doStatement')    

  def _compileReturnStatement(self):
    self._startNonTerminal('returnStatement')
    self._handleValue('return')
    
    if self._isExpression():
    	self._compileExpression()

    if self.currentSubDataType == 'void':
      self.vm.writePush('constant', '0')

    self._handleValue(';')
    self.vm.writeReturn()
    self._endNonTerminal('returnStatement')
    
    

  def _compileExpression(self):
    self._startNonTerminal('expression')
    self._compileTerm()
    self._handleZeroOrMoreToken('opTerm')
    self._endNonTerminal('expression')

  def _compileTerm(self):
    self._startNonTerminal('term')
    tokenType = self._getTokenType(self.currentToken)
    if tokenType == "integerConstant" or tokenType == "stringConstant" or self.currentTokenValue in 'true false null this'.split():
      
      if tokenType == "integerConstant":
        self.vm.writePush('constant', self.currentTokenValue)

      elif tokenType == "stringConstant":
        # count the length of string
        stringLength = len(self.currentTokenValue)
        # push string length
        self.vm.writePush('constant', stringLength)
        # call String.new 1
        self.vm.writeCall('String.new', 1)
        # loop lenght of string times to append char
        for char in self.currentTokenValue:
          self.vm.writePush('constant', ord(char))
          self.vm.writeCall('String.appendChar', 2)

        # debug
        print(self.currentTokenValue)

      elif self.currentTokenValue in 'true false null this'.split():
        if self.currentTokenValue == 'true':
          self.vm.writePush('constant', 0)
          self.vm.writeArithmetic('not')
      
        elif self.currentTokenValue == 'false':
          self.vm.writePush('constant', 0)
      
        elif self.currentTokenValue == 'null':
          self.vm.writePush('constant', 0)

        elif self.currentTokenValue == 'this':
          self.vm.writePush('pointer', 0)

      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()

    elif self.currentTokenValue == '(':
      # handle for expression
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()
      self._compileExpression()
      self._handleValue(')')

    elif self.currentTokenValue in '- ~'.split(): # check if it is unaryOp
      token = self.currentTokenValue
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()
      self._compileTerm()
      
      if token == '-':
        self.vm.writeArithmetic('neg')
      elif token == '~':
        self.vm.writeArithmetic('not')

    
    elif  self._isIdentifier():
      nextTokenValue = self._getTokenValue(self.tokenList[self.tokenIndex + 1])
      if nextTokenValue in '( .'.split():
        # handle for subRoutineCall
        self._compileSubRoutineCall() 
      elif nextTokenValue == '[':
        # handle for varName and expression
        tempVar = self.currentTokenValue
        self._writeCurrentTokenToOutput() # for varName
        self._updateCurrentToken()
        
        self._translateVar(tempVar)
        self.vm.writePush(self.vmSegment[0], self.vmSegment[1])

        self._writeCurrentTokenToOutput() # for [ symbol
        self._updateCurrentToken() 
        self._compileExpression()
        self._handleValue(']')

        self.vm.writeArithmetic('+')
        self.vm.writePop('pointer', 1)
        self.vm.writePush('that', 0)
             
      else:
        # handle varName only 
        self._translateVar(self.currentTokenValue)
        self._handleIdentifier()
        self.vm.writePush(self.vmSegment[0], self.vmSegment[1])

    else: self._throwError()

    self._endNonTerminal('term')     
  
  def _compileSubRoutineCall(self):
    identifier = self.currentTokenValue # saved for later use as an object or a class name
    self._handleIdentifier()

    if self.currentTokenValue == '(':
      self.vm.writePush('pointer', '0')
      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()
      expListCounter = self._compileExpressionList()
      self._handleValue(')')
      self.vm.writeCall(self.currentClassName + '.' + identifier, expListCounter + 1) # + 1 for pointer 0

    elif self.currentTokenValue == '.': # It can be OS call or method call

      self._writeCurrentTokenToOutput()
      self._updateCurrentToken()
      methodName = self.currentTokenValue
      self._handleIdentifier()
      self._handleValue('(')
      className = ""

      if identifier in self.classSymbolTable.data: # if identifier is in the class symbol table, it is an object.method()  
        className = self.classSymbolTable.data[identifier][0] # save class type for later call
        self._translateVar(identifier) # Pass the object on which the method is called.
        self.vm.writePush(self.vmSegment[0], self.vmSegment[1])

      elif identifier in self.subSymbolTable.data: # Check again in sub symbol table.
        className = self.subSymbolTable.data[identifier][0] # save class type for later call 
        self._translateVar(identifier) # Pass the object on which the method is called on.
        self.vm.writePush(self.vmSegment[0], self.vmSegment[1])

      expListCounter = self._compileExpressionList()
      if className != "":
        self.vm.writeCall(className + '.' + methodName, expListCounter + 1)

      else:
        self.vm.writeCall(identifier + '.' + methodName, expListCounter) 

      self._handleValue(')')

    else:
      self._throwError()
 
  def _compileExpressionList(self):
    self._startNonTerminal('expressionList')
    expListCounter = 0

    if self._isExpression():
      self._compileExpression()
      expListCounter += 1
      expListCounter = self._handleZeroOrMoreToken('commaExpression', expListCounter)

    self._endNonTerminal('expressionList')

    return expListCounter