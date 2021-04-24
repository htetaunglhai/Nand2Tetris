import sys

class SymbolTable():
	"""docstring for SymbolTable"""
	def __init__(self):
		self.data = {} 
		self.static = 0
		self.field = 0
		self.argument = 0
		self.local = 0



	def define(self, symbolList): #list comes in that format -> [scope, type, name, class (only when data type is a class name)]
		tempEntry = []

		#check var type if int
		if symbolList[1] == 'int':
			tempEntry.append('int')

		elif symbolList[1] == 'char':
			tempEntry.append('char')

		elif symbolList[1] == 'boolean':
			tempEntry.append('boolean')

		# this might be a class name
		else:
			tempEntry.append(symbolList[1]) 

		#check var scope and add number
		if symbolList[0] == 'field':
			tempEntry.append('field')
			tempEntry.append(self.field)
			self.field += 1

		if symbolList[0] == 'static':
			tempEntry.append('static')
			tempEntry.append(self.static)
			self.static += 1

		if symbolList[0] == 'argument':
			tempEntry.append('argument')
			tempEntry.append(self.argument)
			self.argument += 1

		if symbolList[0] == 'local':
			tempEntry.append('local')
			tempEntry.append(self.local)
			self.local += 1


		self.data.update({symbolList[2]: tempEntry}) #output format -> name: [type, scope, num]


	def countVar(self, kind):
		if kind == 'static':
			return self.static

		elif kind == 'field':
			return self.field
			
		elif kind == 'argument':
			return self.argument
			
		elif kind == 'local':
			return self.local


	def getVarScope(self, name):
		if name in self.data:
			return (self.data[name][1] + ' ' + str(self.data[name][2])).split()

		return None 

		
	def reset(self):
		self.data = {} 
		self.static = 0
		self.field = 0
		self.argument = 0
		self.local = 0

		
	def throwError():
		print('Error!: Variable not found.')
		sys.exit()

 