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

		return [commandType, line]


	def parse(self, line):

		if self._isWhitespaces(line):
			return [None, None]
		line = self._clearInlineComment(line)
		return self._checkType(line)