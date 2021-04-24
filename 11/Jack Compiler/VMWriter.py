import os

class VMWriter():
	"""docstring for VMWriter"""
	def __init__(self, filePath):
		#create output file for vm file
		self.outputVMFileName = os.path.splitext(os.path.basename(filePath))[0] + '.vm'
		self.outputVMFile = open('.\\output\\'+ self.outputVMFileName, 'w')

	def _writeOutput(self, command):
		self.outputVMFile.write(command + '\n') 

	def writePush(self, segment, index):
		command = "push " + segment + ' ' + str(index)
		self._writeOutput(command)

	def writePop(self, segment, index):
		command = "pop " + segment + ' ' + str(index)
		self._writeOutput(command)

	def writeArithmetic(self, command):
		arithmetics = { '+': 'add', '-': 'sub', '&': 'and', 
						'|': 'or', 'not': 'not', 'neg': 'neg', 
						'=': 'eq', '>': 'gt', '<': 'lt'
						}

		self._writeOutput(arithmetics[command])

	def writeLable(self, label):
		self._writeOutput("label " + label)

	def writeGoto(self, label):
		self._writeOutput("goto " + label)

	def writeIf(self, label):
		self._writeOutput("if-goto " + label)

	def writeCall(self, name, nArgs):
		command = 'call ' + name + ' ' + str(nArgs)
		self._writeOutput(command)


	def writeFunction(self, name, nLocals):
		command = 'function ' + self.outputVMFileName[:-3] + '.' + name + ' ' +str(nLocals)
		self._writeOutput(command)

	def writeReturn(self):
		self._writeOutput("return")



	

