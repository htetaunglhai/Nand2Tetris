from Function import *

symbolTable = {"SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4,"R0":0, "R1":1,
"R2":2, "R3":3, "R4":4, "R5":5, "R6":6, "R7":7, "R8":8, "R9":9,"R10":10,
"R11":11, "R12":12, "R13":13, "R14":14, "R15":15, 'SCREEN': 16384, "KBD":24576}


compTable = {
'0': '101010', 
'1': '111111', 
'-1': '111010', 
'D': '001100', 
'A': '110000', 
'M': '110000', 
'!D': '001101', 
'!A': '110001', 
'!M': '110001', 
'-D': '001111', 
'-A': '110011', 
'-M': '110011', 
'D+1': '011111', 
'A+1': '110111', 
'M+1': '110111',
'D-1': '001110', 
'A-1': '110010', 
'M-1': '110010', 
'D+A': '000010', 
'D+M': '000010', 
'D-A': '010011', 
'D-M': '010011', 
'A-D': '000111', 
'M-D': '000111',
'D&A': '000000', 
'D&M': '000000', 
'D|A': '010101', 
'D|M': '010101'
}



LastVarLocation = 16

print("What is the name of the file?")
filename = input()

with open(filename) as fileObject:
    file = fileObject.readlines()

#clear the comments 
rawCodes = removeCmt(file) 

#clear inline comments and get pure asm code
codes = [] 
for i in range(len(rawCodes)):
    cd = clearInlineCmt(rawCodes[i])
    if(isBlankLine(rawCodes[i]) == False):
    	if(cd != ''):
    		codes.append(cd.strip())

#Lables are removed
labelessCodes = []
numOfLabel = 0
for linenum in range(len(codes)):
	currentLine = codes[linenum]
	if (isLable(currentLine)):
		lableName = currentLine[1:-1]
		symbolTable[lableName] = linenum - numOfLabel
		numOfLabel += 1
		continue 
	labelessCodes.append(currentLine)

outputCodes = []

for codeline in range(len(labelessCodes)):
	translatedCode = ''
	currentLine = labelessCodes[codeline]

	if isA(currentLine):
		aIns = currentLine[1:]

		if aIns.isdigit():
			translatedCode = decToBin(aIns)
		elif(aIns not in symbolTable):
			symbolTable[aIns] = LastVarLocation
			translatedCode = decToBin(LastVarLocation)
			LastVarLocation += 1
		elif(aIns in symbolTable):
			translatedCode = decToBin(symbolTable[aIns])

		translatedCode = addExtraZero(translatedCode)

	elif isC(currentLine):
		dest, comp, jump = parseCInst(currentLine)
		dBits = genDBits(dest)
		cBits = genCBit(compTable, comp)
		jBits = genJBit(jump)
		aBit =  hasAOrNot(comp)

		translatedCode = '111'+aBit+cBits+dBits+jBits 


	outputCodes.append(translatedCode)

	
outfilename = filename[:-4] + '.hack'
with open(outfilename, 'w') as file_object:
	for line in  outputCodes:
		file_object.write(line + '\n')




input()