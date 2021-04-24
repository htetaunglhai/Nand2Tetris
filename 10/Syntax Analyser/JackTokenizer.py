import JackGrammar
class JackTokenizer():

    def tokenize(self, source):
        self.sourceCode = self._getSourceCode(source)
        self.tokens = self._tokenize(self.sourceCode)
        return self.tokens



    def _getSourceCode(self, filePath):
        code = open(filePath)
        return code.readlines()


    def _checkTokenType(self, word):

        # check if symbol
        if len(word) == 1 and self._isSymbol(word):
                return 'symbol'

        # check if string
        elif self._isStringConstStarts(word[0]):
            return 'stringConstant'

        # check if integer
        elif self._isIntConst(word):
            return 'integerConstant'

        # check if keyword
        elif self._isKeyword(word):
            return 'keyword'

        # check if identifier
        elif self._isIdentifier(word):
            return 'identifier'


    def _isSymbol(self, char):
        grammar = JackGrammar.JackGrammar()
        return char in grammar.symbol

    def _isNewLine(self, codeLine):
        return codeLine == '\n'

    def _isStringConstStarts(self, char):
        return char == '"'

    def _isIntConst(self, word):
        return word in '0123456789'

    def _isKeyword(self, word):
        grammar = JackGrammar.JackGrammar()
        return word in grammar.keyword

    def _isIdentifier(self, word):
        invalidWords = '`~!@#$%^&'
        return word[0] not in '0123456789' and word not in invalidWords

    def _isMultCmt(self, codeLine):
        if len(codeLine) > 1:
            return codeLine[0:2] == "/*"
        return False


    def _isMultCmtEnd(self, codeLine):

        if len(codeLine) > 1:
            return codeLine[-2] + codeLine[-1] == "*/"
        else:
            return False

    def _isSingleCmt(self, string):
        if len(string) > 1:
            return string[0:2] == "//"
        return False

    def _isSpace(self, char):
        return char == " "

    def _isTempNotEmpty(self, tempWord):
        return tempWord != ""



    def _makeToken(self, word, tokenType):
        token = ""
        if word == '<':
            token = '&lt;'
        elif word == '>':
            token = '&gt;'
        else:
            token = word
        return '<' + tokenType + '> ' + token.replace('"', '') + ' </' + tokenType + '>'



    def _getToken(self, word):   #:write
        tokenType = self._checkTokenType(word)
        return self._makeToken(word, tokenType)


    def _tokenize(self, sourceCode):   # Pass the jack source code file and it returns Jack tokens
        multCmtMode = None
        stringMode = None
        temp = ""
        tempTokens = []

        for line in sourceCode: # Loop through each line in source code

            if self._isNewLine(line):

                continue
            else:
                currentLine = line.strip()

            # Removed unwanted spaces from the left
            #Handle the comments
            if self._isMultCmt(currentLine):  # Check if current line contains multi-line comment.

                if self._isMultCmtEnd(currentLine): # If this comment is ended in one line, go to next line.
                    continue
                else:
                    multCmtMode = True  # Multi-line comment mode on and go to next line.
                    continue

            elif multCmtMode:
                if self._isMultCmtEnd(currentLine):   # check if multi-line comment ended.
                    multCmtMode = False  # Out of multi-line commment loop
                    continue
                else:
                    continue   # still in multi-line comment
            elif self._isSingleCmt(currentLine): # handle for single line comment
                continue
            elif self._isNewLine(currentLine): # if blank line, continue
                continue
            else:
                # Handle the source codes
                for char in currentLine:  # loop each char in current line
                    if not stringMode:
                        if self._isStringConstStarts(char): # check if string constant starts
                            stringMode = True
                        elif self._isSpace(char): # if char is space, there might be token in temp
                            if self._isTempNotEmpty(temp):
                                tempTokens.append(self._getToken(temp))
                                temp = ""
                            else:   continue

                        elif self._isSymbol(char):
                            if self._isTempNotEmpty(temp):
                                tempTokens.append(self._getToken(temp))
                                temp = ""
                                tempTokens.append(self._getToken(char))
                            else:
                                tempTokens.append(self._getToken(char))
                        else:
                            temp = temp + char

                    elif stringMode:
                        if not char == '"': # keep adding to temp till we found string end (")
                            temp = temp + char
                        else:
                            tempTokens.append(self._getToken('"' + temp + '"'))     # Added double quote at the start and end so we can know it is the string
                            temp = ""
                            stringMode = False

        return tempTokens






