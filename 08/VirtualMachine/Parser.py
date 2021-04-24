class Parser():

    def _isWhitespaces(self, line):
        return line[0:2] == '//' or self._isBlankLine(line)


    def _isBlankLine(self, line):
        return line == '\n'


    def _clearInlineComment(self, line):
        pureCommands = ''

        for i in line:
            if i == '/':
                break
            pureCommands +=i

        return pureCommands

    def _checkType(self, line): #return command type and command
        line = line.split()
        commandType = ''

        if line[0] == 'push':
            commandType = 'C_PUSH'

        elif line[0] == 'pop':
            commandType = 'C_POP'

        elif line[0] in 'add sub neg eq gt lt and or not':
            commandType = 'C_ARITHMETIC'

        elif line[0] == 'label':
            commandType = 'C_LABEL'

        elif line[0] == 'goto':
            commandType = 'C_GOTO'

        elif line[0] == 'if-goto':
            commandType = 'C_IF'

        elif line[0] == 'function':
            commandType = 'C_FUNCTION'

        elif line[0] == 'return':
            commandType = 'C_RETURN'

        elif line[0] == 'call':
            commandType = 'C_CALL'

        return [commandType, line]


    def parse(self, line):

        if self._isWhitespaces(line):
            return [None, None]
        line = self._clearInlineComment(line)
        return self._checkType(line)
